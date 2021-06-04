#!/usr/bin/env python3

import os
import sys
import logging
import pathlib
import boto3
from botocore.exceptions import ClientError

basedir = pathlib.Path(os.path.dirname(os.path.dirname(__file__)))
AWS_S3_NIGHTLY_BUCKET = os.getenv("AWS_S3_NIGHTLY_BUCKET")
AWS_S3_NIGHTLY_BASEURI = os.getenv("AWS_S3_NIGHTLY_BASEURI")

def upload_file(file):
    file = f'{file}'
    object_name = f'{os.getenv("TALLY_VERSION")}/{os.path.basename(file)}'

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file, AWS_S3_NIGHTLY_BUCKET, object_name, ExtraArgs={'ACL': 'public-read'})
        print(f'::warning ::Artifact is available at {AWS_S3_NIGHTLY_BASEURI}/{file} for the next days.')
    except ClientError as e:
        logging.error(e)
        return False
    return True

found = False

for file in os.listdir(basedir / "dist"):
    if file.startswith("vtally-"):
        path = basedir / "dist" / file
        logging.info(f'Uploading {file}...')
        if not upload_file(path):
            logging.error(f'Could not upload {path} to S3.')
        else:
            found = True

if not found: 
    logging.error("No file found to upload.")
    sys.exit(-1)
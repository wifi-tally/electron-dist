# Electron Builder for vTally

At its core, vTally is build without Electron. But to make distribution and installation easy
we use Electron to create a file that is installable with a few clicks.

## Development

````bash
npm ci
./node_modules/.bin/electron-rebuild

npm start
````

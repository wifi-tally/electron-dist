# Electron Builder for vTally

At its core, vTally is build without Electron. But to make distribution and installation easy
we use Electron to create a file that is installable with a few clicks.

## Development

````bash
yarn install
./node_modules/.bin/electron-rebuild

yarn start
````

# Logs

* **on Linux**: ~/.config/vtally-electron/logs/main.log
* **on macOS**: ~/Library/Logs/vtally-electron/main.log
* **on Windows**: %USERPROFILE%\AppData\Roaming\vtally-electron\logs\main.log

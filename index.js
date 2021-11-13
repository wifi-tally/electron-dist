// override logging
// @see https://github.com/megahertz/electron-log#overriding-consolelog
Object.assign(console, require('electron-log').functions);

console.log("Using Electron Runner for vTally");
console.log("================================");
console.log("");


const { app, dialog } = require('electron')

let appLock = app.requestSingleInstanceLock()
if (!appLock) {
    dialog.showErrorBox(
        'Multiple instances',
        'Another instance of vTally is already running. Please close the other instance first.'
    )
    app.quit()
    return
}

// start vTally
process.env.NODE_ENV = 'production'
require('vtally/src/server')
require('./src/tray')

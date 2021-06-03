const package = require('vtally/package.json')
const { app, Tray, Menu, dialog } = require('electron')
const open = require("open")

const httpPort = (typeof process.env.PORT === "string" && parseInt(process.env.PORT, 10)) || 3000

const openBrowser = () => {
    open(`http://localhost:${httpPort}`)
}

const exitApp = () => {
    dialog.showMessageBox({
        title: "Really quit vTally?",
        message: "Do you really want to stop vTally?",
        buttons: ["No", "Yes"],
        defaultId: 0,
        cancelId: 0,
    }).then(({response}) => {
        if (response === 1) {
            app.quit()
        }
    })
}

let tray = null
app.whenReady().then(() => {
    tray = new Tray('build/icons/icon.ico')
    const contextMenu = Menu.buildFromTemplate([
        { label: `Tally Hub ${package.version}`, enabled: false },
        { 
            label: 'Open in Browser', 
            toolTip: 'Opens vTally Hub in your default browser',
            click: openBrowser,
        },
        { label: "Seperator", type: "separator" },
        { 
            label: 'Exit', 
            click: exitApp
        }
    ])
    tray.setToolTip('vTally Hub')
    tray.setContextMenu(contextMenu)
    tray.on('double-click', openBrowser)
})

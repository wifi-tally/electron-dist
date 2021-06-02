console.log("Using Electron Runner for vTally");
console.log("================================");
console.log("");

process.env.NODE_ENV = 'production';
require('vtally/src/server');
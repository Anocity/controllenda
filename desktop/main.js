const { app, BrowserWindow } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let mainWindow;
let backendProcess;

function createWindow() {
  const { screen } = require('electron');
  const primaryDisplay = screen.getPrimaryDisplay();
  const { width, height } = primaryDisplay.workAreaSize;

  // Janela com 50% da largura e 70% da altura
  const windowWidth = Math.floor(width * 0.5);
  const windowHeight = Math.floor(height * 0.7);

  mainWindow = new BrowserWindow({
    width: windowWidth,
    height: windowHeight,
    minWidth: 800,
    minHeight: 600,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
    },
    icon: path.join(__dirname, 'icon.ico'),
    title: 'MIR4 Account Manager',
    autoHideMenuBar: true,
  });

  // Load the React app
  mainWindow.loadFile(path.join(__dirname, 'build', 'index.html'));

  mainWindow.on('closed', function () {
    mainWindow = null;
  });
}

function startBackend() {
  const backendPath = path.join(__dirname, 'backend', 'server_desktop.exe');
  
  backendProcess = spawn(backendPath, [], {
    cwd: path.join(__dirname, 'backend'),
  });

  backendProcess.stdout.on('data', (data) => {
    console.log(`Backend: ${data}`);
  });

  backendProcess.stderr.on('data', (data) => {
    console.error(`Backend Error: ${data}`);
  });

  backendProcess.on('close', (code) => {
    console.log(`Backend process exited with code ${code}`);
  });

  // Aguardar backend iniciar
  setTimeout(() => {
    createWindow();
  }, 3000);
}

app.on('ready', () => {
  startBackend();
});

app.on('window-all-closed', function () {
  if (backendProcess) {
    backendProcess.kill();
  }
  app.quit();
});

app.on('activate', function () {
  if (mainWindow === null) {
    createWindow();
  }
});

app.on('quit', function () {
  if (backendProcess) {
    backendProcess.kill();
  }
});

# Script de Build - MIR4 Desktop App
# Execute este script para gerar o executável .exe

Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  MIR4 Account Manager - Build Desktop App" -ForegroundColor Yellow
Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

$ErrorActionPreference = "Stop"
$desktopDir = "desktop"
$frontendDir = "frontend"
$backendFile = "server_desktop.py"

# Step 1: Build Frontend
Write-Host "[1/5] Building Frontend..." -ForegroundColor Green
Set-Location $frontendDir

# Update .env for local backend
$envContent = "REACT_APP_BACKEND_URL=http://127.0.0.1:8001"
$envContent | Out-File -FilePath ".env" -Encoding UTF8

Write-Host "  Installing dependencies..." -ForegroundColor Gray
yarn install --silent

Write-Host "  Building React app..." -ForegroundColor Gray
yarn build

# Copy build to desktop folder
Write-Host "  Copying build to desktop folder..." -ForegroundColor Gray
Copy-Item -Path "build" -Destination "../$desktopDir/build" -Recurse -Force

Set-Location ..

# Step 2: Create Backend Executable
Write-Host ""
Write-Host "[2/5] Creating Backend Executable..." -ForegroundColor Green

# Check if PyInstaller is installed
$pyinstallerCheck = python -m PyInstaller --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "  Installing PyInstaller..." -ForegroundColor Gray
    pip install pyinstaller
}

# Create backend executable
Write-Host "  Compiling Python backend to .exe..." -ForegroundColor Gray
python -m PyInstaller --onefile --name server_desktop --hidden-import uvicorn.protocols.http.auto --hidden-import uvicorn.protocols.websockets.auto --hidden-import uvicorn.lifespan.on "$desktopDir/$backendFile"

# Move executable to desktop/backend folder
Write-Host "  Moving executable..." -ForegroundColor Gray
New-Item -ItemType Directory -Force -Path "$desktopDir/backend" | Out-Null
Move-Item -Path "dist/server_desktop.exe" -Destination "$desktopDir/backend/server_desktop.exe" -Force

# Clean up build files
Remove-Item -Path "build" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "dist" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "server_desktop.spec" -Force -ErrorAction SilentlyContinue

# Step 3: Install Electron dependencies
Write-Host ""
Write-Host "[3/5] Installing Electron dependencies..." -ForegroundColor Green
Set-Location $desktopDir
if (-Not (Test-Path "node_modules")) {
    yarn install
}

# Step 4: Build Electron App
Write-Host ""
Write-Host "[4/5] Building Electron App..." -ForegroundColor Green
Write-Host "  This may take a few minutes..." -ForegroundColor Gray
yarn build

Set-Location ..

# Step 5: Done
Write-Host ""
Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  ✓ Build Complete!" -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""
Write-Host "Executable location:" -ForegroundColor Yellow
Write-Host "  $desktopDir\dist\MIR4 Account Manager Setup.exe" -ForegroundColor White
Write-Host ""
Write-Host "To install:" -ForegroundColor Yellow
Write-Host "  1. Navigate to desktop\dist\" -ForegroundColor White
Write-Host "  2. Run 'MIR4 Account Manager Setup.exe'" -ForegroundColor White
Write-Host "  3. Follow installation wizard" -ForegroundColor White
Write-Host ""
Write-Host "The app will be installed and a desktop shortcut created!" -ForegroundColor Green
Write-Host ""

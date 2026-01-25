@echo off
echo ============================================================
echo   MIR4 Account Manager - Build Desktop App
echo ============================================================
echo.

REM Step 1: Build Frontend
echo [1/5] Building Frontend...
cd frontend
echo REACT_APP_BACKEND_URL=http://127.0.0.1:8001> .env
call yarn install
call yarn build
xcopy /E /I /Y build ..\desktop\build
cd ..

REM Step 2: Install PyInstaller
echo.
echo [2/5] Installing PyInstaller...
pip install pyinstaller

REM Step 3: Create Backend Executable
echo.
echo [3/5] Creating Backend Executable...
python -m PyInstaller --onefile --name server_desktop --hidden-import uvicorn.protocols.http.auto --hidden-import uvicorn.protocols.websockets.auto desktop\server_desktop.py

REM Move files
if not exist "desktop\backend" mkdir desktop\backend
move /Y dist\server_desktop.exe desktop\backend\

REM Clean up
rmdir /S /Q build
rmdir /S /Q dist
del /F /Q server_desktop.spec

REM Step 4: Install Electron dependencies
echo.
echo [4/5] Installing Electron dependencies...
cd desktop
call yarn install

REM Step 5: Build Electron App
echo.
echo [5/5] Building Electron App...
echo This may take a few minutes...
call yarn build
cd ..

echo.
echo ============================================================
echo   Build Complete!
echo ============================================================
echo.
echo Executable location:
echo   desktop\dist\MIR4 Account Manager Setup.exe
echo.
echo To install:
echo   1. Navigate to desktop\dist\
echo   2. Run "MIR4 Account Manager Setup.exe"
echo   3. Follow installation wizard
echo.
pause

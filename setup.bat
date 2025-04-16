@echo off
setlocal enabledelayedexpansion

set PROJECT_DIR=%~dp0
set PYTHON_EXEC=python
set VENV_DIR=%PROJECT_DIR%venv
set REQUIREMENTS_FILE=%PROJECT_DIR%requirements.txt
set SCRIPT_FILE=%PROJECT_DIR%meduza.py
set CONFIG_DIR=%PROJECT_DIR%config

echo Checking if Python is installed...
where %PYTHON_EXEC% >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Python is not installed. Please install Python before continuing.
    pause
    exit /b
)

echo Checking if virtual environment directory exists...
if not exist "%VENV_DIR%" (
    echo Virtual environment not found. Creating one now...
    %PYTHON_EXEC% -m venv "%VENV_DIR%"
) else (
    echo Virtual environment found. Skipping creation.
)

echo Activating virtual environment...
call "%VENV_DIR%\Scripts\activate.bat"

echo Upgrading pip...
pip install --upgrade pip

echo Checking if requirements.txt exists...
if not exist "%REQUIREMENTS_FILE%" (
    echo requirements.txt not found. Skipping dependencies installation.
) else (
    echo Installing dependencies from requirements.txt...
    pip install -r "%REQUIREMENTS_FILE%"
)

echo Checking if the script file exists...
if not exist "%SCRIPT_FILE%" (
    echo Script file %SCRIPT_FILE% not found. Please check the script name.
    pause
    exit /b
)

echo Creating config files...

if not exist "%CONFIG_DIR%" (
    mkdir "%CONFIG_DIR%"
    echo Config directory created.
) else (
    echo Config directory already exists.
)

rem Creating .cfg files
echo Creating config/github_config.cfg...
echo # GitHub Configuration File > "%CONFIG_DIR%\github_config.cfg"
echo api_url=https://api.github.com >> "%CONFIG_DIR%\github_config.cfg"
echo headers={"Accept": "application/vnd.github+json", "User-Agent": "Meduza-Email-Finder"} >> "%CONFIG_DIR%\github_config.cfg"
echo max_retries=3 >> "%CONFIG_DIR%\github_config.cfg"
echo timeout=10 >> "%CONFIG_DIR%\github_config.cfg"

echo Creating config/log_config.cfg...
echo # Log Configuration File > "%CONFIG_DIR%\log_config.cfg"
echo log_file=meduza_log.txt >> "%CONFIG_DIR%\log_config.cfg"
echo log_level=INFO >> "%CONFIG_DIR%\log_config.cfg"
echo log_format=%(asctime)s - %(levelname)s - %(message)s >> "%CONFIG_DIR%\log_config.cfg"

echo Creating config/user_config.cfg...
echo # User Preferences > "%CONFIG_DIR%\user_config.cfg"
echo search_interval=10 >> "%CONFIG_DIR%\user_config.cfg"
echo email_provider=github >> "%CONFIG_DIR%\user_config.cfg"

echo Creating config/terminal_config.cfg...
echo # Terminal Configuration File > "%CONFIG_DIR%\terminal_config.cfg"
echo title=Meduza Terminal >> "%CONFIG_DIR%\terminal_config.cfg"
echo color_scheme=yellow >> "%CONFIG_DIR%\terminal_config.cfg"

echo Creating config/advanced_config.cfg...
echo # Advanced Configuration File > "%CONFIG_DIR%\advanced_config.cfg"
echo enable_advanced_logging=true >> "%CONFIG_DIR%\advanced_config.cfg"
echo enable_retries=true >> "%CONFIG_DIR%\advanced_config.cfg"
echo retry_delay=5 >> "%CONFIG_DIR%\advanced_config.cfg"

rem Creating .ini files
echo Creating config/github_config.ini...
echo [GitHub] > "%CONFIG_DIR%\github_config.ini"
echo api_url=https://api.github.com >> "%CONFIG_DIR%\github_config.ini"
echo headers={"Accept": "application/vnd.github+json", "User-Agent": "Meduza-Email-Finder"} >> "%CONFIG_DIR%\github_config.ini"
echo max_retries=3 >> "%CONFIG_DIR%\github_config.ini"
echo timeout=10 >> "%CONFIG_DIR%\github_config.ini"

echo Creating config/log_config.ini...
echo [Log] > "%CONFIG_DIR%\log_config.ini"
echo log_file=meduza_log.txt >> "%CONFIG_DIR%\log_config.ini"
echo log_level=INFO >> "%CONFIG_DIR%\log_config.ini"
echo log_format=%(asctime)s - %(levelname)s - %(message)s >> "%CONFIG_DIR%\log_config.ini"

echo Creating config/user_config.ini...
echo [User Preferences] > "%CONFIG_DIR%\user_config.ini"
echo search_interval=10 >> "%CONFIG_DIR%\user_config.ini"
echo email_provider=github >> "%CONFIG_DIR%\user_config.ini"

echo Creating config/terminal_config.ini...
echo [Terminal] > "%CONFIG_DIR%\terminal_config.ini"
echo title=Meduza Terminal >> "%CONFIG_DIR%\terminal_config.ini"
echo color_scheme=yellow >> "%CONFIG_DIR%\terminal_config.ini"

echo Creating config/advanced_config.ini...
echo [Advanced Configuration] > "%CONFIG_DIR%\advanced_config.ini"
echo enable_advanced_logging=true >> "%CONFIG_DIR%\advanced_config.ini"
echo enable_retries=true >> "%CONFIG_DIR%\advanced_config.ini"
echo retry_delay=5 >> "%CONFIG_DIR%\advanced_config.ini"

echo All configuration files created successfully.

echo Running the Python script...
python "%SCRIPT_FILE%"

echo Deactivating virtual environment...
deactivate

echo Cleanup...
if exist "%VENV_DIR%" (
    echo Removing the virtual environment...
    rmdir /S /Q "%VENV_DIR%"
)

echo Setup complete!
pause>nul

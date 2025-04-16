@echo off
setlocal enabledelayedexpansion

set PROJECT_DIR=%~dp0
set CONFIG_DIR=%PROJECT_DIR%config

echo Reconfiguring the configuration files...


if not exist "%CONFIG_DIR%" (
    mkdir "%CONFIG_DIR%"
    echo Config directory created.
) else (
    echo Config directory already exists.
)


echo Removing old configuration files...
del /f /q "%CONFIG_DIR%\github_config.cfg"
del /f /q "%CONFIG_DIR%\log_config.cfg"
del /f /q "%CONFIG_DIR%\user_config.cfg"
del /f /q "%CONFIG_DIR%\terminal_config.cfg"
del /f /q "%CONFIG_DIR%\advanced_config.cfg"
del /f /q "%CONFIG_DIR%\github_config.ini"
del /f /q "%CONFIG_DIR%\log_config.ini"
del /f /q "%CONFIG_DIR%\user_config.ini"
del /f /q "%CONFIG_DIR%\terminal_config.ini"
del /f /q "%CONFIG_DIR%\advanced_config.ini"


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

echo Reconfiguration complete!

pause>nul

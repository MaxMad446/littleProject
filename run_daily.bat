@echo off
chcp 65001 > nul
echo ========================================
echo    Daily Python Commit Automation
echo ========================================
echo Дата: %date% %time%
echo.

cd /d "C:\Users\Maxim\Desktop\Project\DailyCommit\littleProject"

:: Проверяем Python
where python >nul 2>&1
if %errorlevel% equ 0 (
    echo Используется: python
    python daily.py
) else (
    where python3 >nul 2>&1
    if %errorlevel% equ 0 (
        echo Используется: python3
        python3 daily.py
    ) else (
        where py >nul 2>&1
        if %errorlevel% equ 0 (
            echo Используется: py
            py daily.py
        ) else (
            echo ОШИБКА: Python не найден!
            echo Установите Python 3.x с python.org
            pause
            exit 1
        )
    )
)

echo.
echo Завершено. Нажмите любую клавишу...
pause > nul
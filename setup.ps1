# Создайте обновленный setup.ps1
@'
Write-Host "НАСТРОЙКА АВТОМАТИЧЕСКОГО ЕЖЕДНЕВНОГО КОММИТА" -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Cyan
Write-Host "Версия: 2.0" -ForegroundColor Yellow
Write-Host "Дата: $(Get-Date -Format 'yyyy-MM-dd')" -ForegroundColor Yellow

# Проверяем Python
$pythonFound = $false
$pythonCmd = ""

if (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCmd = "python"
    $pythonFound = $true
}
elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
    $pythonCmd = "python3"
    $pythonFound = $true
}
elseif (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCmd = "py"
    $pythonFound = $true
}

if (-not $pythonFound) {
    Write-Host "❌ Python не найден!" -ForegroundColor Red
    Write-Host "Установите Python 3.x с официального сайта" -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Python найден: $pythonCmd" -ForegroundColor Green

# Создаем необходимые папки
$folders = @("daily_python_scripts", "backups", "logs", "temp")
foreach ($folder in $folders) {
    if (-not (Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder -Force | Out-Null
        Write-Host "✅ Папка $folder создана" -ForegroundColor Green
    } else {
        Write-Host "✅ Папка $folder уже существует" -ForegroundColor Green
    }
}

# Создаем файл для ежедневного запуска если нет
if (-not (Test-Path "daily_task.ps1")) {
    $dailyTaskContent = @'
# daily_task.ps1 - скрипт для ежедневного запуска
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
Write-Host "Daily Commit - $timestamp"
Set-Location "C:\\Users\\Maxim\\Desktop\\Project\\DailyCommit\\littleProject"

# Проверяем наличие daily.py
if (Test-Path "daily.py") {
    python daily.py
} else {
    Write-Host "❌ Основной скрипт daily.py не найден!" -ForegroundColor Red
    exit 1
}
'@
    Set-Content -Path "daily_task.ps1" -Value $dailyTaskContent -Encoding UTF8
    Write-Host "✅ Файл daily_task.ps1 создан" -ForegroundColor Green
}

# Создаем bat файл для ручного запуска если нет
if (-not (Test-Path "run_daily.bat")) {
    $batContent = @'
@echo off
chcp 65001 > nul
echo ========================================
echo    Daily Python Commit Automation
echo ========================================
echo Дата: %date% %time%
echo.

cd /d "C:\\Users\\Maxim\\Desktop\\Project\\DailyCommit\\littleProject"

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
'@
    Set-Content -Path "run_daily.bat" -Value $batContent -Encoding ASCII
    Write-Host "✅ Файл run_daily.bat создан" -ForegroundColor Green
}

# Создаем файл управления если нет
if (-not (Test-Path "manager.ps1")) {
    $managerContent = @'
# manager.ps1 - управление автоматическим коммитом

function Show-Menu {
    Clear-Host
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "   Управление Daily Commit System      " -ForegroundColor Yellow
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "1. 🚀 Запустить коммит сейчас" -ForegroundColor Green
    Write-Host "2. ⏰ Показать статус задания" -ForegroundColor Cyan
    Write-Host "3. 📊 Показать логи" -ForegroundColor Magenta
    Write-Host "4. 🔧 Проверить настройки" -ForegroundColor Yellow
    Write-Host "5. ❌ Остановить задание" -ForegroundColor Red
    Write-Host "6. ▶️  Запустить задание" -ForegroundColor Green
    Write-Host "7. 📁 Показать созданные скрипты" -ForegroundColor Blue
    Write-Host "8. 🚪 Выход" -ForegroundColor Gray
    Write-Host "========================================" -ForegroundColor Cyan
}

function Run-Commit {
    Write-Host "Запуск коммита..." -ForegroundColor Yellow
    Set-Location $PSScriptRoot
    if (Test-Path "daily.py") {
        python daily.py
    } else {
        Write-Host "❌ Файл daily.py не найден!" -ForegroundColor Red
    }
    pause
}

function Show-Status {
    Write-Host "Статус задания:" -ForegroundColor Cyan
    try {
        $task = Get-ScheduledTask -TaskName "DailyGitHubCommit" -ErrorAction Stop
        $taskInfo = $task | Get-ScheduledTaskInfo
        Write-Host "✅ Задание существует" -ForegroundColor Green
        Write-Host "   Имя: $($task.TaskName)" -ForegroundColor White
        Write-Host "   Состояние: $($task.State)" -ForegroundColor White
        Write-Host "   Последний запуск: $($taskInfo.LastRunTime)" -ForegroundColor White
        Write-Host "   Следующий запуск: $($taskInfo.NextRunTime)" -ForegroundColor White
    } catch {
        Write-Host "❌ Задание не найдено" -ForegroundColor Red
    }
    pause
}

function Show-Logs {
    $logPath = "logs/daily_commit.log"
    if (Test-Path $logPath) {
        Write-Host "Последние 10 записей лога:" -ForegroundColor Cyan
        Get-Content $logPath -Tail 10
    } else {
        Write-Host "Файл лога не найден: $logPath" -ForegroundColor Yellow
    }
    pause
}

function Check-Settings {
    Write-Host "Проверка настроек:" -ForegroundColor Cyan
    
    # Проверка Python
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Python найден: $pythonVersion" -ForegroundColor Green
    } else {
        Write-Host "❌ Python не найден" -ForegroundColor Red
    }
    
    # Проверка git
    $gitVersion = git --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Git найден: $gitVersion" -ForegroundColor Green
    } else {
        Write-Host "❌ Git не найден" -ForegroundColor Red
    }
    
    # Проверка папки скриптов
    if (Test-Path "daily_python_scripts") {
        $count = (Get-ChildItem "daily_python_scripts\\*.py" -ErrorAction SilentlyContinue).Count
        Write-Host "✅ Папка скриптов: $count файлов" -ForegroundColor Green
    } else {
        Write-Host "❌ Папка скриптов не найдена" -ForegroundColor Red
    }
    
    # Проверка конфигурационного файла
    if (Test-Path "config.json") {
        Write-Host "✅ Конфигурационный файл найден" -ForegroundColor Green
    } else {
        Write-Host "❌ Конфигурационный файл не найден" -ForegroundColor Red
    }
    
    # Проверка файла отслеживания идей
    if (Test-Path "used_ideas.json") {
        Write-Host "✅ Файл отслеживания идей найден" -ForegroundColor Green
    } else {
        Write-Host "❌ Файл отслеживания идей не найден" -ForegroundColor Red
    }
    
    pause
}

function Stop-Task {
    try {
        Stop-ScheduledTask -TaskName "DailyGitHubCommit"
        Write-Host "✅ Задание остановлено" -ForegroundColor Green
    } catch {
        Write-Host "❌ Не удалось остановить задание" -ForegroundColor Red
    }
    pause
}

function Start-Task {
    try {
        Start-ScheduledTask -TaskName "DailyGitHubCommit"
        Write-Host "✅ Задание запущено" -ForegroundColor Green
    } catch {
        Write-Host "❌ Не удалось запустить задание" -ForegroundColor Red
    }
    pause
}

function Show-Scripts {
    if (Test-Path "daily_python_scripts") {
        $scripts = Get-ChildItem "daily_python_scripts\\*.py" | Sort-Object LastWriteTime -Descending
        Write-Host "Последние 10 скриптов:" -ForegroundColor Cyan
        $scripts | Select-Object -First 10 | ForEach-Object {
            $size = $_.Length / 1KB
            Write-Host "  📄 $($_.Name)" -ForegroundColor White
            Write-Host "     📏 Размер: $([Math]::Round($size,2)) KB, Дата: $($_.LastWriteTime)" -ForegroundColor Gray
        }
        Write-Host "\nВсего скриптов: $($scripts.Count)" -ForegroundColor Yellow
    } else {
        Write-Host "Папка скриптов не найдена" -ForegroundColor Red
    }
    pause
}

# Главный цикл
do {
    Show-Menu
    $choice = Read-Host "`nВыберите действие (1-8)"
    
    switch ($choice) {
        '1' { Run-Commit }
        '2' { Show-Status }
        '3' { Show-Logs }
        '4' { Check-Settings }
        '5' { Stop-Task }
        '6' { Start-Task }
        '7' { Show-Scripts }
        '8' { 
            Write-Host "Выход..." -ForegroundColor Gray
            exit 0
        }
        default {
            Write-Host "Неверный выбор" -ForegroundColor Red
            pause
        }
    }
} while ($true)
'@
    Set-Content -Path "manager.ps1" -Value $managerContent -Encoding UTF8
    Write-Host "✅ Файл manager.ps1 создан" -ForegroundColor Green
}

# Тестируем скрипт
Write-Host "`n🧪 Тестируем основной скрипт..." -ForegroundColor Yellow
& $pythonCmd daily_commit.py

# Создаем задание в Планировщике задач
Write-Host "`n🔄 Настройка Планировщика задач..." -ForegroundColor Cyan

$taskName = "DailyGitHubCommit"
$scriptPath = Join-Path $PWD "daily_task.ps1"
$configPath = Join-Path $PWD "config.json"

try {
    # Удаляем старое задание если есть
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false -ErrorAction SilentlyContinue
    
    # Создаем действие
    $action = New-ScheduledTaskAction `
        -Execute "powershell.exe" `
        -Argument "-ExecutionPolicy Bypass -File `"$scriptPath`""
    
    # Проверяем наличие конфигурации
    if (Test-Path $configPath) {
        try {
            $config = Get-Content $configPath | ConvertFrom-Json
            $dailyTime = $config.daily_time
            Write-Host "✅ Конфигурация загружена: время запуска $dailyTime" -ForegroundColor Green
        } catch {
            Write-Host "⚠️ Ошибка чтения конфигурации, используем время по умолчанию 09:00" -ForegroundColor Yellow
            $dailyTime = "09:00"
        }
    } else {
        Write-Host "⚠️ Конфигурационный файл не найден, используем время по умолчанию 09:00" -ForegroundColor Yellow
        $dailyTime = "09:00"
    }
    
    # Создаем триггер (ежедневно в заданное время)
    $trigger = New-ScheduledTaskTrigger `
        -Daily `
        -At $dailyTime
    
    # Настройки
    $settings = New-ScheduledTaskSettingsSet `
        -AllowStartIfOnBatteries `
        -DontStopIfGoingOnBatteries `
        -StartWhenAvailable `
        -Hidden $false
    
    # Принципал
    $principal = New-ScheduledTaskPrincipal `
        -UserId "$env:USERDOMAIN\$env:USERNAME" `
        -LogonType Interactive `
        -RunLevel Highest
    
    # Регистрируем задание
    $task = Register-ScheduledTask `
        -TaskName $taskName `
        -Action $action `
        -Trigger $trigger `
        -Principal $principal `
        -Settings $settings `
        -Description "Ежедневный коммит Python скриптов в GitHub" `
        -Force
    
    # Проверяем успешность создания
    if ($task) {
        Write-Host "✅ Задание успешно создано!" -ForegroundColor Green
    } else {
        Write-Host "❌ Не удалось создать задание" -ForegroundColor Red
    }
    
    Write-Host "✅ Задание создано в Планировщике задач!" -ForegroundColor Green
    Write-Host "   Имя: $taskName" -ForegroundColor Yellow
    Write-Host "   Время: Ежедневно в 10:00" -ForegroundColor Yellow
    Write-Host "   Скрипт: daily_task.ps1" -ForegroundColor Yellow
    
    # Тестовый запуск
    Write-Host "`n🚀 Тестовый запуск задания..." -ForegroundColor Cyan
    try {
        Start-ScheduledTask -TaskName $taskName -ErrorAction Stop
        Start-Sleep -Seconds 3
        $taskInfo = $task | Get-ScheduledTaskInfo
        Write-Host "   Статус: $($task.State)" -ForegroundColor White
        Write-Host "   Последний результат: $($taskInfo.LastTaskResult)" -ForegroundColor White
        
        if ($taskInfo.LastTaskResult -eq 0) {
            Write-Host "✅ Тестовый запуск успешен!" -ForegroundColor Green
        } else {
            Write-Host "❌ Тестовый запуск завершился с ошибкой" -ForegroundColor Red
        }
    } catch {
        Write-Host "❌ Не удалось запустить тестовое выполнение: $_" -ForegroundColor Red
    }

} catch {
    Write-Host "⚠️ Не удалось создать задание автоматически: $_" -ForegroundColor Yellow
    Write-Host "`n📋 Создайте задание вручную:" -ForegroundColor White
    Write-Host "1. Откройте Планировщик заданий (Win+R -> taskschd.msc)" -ForegroundColor White
    Write-Host "2. Создайте задание:" -ForegroundColor White
    Write-Host "   - Имя: DailyGitHubCommit" -ForegroundColor White
    Write-Host "   - Триггер: Ежедневно в 10:00" -ForegroundColor White
    Write-Host "   - Действие: Запустить программу" -ForegroundColor White
    Write-Host "   - Программа: powershell.exe" -ForegroundColor White
    Write-Host "   - Аргументы: -ExecutionPolicy Bypass -File `"$scriptPath`"" -ForegroundColor White
}

# Инструкции
Write-Host "`n📋 ИНСТРУКЦИЯ:" -ForegroundColor Magenta
Write-Host "• Для ручного запуска: двойной клик на run_daily.bat" -ForegroundColor Yellow
Write-Host "• Для управления: запустите manager.ps1" -ForegroundColor Yellow
Write-Host "• Автоматически: ежедневно в 10:00" -ForegroundColor Yellow
Write-Host "`n📁 Файлы проекта:" -ForegroundColor Cyan
Get-ChildItem *.py, *.ps1, *.bat, *.json, .gitignore | Format-Table Name, Length, LastWriteTime -AutoSize

Write-Host "`n✅ Настройка завершена!" -ForegroundColor Green
'@ | Set-Content -Path "setup.ps1" -Encoding UTF8

Write-Host "✅ Файл setup.ps1 обновлен" -ForegroundColor Green
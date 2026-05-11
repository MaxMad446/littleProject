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
        $count = (Get-ChildItem "daily_python_scripts\*.py" -ErrorAction SilentlyContinue).Count
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
        $scripts = Get-ChildItem "daily_python_scripts\*.py" | Sort-Object LastWriteTime -Descending
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
# Создайте обновленный setup.ps1
@'
Write-Host "НАСТРОЙКА АВТОМАТИЧЕСКОГО ЕЖЕДНЕВНОГО КОММИТА" -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Cyan

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
$folders = @("daily_python_scripts", "backups", "logs")
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
Set-Location "C:\Users\Maxim\Desktop\Project\DailyCommit\littleProject"
python daily_commit.py
'@
    Set-Content -Path "daily_task.ps1" -Value $dailyTaskContent -Encoding UTF8
    Write-Host "✅ Файл daily_task.ps1 создан" -ForegroundColor Green
}

# Создаем bat файл для ручного запуска если нет
if (-not (Test-Path "run_daily.bat")) {
    $batContent = @'
@echo off
cd /d "C:\Users\Maxim\Desktop\Project\DailyCommit\littleProject"
python daily_commit.py
pause
'@
    Set-Content -Path "run_daily.bat" -Value $batContent -Encoding ASCII
    Write-Host "✅ Файл run_daily.bat создан" -ForegroundColor Green
}

# Создаем файл управления если нет
if (-not (Test-Path "manager.ps1")) {
    $managerContent = @'
# Простой менеджер
Write-Host "Daily Commit Manager"
Write-Host "1. Run commit now"
Write-Host "2. Show logs"
$choice = Read-Host "Choice"
if ($choice -eq "1") { python daily_commit.py }
if ($choice -eq "2") { Get-Content daily_commit.log -Tail 10 }
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

try {
    # Удаляем старое задание если есть
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false -ErrorAction SilentlyContinue
    
    # Создаем действие
    $action = New-ScheduledTaskAction `
        -Execute "powershell.exe" `
        -Argument "-ExecutionPolicy Bypass -File `"$scriptPath`""
    
    # Создаем триггер (ежедневно в 10:00)
    $trigger = New-ScheduledTaskTrigger `
        -Daily `
        -At "10:00AM"
    
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
    
    Write-Host "✅ Задание создано в Планировщике задач!" -ForegroundColor Green
    Write-Host "   Имя: $taskName" -ForegroundColor Yellow
    Write-Host "   Время: Ежедневно в 10:00" -ForegroundColor Yellow
    Write-Host "   Скрипт: daily_task.ps1" -ForegroundColor Yellow
    
    # Тестовый запуск
    Write-Host "`n🚀 Тестовый запуск задания..." -ForegroundColor Cyan
    Start-ScheduledTask -TaskName $taskName
    Start-Sleep -Seconds 2
    $taskInfo = $task | Get-ScheduledTaskInfo
    Write-Host "   Статус: $($task.State)" -ForegroundColor White
    Write-Host "   Последний результат: $($taskInfo.LastTaskResult)" -ForegroundColor White
    
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
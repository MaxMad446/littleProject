# Настройка автоматического ежедневного коммита для Windows

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonScript = Join-Path $scriptDir "daily_commit.py"
$pythonExe = "python.exe"

# Проверяем наличие Python
if (-not (Get-Command $pythonExe -ErrorAction SilentlyContinue)) {
    Write-Host "Python не найден! Установите Python 3.x" -ForegroundColor Red
    exit 1
}

# Создаем задание в планировщике задач
$action = New-ScheduledTaskAction -Execute $pythonExe -Argument $pythonScript -WorkingDirectory $scriptDir
$trigger = New-ScheduledTaskTrigger -Daily -At "9:00AM"
$principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount -RunLevel Highest
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries

$taskName = "DailyGitHubCommit"

# Проверяем, существует ли уже задание
if (Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue) {
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
}

# Регистрируем новое задание
Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Description "Ежедневный коммит Python кода в GitHub"

Write-Host "Задание создано в планировщике задач Windows!" -ForegroundColor Green
Write-Host "Скрипт будет выполняться каждый день в 9:00 утра" -ForegroundColor Green
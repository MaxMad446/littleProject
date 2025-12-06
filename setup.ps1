# Создаем setup.ps1
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

# Создаем папку для скриптов
New-Item -ItemType Directory -Path "daily_python_scripts" -Force | Out-Null
Write-Host "✅ Папка daily_python_scripts создана" -ForegroundColor Green

# Создаем простой тестовый скрипт
$testScript = @'
print("Тестовый скрипт")
print("Если вы видите этот текст, значит все работает!")
'@

Set-Content -Path "test_script.py" -Value $testScript -Encoding UTF8

# Тестируем Python
Write-Host "`n🧪 Тестируем Python..." -ForegroundColor Yellow
& $pythonCmd --version

# Тестируем скрипт
Write-Host "`n🧪 Тестируем создание скрипта..." -ForegroundColor Yellow
& $pythonCmd daily_commit.py

# Инструкции
Write-Host "`n📋 ИНСТРУКЦИЯ:" -ForegroundColor Magenta
Write-Host "1. Для РУЧНОГО запуска: двойной клик на run.bat" -ForegroundColor Yellow
Write-Host "2. Для ТЕСТА: запустите .\run.bat" -ForegroundColor Yellow
Write-Host "3. Для АВТОМАТИЗАЦИИ:" -ForegroundColor Yellow
Write-Host "   а) Откройте Планировщик заданий (Win+R -> taskschd.msc)" -ForegroundColor White
Write-Host "   б) Создайте задание:" -ForegroundColor White
Write-Host "      - Триггер: Ежедневно в 09:00" -ForegroundColor White
Write-Host "      - Действие: powershell.exe" -ForegroundColor White
Write-Host "      - Аргументы: -ExecutionPolicy Bypass -File `"$PWD\setup.ps1`"" -ForegroundColor White
Write-Host "`n🌐 GitHub репозиторий: https://github.com/MaxMad446/littleProject" -ForegroundColor Cyan

Write-Host "`n✅ Настройка завершена!" -ForegroundColor Green
'@ | Set-Content -Path "setup.ps1" -Encoding UTF8

Write-Host "✅ Файл setup.ps1 создан" -ForegroundColor Green
## Запуск
1. Установить зависимости с помощью pip install -r requirements.txt
2. Запустить main.py

## Ввод
В папке data/raw/test
- solutions.xlsx
- tasks.xlsx
- tests.xlsx 

## Вывод
- data/complete/submission.csv \
Возможны проблемы с индексами

## Защита от инъекций
Тестировалась на небольшом объеме данных, по умолчанию выключена. Чтобы включить, нужно передать аргумент injection_protect=True в generate_submit()

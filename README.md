## Запуск
1. pip install -r requirements.txt
2. main.py

## Ввод
- solutions.xlsx
- tasks.xlsx
- tests.xlsx
В папке data/raw/test

## Вывод
- data/complete/submission.csv
Возможны проблемы с индексами

## Защита от инъекций
Экспериментальная, по умолчанию выключена. Передать параметр в generate_submit() injection_protect=True

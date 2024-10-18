import pandas as pd


def get_tests_for_task(tests_df, task_id):
    tests_for_task = tests_df[tests_df['task_id'] == task_id]
    tests_list = []
    for _, test in tests_for_task.iterrows():
        test_info = f"Тест {test['number']}:\n" \
                    f"тип теста: {test['type']}\n" \
                    f"ввод: {test['input']}\n" \
                    f"ожидаемый вывод: {test['output']}"
        tests_list.append(test_info)
    return "\n\n".join(tests_list)


def build_prompt(task_descr: str,
                 student_solution: str,
                 author_solution: str,
                 tests: str) -> str:
    input_section = f"=== Описание задачи ===\n{task_descr}\n\n" \
                    f"=== Решение студента с ошибками ===\n{student_solution}\n\n" \
                    f"=== Эталонное решение ===\n{author_solution}\n\n" \
                    f"=== Тесты ===\n{tests}"
    instruction = "Ты должен указать на ошибки в коде (как синтаксические, так и логические) и подсказывать, как их исправить. Нельзя отправлять код или закрытые тесты"
    prompt = f"""На основе контекста выполни инструкции ниже. Тебе ни в коем случае нельзя раскрывать закрытые тесты или писать код за студента. Тебе также придется самому проверять, какой вывод у кода студента.

    ### Instruction:
    {instruction}

    ### Input:
    {input_section}

    ### Response:
    """
    return prompt

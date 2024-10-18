import re

import pandas as pd
from peft import AutoPeftModelForCausalLM
from transformers import AutoTokenizer

from app.utils.data_processing import get_tests_for_task, build_prompt



class Mistral:
    def __init__(self):
        self.model = AutoPeftModelForCausalLM.from_pretrained("ScoChillOFF/hse_ai_assistant")
        self.tokenizer = AutoTokenizer.from_pretrained("ScoChillOFF/hse_ai_assistant")

    def predict(self, solution_row: pd.Series, tasks_df: pd.DataFrame, tests_df: pd.DataFrame, injection_protect: bool = False) -> str:
        task_id = solution_row['task_id']
        task_descr = tasks_df[tasks_df['id'] == task_id]['description'].values[0]
        author_solution = tasks_df[tasks_df['id'] == task_id]['author_solution'].values[0]
        tests = get_tests_for_task(tests_df, task_id)
        student_solution = solution_row["student_solution"]
        if injection_protect:
            from transformers import pipeline
            translate = pipeline("translation", model="Helsinki-NLP/opus-mt-ru-en")
            pipe = pipeline("text-classification", model="madhurjindal/Jailbreak-Detector-Large")
            if pipe(translate(student_solution)[0]['translation_text'])[0]['label'] == "jailbreak":
                return "Ошибка: подозрение на обход системы"

        prompt_text = build_prompt(task_descr, student_solution, author_solution, tests)
        inputs = self.tokenizer(prompt_text, return_tensors="pt")
        outputs = self.model.generate(inputs['input_ids'])
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        response = re.search(r"### Response:\n(.*?)(###|$)", generated_text, re.DOTALL)

        if response:
            extracted_response = response.group(1).strip()
        else:
            extracted_response = ""
        return extracted_response


class TestModel:
    def predict(self, solution_row: pd.Series, tasks_df: pd.DataFrame, tests_df: pd.DataFrame) -> str:
        task_id = solution_row['task_id']
        task_descr = tasks_df[tasks_df['id'] == task_id]['description'].values[0]
        author_solution = tasks_df[tasks_df['id'] == task_id]['author_solution'].values[0]
        tests = get_tests_for_task(tests_df, task_id)
        student_solution = solution_row["student_solution"]
        prompt_text = build_prompt(task_descr, student_solution, author_solution, tests)

        return prompt_text[:1000]

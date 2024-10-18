from app.models.mistral import Mistral, TestModel
from app.utils.submit import generate_submit

if __name__ == "__main__":
    model = Mistral()

    generate_submit(
        test_solutions_path="data/raw/test/solutions.xlsx",
        test_tasks_path="data/raw/test/tasks.xlsx",
        test_tests_path="data/raw/test/tests.xlsx",
        predict_func=model.predict,
        save_path="data/complete/submission.csv",
        use_tqdm=True,
        injection_protect=False,
    )

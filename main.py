# Disclaimer: this is not a functional agent and is only for demonstration purposes. This implementation is just a single model call.
from test.tests_processor import run_single_task_tests
import os
import toml
import asyncio
from pathlib import Path

def run(input: dict[str, dict], **kwargs) -> dict[str, str]:

    assert 'model_name' in kwargs, 'model_name is required'
    assert len(input) == 1, 'input must contain only one task'

    print(kwargs)

    env_content = f"AUTOGEN_MODEL_NAME={kwargs['model_name']}"

    env_path = Path(".env")
    env_path.write_text(env_content)

    task_id, task = list(input.items())[0]
    task["task_id"] = task_id
    print(f"Task ID: {task_id}")
    print(f"Task: {task}")

    asyncio.run(run_single_task_tests(None, None, test_results_id="", task_config=task,take_screenshots=True))

    
    results = {}
    results[task_id] = {"trajectory": f"./results/online_mind2web/RUN_ID/{task_id}/result/trajectory", 
                        "result_file": f"./results/online_mind2web/RUN_ID/{task_id}/result/result.json"}
    
        
    return results
"""第 2 课：Future、as_completed() 和异常处理。"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def work(task_id: int) -> str:
    time.sleep((6 - task_id) * 0.1)
    if task_id == 3:
        raise ValueError("任务 3 模拟失败")
    return f"任务 {task_id} 成功"


with ThreadPoolExecutor(max_workers=3) as executor:
    future_to_task = {
        executor.submit(work, task_id): task_id
        for task_id in range(1, 6)
    }

    for future in as_completed(future_to_task):
        task_id = future_to_task[future]
        try:
            print(future.result())
        except Exception as error:
            print(f"任务 {task_id} 失败：{error}")

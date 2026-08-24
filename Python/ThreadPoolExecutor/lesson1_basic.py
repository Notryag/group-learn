"""第 1 课：创建线程池，并比较 submit() 与 map()。"""

from concurrent.futures import ThreadPoolExecutor
import time


def work(task_id: int) -> str:
    print(f"任务 {task_id} 开始")
    time.sleep(1)
    print(f"任务 {task_id} 完成")
    return f"结果-{task_id}"


def use_submit() -> None:
    print("--- submit() ---")
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(work, task_id) for task_id in range(1, 6)]
        results = [future.result() for future in futures]
    print("结果顺序：", results)


def use_map() -> None:
    print("--- map() ---")
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(work, range(1, 6)))
    print("结果顺序：", results)


if __name__ == "__main__":
    use_submit()
    use_map()

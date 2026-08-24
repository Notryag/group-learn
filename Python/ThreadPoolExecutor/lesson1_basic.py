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
    # 先用完整写法理解线程池的生命周期。
    executor = ThreadPoolExecutor(max_workers=3)

    futures = []
    for task_id in range(1, 6):
        future = executor.submit(work, task_id)
        futures.append(future)

    for future in futures:
        result = future.result()
        print(f"获取结果：{result}")

    executor.shutdown(wait=True)


def use_map() -> None:
    print("--- map() ---")
    # 理解基础流程后，使用实际开发中更推荐的 with 写法。
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(work, range(1, 6)))
    print("结果顺序：", results)


if __name__ == "__main__":
    use_submit()
    use_map()

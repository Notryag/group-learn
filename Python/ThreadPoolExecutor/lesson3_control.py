"""第 3 课：超时和取消任务。"""

from concurrent.futures import ThreadPoolExecutor, TimeoutError
import time


def slow_work(name: str, seconds: float) -> str:
    time.sleep(seconds)
    return f"{name} 完成"


with ThreadPoolExecutor(max_workers=1) as executor:
    running = executor.submit(slow_work, "正在运行的任务", 1)
    queued = executor.submit(slow_work, "排队中的任务", 1)

    # 线程已经开始执行的任务通常不能取消，尚未开始的排队任务可以取消。
    print("排队任务取消成功：", queued.cancel())

    try:
        print(running.result(timeout=0.1))
    except TimeoutError:
        print("0.1 秒内还没有完成，任务仍会继续运行")

    print(running.result())

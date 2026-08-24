"""第 4 课：综合练习——批量处理任务并收集成功、失败结果。"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def process(item: int) -> int:
    time.sleep(0.2)
    if item % 4 == 0:
        raise RuntimeError(f"数据 {item} 无法处理")
    return item * item


def main() -> None:
    success: dict[int, int] = {}
    failures: dict[int, str] = {}

    with ThreadPoolExecutor(max_workers=4) as executor:
        future_to_item = {
            executor.submit(process, item): item
            for item in range(1, 11)
        }

        for future in as_completed(future_to_item):
            item = future_to_item[future]
            try:
                success[item] = future.result()
            except Exception as error:
                failures[item] = str(error)

    print("成功：", dict(sorted(success.items())))
    print("失败：", dict(sorted(failures.items())))
    print(f"统计：成功 {len(success)} 个，失败 {len(failures)} 个")


if __name__ == "__main__":
    main()

# Python `ThreadPoolExecutor` 课程

这是一套从零开始的线程池课程。建议按照顺序学习，并且先运行示例，再修改代码观察结果。

## 学习目标

完成课程后，你应该能够：

- 理解线程、线程池和 `Future`
- 使用 `submit()` 和 `map()` 并发执行任务
- 使用 `as_completed()` 及时处理已完成的任务
- 正确处理异常、超时和取消任务
- 为 I/O 密集型任务设置合适的并发数量
- 写出可控、可排错的批量任务代码

## 课程目录

| 课次 | 文件 | 内容 |
| --- | --- | --- |
| 第 1 课 | [`lesson1_basic.py`](lesson1_basic.py) | 创建线程池、`submit()`、`map()` |
| 第 2 课 | [`lesson2_future.py`](lesson2_future.py) | `Future`、异常、`as_completed()` |
| 第 3 课 | [`lesson3_control.py`](lesson3_control.py) | 超时和取消任务 |
| 第 4 课 | [`lesson4_batch.py`](lesson4_batch.py) | 综合练习：批量处理和错误收集 |

## 如何运行

在项目根目录执行：

```bash
python -B Python/ThreadPoolExecutor/lesson1_basic.py
python -B Python/ThreadPoolExecutor/lesson2_future.py
python -B Python/ThreadPoolExecutor/lesson3_control.py
python -B Python/ThreadPoolExecutor/lesson4_batch.py
```

## 先记住这几个对象

```text
ThreadPoolExecutor  -> 线程池，负责管理工作线程
submit()            -> 提交一个任务，返回 Future
Future              -> 任务的“凭证”，可以取结果、查状态、取消任务
map()               -> 批量提交任务，并按输入顺序返回结果
as_completed()      -> 按完成顺序逐个得到 Future
```

## `submit()` 和 `map()` 的区别

| 方法 | 适合场景 | 结果顺序 | 异常处理 |
| --- | --- | --- | --- |
| `submit()` | 每个任务参数不同，想单独控制任务 | 配合 `as_completed()` 可按完成顺序 | 调用 `future.result()` 时抛出 |
| `map()` | 对一批数据执行同一个函数 | 按输入顺序 | 遍历结果时抛出 |

## 重要原则

`ThreadPoolExecutor` 主要适合网络请求、文件读写、数据库访问等 I/O 密集型任务。纯计算任务通常不能仅靠增加线程获得明显提升，因为 Python 有 GIL；这类任务可以进一步学习 `ProcessPoolExecutor`。

## 练习

1. 修改第 1 课，让任务返回任务耗时，并比较单线程与线程池耗时。
2. 修改第 2 课，把失败任务的编号也打印出来。
3. 修改第 3 课，让线程池同时运行 2 个任务，观察 `cancel()` 成功率为什么会变化。
4. 完成第 4 课末尾的练习：统计成功数量、失败数量和所有成功结果。

建议学习顺序：先理解“任务提交”和“结果获取”的区别，再学习异常、超时和取消。不要一开始只记 API，用输出顺序观察并发行为。

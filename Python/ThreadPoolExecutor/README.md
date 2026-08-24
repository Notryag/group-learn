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

## 一、线程池的工作模型

线程池把任务提交和任务执行分开：主线程负责提交任务，线程池中的工作线程负责执行任务。

```text
主线程                         ThreadPoolExecutor
   |                                    |
   | submit(work, data)                |
   +-------------------------------> 任务队列
                                        |
                              工作线程取出任务
                                        |
                              执行 work(data)
                                        |
主线程 <-------- Future.result() ----- 任务结果
```

`max_workers=3` 表示最多同时有 3 个工作线程，不代表一定会创建 3 个线程，也不代表任务只有 3 个。多出来的任务会在队列中等待。

## 二、核心对象

```text
ThreadPoolExecutor  -> 线程池，负责管理工作线程
submit()            -> 提交一个任务，返回 Future
Future              -> 任务的“凭证”，可以取结果、查状态、取消任务
map()               -> 批量提交任务，并按输入顺序返回结果
as_completed()      -> 按完成顺序逐个得到 Future
```

### 1. `ThreadPoolExecutor`

先看最基本的写法。这里暂时不使用 `with`，目的是先看清楚线程池是如何创建、提交任务、获取结果和关闭的：

```python
from concurrent.futures import ThreadPoolExecutor

# 这是在线程中执行的普通函数
def work(number):
    return number * 2

# 1. 创建线程池
executor = ThreadPoolExecutor(max_workers=3)

# 2. 提交任务，得到一个 Future
future = executor.submit(work, 10)

# 3. 等待任务完成并取得返回值
result = future.result()
print(result)  # 20

# 4. 不再使用线程池时关闭它
executor.shutdown(wait=True)
```

上面的代码可以帮助我们理解完整流程：`executor` 管理线程，`submit()` 提交任务，`future` 保存任务状态和结果，`result()` 获取结果，`shutdown()` 关闭线程池。

实际开发中更推荐使用 `with`。它会在代码块结束时等待任务完成并关闭线程池，即使代码块中间发生异常，也能更安全地清理资源：

```python
# 任务函数仍然是普通函数
def work(number):
    return number * 2

# 离开 with 代码块时，线程池会自动关闭
with ThreadPoolExecutor(max_workers=3) as executor:
    future = executor.submit(work, 10)
    result = future.result()
    print(result)  # 20
```

学习顺序可以这样安排：第 1 课先理解上面的四步流程；从第 2 课开始，示例统一使用 `with`，把注意力放在 `Future`、异常和并发结果处理上。

常用方法：

| 方法 | 作用 | 注意事项 |
| --- | --- | --- |
| `submit(fn, *args, **kwargs)` | 提交一个可调用对象，返回 `Future` | 提交时不会立即得到业务结果 |
| `map(fn, *iterables, timeout=None, chunksize=1)` | 对多个输入批量执行函数 | 结果按照输入顺序返回 |
| `shutdown(wait=True, cancel_futures=False)` | 关闭线程池 | `wait=True` 会等待已提交任务完成 |

`submit()` 的第一个参数必须是“可调用对象”，不要提前调用：

```python
executor.submit(work, 10)   # 正确：在线程中执行 work(10)
executor.submit(work(10))   # 错误：work(10) 会先在当前线程执行
```

### 2. `Future`

`Future` 表示一个已经提交、但结果可能尚未准备好的任务。它有三种主要状态：

```text
PENDING（等待执行） -> RUNNING（执行中） -> FINISHED（完成）
                                      \-> CANCELLED（取消）
```

#### Future 的常用方法

| 方法 | 返回值 | 用途 |
| --- | --- | --- |
| `result(timeout=None)` | 任务返回值 | 等待任务完成并取得结果；任务内部异常会在这里重新抛出 |
| `exception(timeout=None)` | 异常对象或 `None` | 查看任务是否以异常结束；同样可能等待任务完成 |
| `done()` | `bool` | 判断任务是否完成或已取消 |
| `running()` | `bool` | 判断任务当前是否正在执行 |
| `cancel()` | `bool` | 尝试取消尚未开始的任务；成功返回 `True` |
| `cancelled()` | `bool` | 判断任务是否被取消 |
| `add_done_callback(fn)` | `None` | 任务结束后自动调用回调函数 |

最常用的结果和异常处理方式：

```python
future = executor.submit(divide, 10, 0)

try:
    result = future.result(timeout=2)
except TimeoutError:
    print("等待结果超时")
except Exception as error:
    print("任务执行失败：", error)
```

`result()` 是阻塞调用：如果任务还没完成，当前线程会等待。`timeout` 只限制等待时间，不会自动停止工作线程；超时后任务仍可能继续运行。

#### 查询 Future 状态

```python
future = executor.submit(work, 10)
print(future.done())       # 可能是 False
print(future.running())    # 可能是 True
print(future.cancelled())  # 通常是 False
print(future.result())     # 等待并取得结果
print(future.done())       # True
```

#### 取消任务

```python
future = executor.submit(work, 10)
if future.cancel():
    print("取消成功")
else:
    print("取消失败：任务可能已经开始执行")
```

`cancel()` 只能取消还在队列中、尚未开始的任务。线程一旦开始执行函数，就不能通过 `Future.cancel()` 强制杀死它。

#### 完成回调

```python
def on_done(future):
    if future.cancelled():
        print("任务被取消")
        return
    try:
        print("任务完成：", future.result())
    except Exception as error:
        print("任务失败：", error)


future = executor.submit(work, 10)
future.add_done_callback(on_done)
```

回调通常由完成任务的工作线程执行，因此回调中不要做很重的工作，也不要假设它一定在主线程运行。

### 3. `as_completed()`

`as_completed(futures)` 接收一组 `Future`，哪个任务先完成就先返回哪个 `Future`：

```python
from concurrent.futures import as_completed

futures = [executor.submit(work, item) for item in items]
for future in as_completed(futures):
    print("收到一个完成结果：", future.result())
```

它适合下载文件、批量请求等场景，可以及时处理已经完成的任务，而不必等待列表中前面的慢任务。

## 三、`submit()` 和 `map()` 的区别

| 方法 | 适合场景 | 结果顺序 | 异常处理 |
| --- | --- | --- | --- |
| `submit()` | 每个任务参数不同，想单独控制任务 | 配合 `as_completed()` 可按完成顺序 | 调用 `future.result()` 时抛出 |
| `map()` | 对一批数据执行同一个函数 | 按输入顺序 | 遍历结果时抛出 |

```python
# map：结果顺序和输入顺序一致
with ThreadPoolExecutor(max_workers=3) as executor:
    for result in executor.map(work, [1, 2, 3]):
        print(result)

# submit + as_completed：结果按照实际完成顺序处理
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(work, item) for item in [1, 2, 3]]
    for future in as_completed(futures):
        print(future.result())
```

## 四、异常、超时和关闭

### 异常不会在 `submit()` 处抛出

工作函数中的异常会保存到 `Future` 中，通常在调用 `result()` 时重新抛出。因此批量任务必须逐个处理异常，避免一个失败任务导致整个程序无法继续：

```python
for future in as_completed(futures):
    try:
        print(future.result())
    except Exception as error:
        print("记录失败任务：", error)
```

### 线程池关闭

```python
executor.shutdown(wait=True)
```

- `wait=True`：等待已经提交的任务完成，默认值
- `wait=False`：调用关闭后立即返回，但 Python 进程通常仍会等待工作线程结束
- Python 3.9+ 支持 `cancel_futures=True`，可以取消队列中尚未开始的任务

优先使用 `with`，除非需要手动控制线程池生命周期。

## 五、并发数量和适用场景

`ThreadPoolExecutor` 主要适合网络请求、文件读写、数据库访问等 I/O 密集型任务。纯计算任务通常不能仅靠增加线程获得明显提升，因为 Python 有 GIL；这类任务可以进一步学习 `ProcessPoolExecutor`。

线程数不是越多越好：

- 太少：并发能力不足，等待 I/O 的时间被浪费
- 太多：线程切换、内存占用和外部服务压力增加
- 网络请求：还要服从对方接口的限流规则
- 数据库访问：线程数不能超过连接池和数据库承受能力

## 六、课程练习

1. 修改第 1 课，让任务返回任务耗时，并比较单线程与线程池耗时。
2. 修改第 2 课，把失败任务的编号也打印出来。
3. 修改第 3 课，让线程池同时运行 2 个任务，观察 `cancel()` 成功率为什么会变化。
4. 完成第 4 课末尾的练习：统计成功数量、失败数量和所有成功结果。

建议学习顺序：先理解“任务提交”和“结果获取”的区别，再学习异常、超时和取消。不要一开始只记 API，用输出顺序观察并发行为。

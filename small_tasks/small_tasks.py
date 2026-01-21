from collections import deque
from typing import Iterable, Tuple, TypeVar

T = TypeVar("T")

items = [1, 2, 3, 4, 5, 5, 6, 7]

def sliding_window_deque(items: list[T], window_size: int = 1) -> Iterable[Tuple[T, ...]]:
    if window_size < 1:
        raise ValueError("window_size should be > 0")
    if window_size > len(items):
        return
    window = deque(maxlen=window_size)
    window.extend(items[:window_size])
    yield tuple(window)
    if window_size < len(items):
        for item in items[window_size:]:
            window.append(item)
            yield tuple(window)




if __name__ == "__main__":
    sliding_window_deque(items, 3)
    for window in sliding_window_deque(items, 3):
        print(*window)
    small_list = [1, 2]
    # should raise an exception
    try:
        next(sliding_window_deque([], 3))
        assert False, "Expected StopIteration"
    except StopIteration as e:
        pass
    try:
        next(sliding_window_deque(small_list, 3))
        assert False, "Expected StopIteration"
    except StopIteration as e:
        pass
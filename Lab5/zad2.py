import queue

def func(kolejka: queue.Queue, n: int):
    if kolejka.empty():
        return "Kolejka pusta"
    l = []
    for _ in range(n):
        if not kolejka.empty():
            l.append(kolejka.get())
        else:
            break
    return l

q = queue.Queue()
# q.put(1)
# q.put(1)
# q.put(1)
# q.put(1)
print(func(q, 2))

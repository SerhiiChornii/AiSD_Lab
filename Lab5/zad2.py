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
empty_queue = queue.Queue()
q.put(10)
q.put(20)
q.put(30)
q.put(40)

print(func(q, 3))
print(func(empty_queue, 1))
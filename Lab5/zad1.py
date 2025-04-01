import queue

liczby = input("Wpisz 3 liczby: ").split()

q = queue.Queue()

for l in liczby:
    q.put(l)

for i in range(q.qsize()):
    print(q.get())

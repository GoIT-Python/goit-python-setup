from datetime import datetime
import statistics

now = datetime.now()


def for_generator(min, max):
    my_list = []
    for i in range(min, max):
        my_list.append(i)


def comprehensions_generator(min, max):
    [i for i in range(min, max)]


n = 100
for_times = []
comprehension_times = []
d1 = datetime.now().timestamp()
for i in range(0, n):
    start = datetime.now().timestamp()
    for_generator(0, 1000000)
    end = datetime.now().timestamp()
    delta = end - start
    for_times.append(delta)

    start = datetime.now().timestamp()
    comprehensions_generator(0, 1000000)
    end = datetime.now().timestamp()
    delta = end - start
    comprehension_times.append(delta)
d2 = datetime.now().timestamp()

print("for_times:", statistics.mean(for_times))
print("comprehension_times: ", statistics.mean(comprehension_times))
print("total time spent: ", d2 - d1)

import time

bar_width = 40

def ft_progress(list):
    start = time.perf_counter()
    total = len(list)
    for i, l in enumerate(list, start=1):

        ratio = i / total
        filled = int(ratio * bar_width)
        empty = bar_width - filled

        percent = str(int(ratio * 100))
        if empty != 0:
            bar = ("=" * filled) + ">" + (" " * (empty - 1))
        else:
            bar = ("=" * filled) + (" " * empty)

        n_total = str(i) + '/' + str(total)

        elapsed_time = time.perf_counter() - start

        if i == 0:
            eta = '-'
        else:
            rate = elapsed_time / i
            remaining = total - i
            eta = remaining * rate
            
        print(f"\rETA: {eta:.2f}s [{percent:>3}%] [{bar}] {n_total} | elapsed time {elapsed_time:.2f}s", end="")

        if ratio == 1:
            print()
        yield l

for x in ft_progress(range(200)):
    time.sleep(0.025)
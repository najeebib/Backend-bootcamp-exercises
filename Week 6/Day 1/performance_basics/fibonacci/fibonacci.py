import time
import sys
sys.path.append('../')

from plot.plot_data import draw_results

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def memo_fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = memo_fibonacci(n-1, memo) + memo_fibonacci(n-2, memo)
    return memo[n]

def main():
    nums = [x for x in range(2,41)]
    fibonacci_rusults = []
    mem_fibonacci_rusults = []
    with open("regular_fibonacci_time.txt", 'w') as f:
        regular_fib_start = time.perf_counter()
        for number in nums:
            start = time.perf_counter()
            result = fibonacci(number)
            end = time.perf_counter()
            total_time = end - start
            experiment_str = f"fibonacci({number}) = {result}, execution time is {total_time} seconds\n"
            f.write(experiment_str)
            fibonacci_rusults.append(total_time)
        regular_fib_end = time.perf_counter()
        regular_fib_total = regular_fib_end - regular_fib_start
        time_str = f"Regular fibonacci function runtime is {regular_fib_total} seconds"
        f.write(time_str)
        print(time_str)


    with open("momo_fibonacci_time.txt", 'w') as f:
        memo_fib_start = time.perf_counter()
        for number in nums:
            start = time.perf_counter()
            result = memo_fibonacci(number)
            end = time.perf_counter()
            total_time = end - start
            experiment_str = f"fibonacci({number}) = {result}, execution time is {total_time} seconds\n"
            f.write(experiment_str)
            mem_fibonacci_rusults.append(total_time)
        memo_fib_end = time.perf_counter()
        memo_fib_total = memo_fib_end - memo_fib_start
        time_str = f"Memo fibonacci function runtime is {memo_fib_total} seconds"
        f.write(time_str)
        print(time_str)

    draw_results(fibonacci_rusults, mem_fibonacci_rusults)
if __name__ == "__main__":
    main()
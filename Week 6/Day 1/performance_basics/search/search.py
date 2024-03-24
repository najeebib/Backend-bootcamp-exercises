import time
import random
import sys
sys.path.append('../')

from plot.plot_data import draw_results
def search(arr, target):
    for i,num in enumerate(arr):
        if num == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    numbers = [x for x in range(100 + 1)]
    random_number_to_search = [random.randint(0,100) for _ in range(15)]
    search_results = []
    binary_search_results = []
    with open("search_results.txt", 'w') as f:
        search_start = time.perf_counter()
        for num in random_number_to_search:
            start = time.perf_counter()
            index = search(numbers, num)
            end = time.perf_counter()
            total = end - start
            experiment_str = f"Index of {num} is {index}, execution time is {total} seconds\n"
            f.write(experiment_str)
            search_results.append(total)
        search_end = time.perf_counter()
        search_total = search_end - search_start
        time_str = f"search function runtime is  {search_total} seconds"
        f.write(time_str)
        print(time_str)

    with open("binary_search_results.txt", 'w') as f:
        binary_search_start = time.perf_counter()
        for num in random_number_to_search:
            start = time.perf_counter()
            index = binary_search(numbers, num)
            end = time.perf_counter()
            total = end - start
            experiment_str = f"Index of {num} is {index}, execution time is {total} seconds\n"
            f.write(experiment_str)
            binary_search_results.append(total)
        binary_search_end = time.perf_counter()
        binary_search_total = binary_search_end - binary_search_start
        time_str = f"binary search function runtime is  {binary_search_total} seconds"
        f.write(time_str)
        print(time_str)
    draw_results(search_results, binary_search_results)
if __name__ == "__main__":
    main()
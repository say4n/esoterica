#! /usr/bin/env python3

import random

def is_sorted(arr) -> bool:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bogosort(arr) -> list:
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

if __name__ == "__main__":
    arr = [10, 6, 2, 3, 5, 1, 4]
    print(bogosort(arr))

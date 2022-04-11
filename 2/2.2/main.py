import numpy as np

arr = [1, 2, 3, 4]
print(arr)


def repeat(array, times):
    result = np.array([], dtype=int)
    for i in range(times):
        result = np.append(result, array)
    return result


print(repeat(arr, 2))
print(repeat(arr, 3))

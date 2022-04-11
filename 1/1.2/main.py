def compute(n):
    result = 0
    for i in range(n):
        result = 1 / (2 * i + 1)
    return result


if __name__ == '__main__':
    print(compute(3))

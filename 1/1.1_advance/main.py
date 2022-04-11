if __name__ == '__main__':
    numberList: list[int] = []
    n = input('Enter a number: ')

    # check if the input is a number, if not then try again
    while not n.isdigit():
        n = input('Input is not number. Enter a valid number: ')

    n = int(n)
    for i in range(n):
        numberList.append(int(input()))

    # find max number in numberList
    print(max(numberList))

    # find min number in numberList
    print(min(numberList))

    # sum of all numbers in numberList
    print(sum(map(int, numberList)))

    # sort ascending
    sortedList = sorted(numberList)
    print(sortedList)

    # show how many positive and negative numbers in numberList
    positiveCount = 0
    negativeCount = 0
    for number in numberList:
        if int(number) > 0:
            positiveCount = positiveCount + 1
        elif number < 0:
            negativeCount = negativeCount + 1
    print('Positive numbers: ' + str(positiveCount))
    print('Negative numbers: ' + str(negativeCount))

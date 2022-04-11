if __name__ == '__main__':
    numberList = []
    n = input('Enter a number: ')

    # check if the input is a number, if not then try again
    while not n.isdigit():
        n = input('Input is not number. Enter a valid number: ')

    n = int(n)
    for i in range(n):
        numberList.append(input())

    # find max number in numberList
    maxNumber = numberList[0]
    for number in numberList:
        if int(number) > int(maxNumber):
            maxNumber = number
    print(maxNumber)

    # find min number in numberList
    minNumber = numberList[0]
    for number in numberList:
        if int(number) < int(minNumber):
            minNumber = number
    print(minNumber)

    # sum of all numbers in numberList
    totalSum = 0
    for number in numberList:
        totalSum = totalSum + int(number)
    print(totalSum)

    # sort ascending
    numberList.sort()
    print(numberList)

    # show how many positive and negative numbers in numberList
    positiveCount = 0
    negativeCount = 0
    for number in numberList:
        if int(number) > 0:
            positiveCount = positiveCount + 1
        elif int(number) < 0:
            negativeCount = negativeCount + 1
    print('Positive numbers: ' + str(positiveCount))
    print('Negative numbers: ' + str(negativeCount))

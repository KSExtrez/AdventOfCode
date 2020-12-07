from typing import Hashable

# Big O(n*n) works, but too slow
def firstTry(numbers):
    for number in numbers:
        for number2 in numbers:
            if number + number2 == 2020:
                print(number)
                print(number2)
                print(number * number2)
                break
            pass
        pass

# Big O(n), now looks good 😉
def secondTry(numbers):
    dic = {}
    for number in numbers:
        dic[number] = True

        toFind = 2020 - number

        if dic.get(toFind):
            print(number)
            print(toFind)
            print(number * toFind)
            break
        pass


numbers = [
    1721,
    979,
    366,
    299,
    675,
    1456
    ]
firstTry(numbers)
# Big O(n*n) works, but too slow
def expensive(numbers):
    for number in numbers:
        for number2 in numbers:
            if number + number2 == 2020:
                print(number)
                print(number2)
                print(number * number2)
            pass
        pass



numbers = [
    1721,
    979,
    366,
    299,
    675,
    1456
    ]
expensive(numbers)
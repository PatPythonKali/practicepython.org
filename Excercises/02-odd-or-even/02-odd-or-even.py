def odd_even():
    num = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = int(num / num2)

    if result %4 == 0:
        print(f"{result} is a multiple of 4")
    elif result %2 == 0:
        print(f"{result} is EVEN")
    else:
        print(f"{result} is ODD")
odd_even()
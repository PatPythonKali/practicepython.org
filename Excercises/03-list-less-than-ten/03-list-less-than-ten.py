a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def less_than_ten(a):
    b = []
    for num in a:
        if num >= 5:
            b.append(num)
    print(b)
less_than_ten(a)

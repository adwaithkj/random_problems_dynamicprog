# Say that you are a traveller on a 2D grid.
# You begin in the top-left corner and your goal is to travel
# to the bottom-right corner.
# You may only move down or right.
# and by the way cacheing is op

def possibilities(m, n, dict1):
    key1 = str(m)+','+str(n)
    key2 = str(n)+','+str(n)
    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    elif m == 1:
        return 1

    elif n == 1:
        return 1
    elif key1 in dict1:
        return dict1[key1]
    elif key2 in dict1:
        return dict1[key2]

    p = possibilities(m-1, n, dict1)+possibilities(m, n-1, dict1)
    dict1[key1] = p
    dict1[key2] = p

    return p


a = input("Enter the value for the size of the grid with spaces seperating them ")
a = list(a.strip().split(" "))

m = list(map(int, a))[0]
n = list(map(int, a))[1]

dict1 = {}
print(f"m is {m} and n is {n}")

print(possibilities(m, n, dict1))

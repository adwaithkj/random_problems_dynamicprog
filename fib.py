def fib(n, db, data):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    elif n == 2:
        return 1
    elif n in db:
        return data[db.index(n)]

    val = fib(n-1, db, data)+fib(n-2, db, data)
    db.append(n)
    data.append(val)

    return val


def main():
    n = int(input("Type in the number n and you will have the nth fibonacci number "))
    db = []
    data = []
    f = fib(n, db, data)
    print(f"The fibonacci number is {f}")


main()

# could have made it faster doing the last 9 with modulo 10000000000 arithmetic
# But this is well under 1 minute with PyPy
fib = 1
fib2 = 2
index = 1


class myError (Exception):
    pass

LOOP = True
output = open("104.ans", "w")
while LOOP:
    index = index + 1
    try:
        test = fib
        last_digits = str(test % 1000000000)
        flag1 = True
        for y in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if y not in last_digits:
                flag1 = False
        flag2 = True
        if not flag1:
            raise myError()
        first_digits = str(test)[:9]
        for y in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if y not in first_digits:
                flag2 = False
        if flag1 and flag2:
            print("Both", index)
            output.write(str(index))
            output.close()
            LOOP = False
    except myError:
        pass
    fibt = fib
    fib = fib2
    fib2 = fib + fibt

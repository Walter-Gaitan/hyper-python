# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
memory = 0
result = 0
opt = ''


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if v1 == 1 or v2 == 1 and v3 == "*":
        msg += msg_7
    if v1 == 0 or v2 == 0 and v3 == '*' or v3 == '+' or v3 == '-':
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
    print(msg)


def sum(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


while True:
    print(msg_0)
    x, operator, y = input().split()

    if x == 'M':
        x = memory
    elif y == 'M':
        y = memory

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue

    check(x, y, operator)

    if operator == '+':
        result = sum(x, y)
        print(result)
    elif operator == '-':
        result = subtract(x, y)
        print(result)
    elif operator == '*':
        result = multiply(x, y)
        print(result)
    elif operator == '/':
        try:
            result = divide(x, y)
            print(result)
        except ZeroDivisionError:
            print(msg_3)
            continue
    else:
        print(msg_2)
        continue
    # first question
    print(msg_4)
    opt = input()
    if opt == 'y':
        memory = result
    elif opt == 'n':
        memory = 0
    # second question
    print(msg_5)
    opt = input()
    if opt == 'y':
        continue
    elif opt == 'n':
        break


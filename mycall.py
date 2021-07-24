
while True:
    x = float(input("Первое число: "))
    s = input("Действие (+,-,*,/,^): ")
    if s in ('+', '-', '*', '/', '^'):
        y = float(input("Второе число: "))
        if s == '+':
            print(x+y)
        elif s == '-':
            print(x-y)
        elif s == '*':
            print(x*y)
        elif s == '^':
            print(x**y)
        elif s == '/':
            if y == 0:
                print("Делить на ноль НЕЛЬЗЯ!")
            else:
                print(x/y)
    else:
        print("ERROR! Неверный знак операции!")

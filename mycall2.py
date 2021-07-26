
while True:
    try:
        x = float(input("Первое число: "))
    except ValueError:
        print("Введите пожалуйста число!")
        continue
    s = input("Действие (+,-,*,/,^): ")
    if s in ('+', '-', '*', '/', '^'):
        try:
            y = float(input("Второе число: "))
        except ValueError:
            print("Введите пожалуйста число!")
            continue    
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
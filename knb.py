print ("Камень, ножницы, бумага")
while True:
    try:
        player  = int (input("Выберите себе: \nКамень  = 1 \nНожницы = 2 \nБумага  = 3\n"))
        if player  == 1:
            print ("\nИгрок     - Камень!")
        elif player  == 2:
            print ("\nИгрок     - Ножницы!")
        elif player  == 3:
            print ("\nИгрок     - Бумага!")
        else:
            print ("\nНапишите число от 1 до 3!\n")
            continue
    except ValueError:
        print("\nНапишите число от 1 до 3!\n")
        continue
    # Выбор ПК
    import random
    pk = random.randint(1, 3)
    if pk == 1:
        print("Компьютер - Камень!\n") 
    elif pk == 2:
        print("Компьютер - Ножницы!\n")
    elif pk == 3:
        print("Компьютер - Бумага!\n")
    # Определение победителя
    if player==pk:
        print ("Ничья!\n\n Новая игра\n")
    elif player == 1 and pk == 2:
        print ("Вы победили. ПОЗДРАВЛЯЕМ!\n\n Новая игра\n")
    elif player == 2 and pk == 3:
        print ("Вы победили. ПОЗДРАВЛЯЕМ!\n\n Новая игра\n")
    elif player == 3 and pk == 1:
        print ("Вы победили. ПОЗДРАВЛЯЕМ!\n\n Новая игра\n")
    elif player == 2 and pk == 1:
        print ("Вы проиграли.\n\n Новая игра\n")
    elif player == 3 and pk == 2:
        print ("Вы проиграли.\n\n Новая игра\n")
    elif player == 1 and pk == 3:
        print ("Вы проиграли.\n\n Новая игра\n")

        
   

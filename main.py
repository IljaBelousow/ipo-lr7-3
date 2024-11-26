import json 

with open("file.json", 'r', encoding='utf-8') as file: 
    file = json.load(file) 
dizel = True
#Счетчик использований программы
counter = 0 


while True:
    print("""
        1 - Вывести все записи 
        2 - Вывести запись по полю 
        3 - Добавить запись 
        4 - Удалить запись по полю 
        5 - Выйти из программы
        """)


    point = int(input("Введите действие: "))


#Вывод всех записей
    if point == 1:
        for i in file:
            print(f"""
            Код: {i['id']}, 
            Имя: {i['name']},                       
            Фабрика: {i['manufacturer']}, 
            Заправлена: {i['is_petrol']},    
            Объем Бака: {i['tank_volume']} 
            """)
        counter += 1


#Вывод по айди записи
    elif point == 2:
        idnum = int(input("Введите номер машины: "))
        qwe = False  
        index = 0  
        for i in file:
            if idnum == i['id']:
                print(f"""
                Код: {i['id']}, 
                Имя: {i['name']},                       
                Фабрика: {i['manufacturer']}, 
                Заправлена: {i['is_petrol']},    
                Объем Бака: {i['tank_volume']}
                Индекс в списке: {index}
                """)
                qwe = True  
                break  
            index += 1
        counter += 1
        if not qwe:
            print("Запись не найдена.")


#Ввод с клавиатуры машины 
    elif point == 3:
        ids = int(input("Введите номер машины: "))
        
        errrror = False
        for i in file:
            if i['id'] == ids:
                errrror = True
                break
        
        if errrror:
            print("Ошибка: машина с таким номером уже существует.")
        else:
            name = input("Введите имя машины: ")  
            manufacturer = input("Введите завод изготовитель: ")  
            is_petrol = input("бензин ? введите да/нет: ") 
            tank_volume = float(input("Введите объем бака машины: "))  

            new_i = {
                'id': ids,
                'name': name,
                'manufacturer': manufacturer,
                'is_petrol': True if is_petrol == 'да' else False, 
                'tank_volume': tank_volume
            }

            file.append(new_i) 
            with open("file.json", 'w', encoding='utf-8') as output_file: 
                json.dump(file, output_file, ensure_ascii=False, indent=2)
            print("Машина успешно добавлена.")
        counter += 1


#Удаление машины
    elif point == 4:
        iddel = int(input("Введите номер машины: "))
        qwe = False  

        for i in file:
            if iddel == i['id']:
                file.remove(i)  
                qwe = True  
                break 

        if not qwe:
            print("Запись не найдена.")
        else:
            with open("file.json", 'w', encoding='utf-8') as output_file:
                json.dump(file, output_file, ensure_ascii=False, indent=2)
            print("Машина успешно удалена.")
        counter += 1


#Выход из программы
    elif point == 5:
        print(f"Программа завершена. ОНА МУЧИЛАСЬ РОВНО{counter} РАЗ !!!!!!!!!")
        break  # Выход из цикла


    else:
        print("Некорректный ввод")

def list():
     name = input('Введите имя: ')
     familienname = input('Введите фамилию: ')
     jahr = int(input('Введите год рождения: '))
     stadt = input('Введите город проживания: ')
     email = input('Введите Е-mail: ')
     phone = input('Номер телефона: ')

     def funkzia(imya, familia, god, gorod, em, fon):
          print(imya, familia, god, gorod, em, fon)

     funkzia(familia=familienname, imya=name, god=jahr, gorod=stadt, em=email, fon=phone)

list()




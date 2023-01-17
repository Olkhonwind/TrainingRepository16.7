price_all = 0
while True:
    try:
        ticket = input("\nКоличество билетов?: ")
        ticket = int(ticket)
        if type(ticket) == int:
            break
    except ValueError:
        print("!!!Введите целое число!!!")

for i in range(ticket):
    i += 1
    while True:
        try:
            person_age = input(f"\nВозраст посетителя №{i}?: ")
            person_age = int(person_age)
            if person_age < 18:
                print("Этот билет бесплатный")
            elif 25 > person_age >= 18:
                price_all += 990
                print("Стоимость билета: 990 руб.")
            else:
                price_all += 1390
                print("Стоимость билета: 1390 руб.")
            if type(person_age) == int:
                break
        except ValueError:
            print("!!!Введите целое число!!!")
if ticket > 3:
    price_all = price_all - ((price_all / 100) * 10)
    print(f"\nВсего к оплате с учетом 10%-ой скидки за покупку более 3 билетов:{price_all} руб.")
else:
    print(f"\nВсего к оплате: {price_all} руб.")
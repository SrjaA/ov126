cakes = {'Наполон': [['масло', 'мука', 'сахар'], 6.5, 2010],
         'Медовик': [['мука', 'сахар', 'honey'], 7.8, 1570],
         'Киевский': [['galushki', 'мука', 'соль'], 15, 340]}


def cake_market(**cake):
    print(f'Здрасцте. Сегодня в наличии:\n {" ".join(map(str, cakes.keys()))} ')

    buy = input('Какое торт Вас интересует: ')
    look = input('Что-то хотели бы уточнить (1-описание, 2- цена, 3-количество)\n'
                 ' или покупаем(Enter)? ')
    for k, v in cake.items():
        if buy == k:
            if look == 'описание' or look == '1':
                print(f'Торт {buy} состоит из ', *v[0])
            elif look == 'цена' or look == '2':
                print(f'Торт {buy} стоит {v[1]} рублей')
            elif look == 'количество' or look == '3':
                print(f'Торта {buy} в наличии {v[2]} грамм')

            while True:
                amount = int(input('Скока вешать?: '))

                if buy == k and amount <= v[2]:
                    bought = amount * v[1] / 100
                    print(f'к оплате {bought}')
                    print(f'Торта {buy} осталось {v[2] - amount} грамм')
                    break
                else:
                    print(f'стока нету. есть тока {buy}: {v[2]} грамм')
            print('Дзякуй, заходзьце')


cake_market(**cakes)

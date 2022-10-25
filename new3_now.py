import razboynik, dice_fight, shop
import os
player_hp = 100
pleyer_name = "вася"
pleyer_money = 500
pleyer_potion = 1

#запустили игру
def game(player_hp, pleyer_name, pleyer_money, pleyer_potion):

    
    print("1 битва с разбойником")
    print("2 игра в кости")
    print("3 лавка алхимика")

    while True:
        answer = input("введите номер дороги и нажмите энтер")
        if answer == "1" or answer == "2" or answer == "3":
            break

    if answer == "1":
        razboynik.fight(player_hp, pleyer_name, pleyer_money, pleyer_potion)
    elif answer == "2":
        dice_fight.dice(player_hp, pleyer_name, pleyer_money, pleyer_potion)
    elif answer == "3":
        shop.shop(player_hp, pleyer_name, pleyer_money, pleyer_potion)

game(player_hp, pleyer_name, pleyer_money, pleyer_potion)
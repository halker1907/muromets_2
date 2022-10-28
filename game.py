import shop2
import player
import os

def start_new_game():
	"""
	создает перса:
		имя
		здоровье
		деньги
		зелья

	"""
	#создаем перса
	print("запустили новую игру")
	player_name = input("как вас зовут")
	if not player_name:
		player_name ="безымянный"
	player_hp = 100
	player_money = 500
	player_potions = 0

	is_game = True
	while is_game:

		player.show_player_stats(player_name,player_hp,player_money,player_potions)

		print("-- ситуация")
		print(f"{player_name} приехал к камню")
		print("вирианты")
		print("1 поехать на битву")
		print("2 поехать играть в кости")
		print("3 поехать в лавку алхимика")
		print("0 ливнуть")


		answer = input("введите номер варианта и нажмите энтер ")
		if answer == "1":
			pass
		elif answer == "2":
			pass
		elif answer == "3":
			shop2.visit_shop(player_name,player_hp,player_money,player_potions)
		elif answer == "0":
			is_game = False

		
start_new_game()
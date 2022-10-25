import os

def shop(player_hp, pleyer_name, pleyer_money, pleyer_potion):
	while True:
		os.sistem("cls")
		print(f"{pleyer_name} приехал в лавку алхимикаю. хилка - 200. у тебя 500 монет")

		print(f"здоровье: {player_hp}")
		print(f"деньги: {pleyer_money}")
		print(f"зелья: {pleyer_potion}")

		print("1 - купить зелье")
		print("2 - уехать к камню")

		
		answer = input("введите номер дороги и нажмите энтер")

		if answer == "1":
			if pleyer_money >= 200:
				pleyer_money -= 200
				pleyer_potion += 1
				print(f"{pleyer_name} купил зелье")
			else:
				print ("у вас нет столько денег")
				input("нажмите энтер для продолжения")
		elif answer == "2":
			print("уехал к камню")
			break

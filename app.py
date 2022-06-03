# coding=utf-8
import os
import time
import random

print('Загрузка...')

time.sleep(random.uniform(0.0001, 3))

os.system('cls')

time.sleep(2)


while True:
	print('''  _____ _                              _____        _        _____            
 / ____| |                            |  __ \      | |      |  __ \           
| (___ | |_ _ __ __ _ _ __   __ _  ___| |  | | __ _| |_ __ _| |__) |___  __ _ 
 \___ \| __| '__/ _` | '_ \ / _` |/ _ \ |  | |/ _` | __/ _` |  _  // _ \/ _` |
 ____) | |_| | | (_| | | | | (_| |  __/ |__| | (_| | || (_| | | \ \  __/ (_| |
|_____/ \__|_|  \__,_|_| |_|\__, |\___|_____/ \__,_|\__\__,_|_|  \_\___|\__,_|
                             __/ |                                            
                            |___/                                             
     _           
    | |          
  __| | ___ _ __ 
 / _` |/ _ \ '__|
| (_| |  __/ |   
 \__,_|\___|_|   
               ''')

	print('Привет! Это StrangeDataReader! Программа в которой можно прочитать или создать файлы в формате .strangedata!')
	
	print('Введите команду | Введите help для списка команд')
	command = input('>>> ')

	if command == 'help':
		os.system('cls')
		print('''Команды:
read - прочитать файл
create - создать файл
quit - выйти''')
		input()
		os.system('cls')
	elif command == 'read':
		os.system('cls')
		print('Укажите ПОЛНЫЙ путь к файлу | Подсказка: для системных файлов (типо readme.strangedata или howdidigettheidea.strangedata) можно прописать: system/{системный файл который нам нужен}')
		while True:
			file_path = input('')

			if file_path == '':
				print('Укажите ПОЛНЫЙ путь к файлу')
			elif file_path == 'system/readme.strangedata':
				os.system('cls')
				file = open('readme.strangedata', 'r').readline()
				print(file)
				input()
				os.system('cls')
				break
			elif file_path == 'system/howdidigettheidea.strangedata':
				os.system('cls')
				file = open('howdidigettheidea.strangedata', 'r').readline()
				print(file)
				input()
				os.system('cls')
				break
			elif file_path == 'system/readme':
				os.system('cls')
				file = open('readme.strangedata', 'r').readline()
				print(file)
				input()
				os.system('cls')
				break
			elif file_path == 'system/howdidigettheidea':
				os.system('cls')
				file = open('howdidigettheidea.strangedata', 'r').readline()
				print(file)
				input()
				os.system('cls')
				break
			else:
				if '.strangedata' not in file_path:
					print('Укажите файл с расширением .strangedata')
				else:
					os.system('cls')
					file = open(file_path, 'r').readline()
					print(file)
					input()
					os.system('cls')
					break
	elif command == 'create':
		os.system('cls')
		print('Введите название файла (без .strangedata)')
		while True:
			file_name = input('')
			if file_name == '':
				for x in range(5):
					num = int(random.uniform(1, 9))
					file_namee = f'noname' + str(num)
				file_name = file_namee + '.strangedata'

				print('Что туда записать?')
				text = input('')
				file = open(file_name, 'a')
				file.write(text)
				file.close()
				print('Готово! Файл сохранён в папке с программой')
				input()
				os.system('cls')
				break
			elif '.' in file_name:
				print('Введите название файла (без .strangedata)')
			else:
				print('Что туда записать?')
				text = input('')
				file = open(file_name + '.strangedata', 'a')
				file.write(text)
				file.close()
				print('Готово! Файл сохранён в папке с программой')
				input()
				os.system('cls')
				break
	elif command == 'quit':
		input('Press ENTER for exit')
		quit()
	else:
		os.system('cls')
		print('Команда не найдена!')



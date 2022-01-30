import hashlib
import os
from colorama import Fore

#Colores
rojo = Fore.RED
verde = Fore.GREEN
cyan = Fore.CYAN

print(f"""{rojo}

    ____  ______   __  _____   _____ __  __
   / __ )/ ____/  / / / /   | / ___// / / /
  / __  / /_     / /_/ / /| | \__ \/ /_/ / 
 / /_/ / __/    / __  / ___ |___/ / __  /  
/_____/_/      /_/ /_/_/  |_/____/_/ /_/

{verde}INSTAGRAM:{cyan} https://instagram.com/the.m.v_

{rojo}Herramienta para descifrar un hash por fuerza bruta
{cyan}====================== OPCIONES ======================

[1] MD5
[2] SHA1
[3] SHA224
[4] SHA256
[5] SHA384
[6] SHA512
[7] SHA3_224
[8] SHA3_256
[9] SHA3_384
[10] SHA3_512
""")
def codigo():
	opcion = input("¿Que opcion elijes?: ")
	wordlists = input("Ingrese la ruta del archivo .txt o presione enter para usar el que viene por defecto: ")
	if opcion == "1":
		if wordlists == "":
				hash = input("Ingrese el hash: ")

				resolver = open('wordlists.txt', 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.md5(a.encode('utf-8')).hexdigest()
					if a == hash:
						print(f"{verde}Hash resuelto: "+ x)
		elif os.path.isfile(wordlists) == True:
				hash = input("Ingrese el hash: ")
				resolver = open(wordlists, 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.md5(a.encode('utf-8')).hexdigest()
				if a == hash:
					print(f"{verde}Hash resuelto: "+ x)
				elif a != hash:
					print(f"{rojo}No se pudo descifrar")
		else:
			print("Archivo no encontrado")

	elif opcion == "2":
			if wordlists == "":
				hash = input("Ingrese el hash: ")

				resolver = open('wordlists.txt', 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.sha1(a.encode('utf-8')).hexdigest()
					if a == hash:
						print(f"{verde}Hash resuelto: "+ x)
			elif os.path.isfile(wordlists) == True:
				hash = input("Ingrese el hash: ")

				resolver = open(wordlists, 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.sha1(a.encode('utf-8')).hexdigest()
				if a == hash:
					print(f"{verde}Hash resuelto: "+ x)
				elif a != hash:
					print(f"{rojo}No se pudo descifrar")
			else:
				print("Archivo no encontrado")

	elif opcion == "3":
			if wordlists == "":
				hash = input("Ingrese el hash: ")

				resolver = open('wordlists.txt', 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.sha224(a.encode('utf-8')).hexdigest()
					if a == hash:
						print(f"{verde}Hash resuelto: "+ x)
			elif os.path.isfile(wordlists) == True:
				hash = input("Ingrese el hash: ")

				resolver = open(wordlists, 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.sha224(a.encode('utf-8')).hexdigest()
				if a == hash:
					print(f"{verde}Hash resuelto: "+ x)
				elif a != hash:
					print(f"{rojo}No se pudo descifrar")
			else:
				print("Archivo no encontrado")

	elif opcion == "4":

			if wordlists == "":
				hash = input("Ingrese el hash: ")

				resolver = open('wordlists.txt', 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.sha256(a.encode('utf-8')).hexdigest()
					if a == hash:
						print(f"{verde}Hash resuelto: "+ x)
			elif os.path.isfile(wordlists) == True:
				hash = input("Ingrese el hash: ")

				resolver = open(wordlists, 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.sha256(a.encode('utf-8')).hexdigest()
				if a == hash:
					print(f"{verde}Hash resuelto: "+ x)
				elif a != hash:
					print(f"{rojo}No se pudo descifrar")
			else:
				print("Archivo no encontrado")

	elif opcion == "5":

			if wordlists == "":
				hash = input("Ingrese el hash: ")

				resolver = open('wordlists.txt', 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.sha384(a.encode('utf-8')).hexdigest()
					if a == hash:
						print(f"{verde}Hash resuelto: "+ x)
			elif os.path.isfile(wordlists) == True:
				hash = input("Ingrese el hash: ")

				resolver = open(wordlists, 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.sha384(a.encode('utf-8')).hexdigest()
				if a == hash:
					print(f"{verde}Hash resuelto: "+ x)
				elif a != hash:
					print(f"{rojo}No se pudo descifrar")
			else:
				print("Archivo no encontrado")

	elif opcion == "6":

			if wordlists == "":
				hash = input("Ingrese el hash: ")

				resolver = open('wordlists.txt', 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.sha512(a.encode('utf-8')).hexdigest()
					if a == hash:
						print(f"{verde}Hash resuelto: "+ x)
			elif os.path.isfile(wordlists) == True:
				hash = input("Ingrese el hash: ")

				resolver = open(wordlists, 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.sha512(a.encode('utf-8')).hexdigest()
				if a == hash:
					print(f"{verde}Hash resuelto: "+ x)
				elif a != hash:
					print(f"{rojo}No se pudo descifrar")
			else:
				print("Archivo no encontrado")

	elif opcion == "7":

			if wordlists == "":
				hash = input("Ingrese el hash: ")

				resolver = open('wordlists.txt', 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.sha3_224(a.encode('utf-8')).hexdigest()
					if a == hash:
						print(f"{verde}Hash resuelto: "+ x)
			elif os.path.isfile(wordlists) == True:
				hash = input("Ingrese el hash: ")

				resolver = open(wordlists, 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.sha3_224(a.encode('utf-8')).hexdigest()
				if a == hash:
					print(f"{verde}Hash resuelto: "+ x)
				elif a != hash:
					print(f"{rojo}No se pudo descifrar")
			else:
				print("Archivo no encontrado")

	elif opcion == "8":

			if wordlists == "":
				hash = input("Ingrese el hash: ")

				resolver = open('wordlists.txt', 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.sha3_256(a.encode('utf-8')).hexdigest()
					if a == hash:
						print(f"{verde}Hash resuelto: "+ x)
			elif os.path.isfile(wordlists) == True:
				hash = input("Ingrese el hash: ")

				resolver = open(wordlists, 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.sha3_256(a.encode('utf-8')).hexdigest()
				if a == hash:
					print(f"{verde}Hash resuelto: "+ x)
				elif a != hash:
					print(f"{rojo}No se pudo descifrar")
			else:
				print("Archivo no encontrado")

	elif opcion == "9":


			if wordlists == "":
				hash = input("Ingrese el hash: ")

				resolver = open('wordlists.txt', 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.sha3_384(a.encode('utf-8')).hexdigest()
					if a == hash:
						print(f"{verde}Hash resuelto: "+ x)
			elif os.path.isfile(wordlists) == True:
				hash = input("Ingrese el hash: ")

				resolver = open(wordlists, 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.sha3_384(a.encode('utf-8')).hexdigest()
				if a == hash:
					print(f"{verde}Hash resuelto: "+ x)
				elif a != hash:
					print(f"{rojo}No se pudo descifrar")
			else:
				print("Archivo no encontrado")

	elif opcion == "10": 

			if wordlists == "":
				hash = input("Ingrese el hash: ")

				resolver = open('wordlists.txt', 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.sha3_512(a.encode('utf-8')).hexdigest()
					if a == hash:
						print(f"{verde}Hash resuelto: "+ x)
			elif os.path.isfile(wordlists) == True:
				hash = input("Ingrese el hash: ")

				resolver = open(wordlists, 'r')

				for x in resolver.readlines():
					a = x.strip("\n")
					a = hashlib.sha3_512(a.encode('utf-8')).hexdigest()
				if a == hash:
					print(f"{verde}Hash resuelto: "+ x)
				elif a != hash:
					print(f"{rojo}No se pudo descifrar")
			else:
				print("Archivo no encontrado")
	else:
		print("Esa opcion no existe")
		os.system("clear")
		exit()
if __name__ == '__main__':
	try:
		codigo()
	except KeyboardInterrupt:
		os.system("clear")
		exit()
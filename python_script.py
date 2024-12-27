import datetime
import random

def print_twinkle() :
    print("""Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are""")

def find_divisible(a,b) :
	c = []
	if isinstance(a,int) == False or isinstance(b,int) == False:
		print ("a and b are not integer")
	elif a >= b : 
		print ("a must less than b")
	else :
		for i in range (a,b):
			if (i%5 == 0 and i%7 == 0) :
				c.append(i)
		print (c)


def get_time_now() :
	print(datetime.datetime.now())


def check_unique(a) :
	t = 0
	for i in range(len(a)):
		for j in range (len(a)):
			if i != j :
				if a[i] == a[j]:
					t = t + 1
	if t == 0: 
		print("True")
	else : 
		print("False")
			

def generate_string(a) :
	if len(a) == 1:
		return a 
	st = []
	for i in range(len(a)):
		current = a[i]
		remain = a[:i] + a[i+1:]
		new_chunk = generate_string(remain)
		for j in new_chunk:
			result = current + j 
			st.append(result)
	return st


def play_guessing_game():
	target_number = random.randint(1, 9)
	while True:
		while True:
			try: 
				input_number = input("Nhap 1 so tu 1 den 9 di nao: ")
				input_number = int(input_number)
				if 1 <= input_number <= 9:
					break
			except:
				print("Khong hop le. Hay nhap so khac nha")
		if target_number == input_number:
			print("Well guessed")
			break
		else: 
			print("Doan lai di ban oiiii")

def fib(number):
	if number == 1:
		return 1
	sum = 0
	for i in range (number):
		print("i = "+str(i))
		sum = fib(number-1) + fib(number-2)
		print("sum = "+str(sum))

print(fib(5))
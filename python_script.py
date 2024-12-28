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
	try :
		number = int(number)
		if number == 1:
			return 1
		if number == 2:
			return 1
		else:
			return fib(number-1) + fib(number-2)
	except:
		return ("Ban can input mot so nguyen")


flatten_result = []
def flatten (arr):
	if isinstance(arr, (dict,list,tuple)) == False:
		flatten_result.append(arr)
		print("flatten_result luc nay la: " + str(flatten_result)+"\n")
		return flatten_result
	
	for a in arr:
		print("Type cua " + str(a) + " la: " + str(type(a)))
		new_value = flatten(a)
	return flatten_result

# input_test = [[[[1], [[[2]]], [[[[5,[[[3]]]]]]]]]]
# input_test = [1, 2, [3, [4, 5]]]
input_test = [1, [2, [3, 4], [[5.4]]]]
print(flatten(input_test))
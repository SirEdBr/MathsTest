import random

while 1==1:
	print("")
	print("This is a programme written in python to test your mental maths skills. It was created by SirEdBr, from reading-school-cs-club.")
	print("Press Ctrl and the letter 'C' to stop this programme.")
	print("What type of test do you want? Type 1 for addition, 2 for subtraction, 3 for division, 4 for multiplication and 5 for number bonds.")
	choice = input("")
	#-----------------------------------------------------------------------------------------------------------------------------------------
	if choice == '1':
		print("")
		print("How many questions do you want to answer?: ")
		amount=input("")
		print("")
		print("What is the biggest integer that the first number can be?")
		m = 1
		while m == 1:
			fns = input("")
			try:
				if type(int(fns)) == int:
					m = 2
			except:
				print("That was not an integer! Try again:")
		print("")
		print("What is the biggest number that the second number can be?")
		j = 1
		while j == 1:
			sns = input("")
			try:
				if type(int(sns)) == int:
					j = 2
			except:
				print("That was not an integer! Try again:")
		print("")
		correct=0
		i=0
		try:
			while i < int(amount):
				num1 = random.randint(1,int(fns))
				num2 = random.randint(1,int(sns))
				n = i + 1
				print(str(n) + ". What is " + str(num1) + " plus " + str(num2) + " ?")
				ans=input("   ")
				if ans == str(num1 + num2):
					correct=correct + 1
				i = i + 1
				print("")
			if amount == '0':
				print("You can't just not answer any questions at all, that's cheating!")
			elif correct == int(amount):
				print("You have finished the test.")
				print("Congratulations, you have got all of them right! Heeeeey!")
			else:
				print("You have finished the test.")
				print("Keep practising! You got " + str(correct) + " out of " + str(amount) + 	".")
			print("")
		except:
			print("That's not a number!")
			print("")
	#-----------------------------------------------------------------------------------------------------------------------------------------
	elif choice == '2':
		print("")
		print("How many questions do you want to answer?: ")
		amount=input("")
		print("")
		print("What is the biggest integer that the first number can be?")
		m = 1
		while m == 1:
			fns = input("")
			try:
				if type(int(fns)) == int:
					m = 2
			except:
				print("That was not an integer! Try again:")
		print("")
		print("What is the biggest integer that the second number can be?")
		j = 1
		while j == 1:
			sns = input("")
			try:
				if type(int(sns)) == int:
					j = 2
			except:
				print("That was not an integer! Try again:")
		print("")
		correct=0
		i=0
		try:
			while i < int(amount):
				num1 = random.randint(1,int(fns))
				num2 = random.randint(1,int(sns))
				n = i + 1
				print(str(n) + ". What is " + str(num1) + " subtract " + str(num2) + " ?")
				ans=input("   ")
				if ans == str(num1 - num2):
					correct=correct + 1
				i = i + 1
				print("")
			if amount == '0':
				print("You can't just not answer any questions at all, that's cheating!")
			elif correct == int(amount):
				print("You have finished the test.")
				print("Congratulations, you have got all of them right! Heeeeey!")
			else:
				print("You have finished the test.")
				print("Keep practising! You got " + str(correct) + " out of " + str(amount) + 	".")
			print("")
		except:
			print("That's not a number!")
			print("")

	#-----------------------------------------------------------------------------------------------------------------------------------------
	elif choice == '3':
		print("")
		print("How many questions do you want to answer?: ")
		amount=input("")
		print("")
		correct=0
		i=0
		try:
			while i < int(amount):
				num1 = random.randint(1,12)
				num2 = random.randint(1,12)
				n = i + 1
				num3 = num1 * num2
				print(str(n) + ". What is " + str(num3) + " divided by " + str(num2) + " ?")
				ans=input("   ")
				if ans == str(num1):
               				correct=correct + 1
				i = i + 1
				print("")
			if amount == '0':
				print("You can't just not answer any questions at all, that's cheating!")
			elif correct == int(amount):
				print("You have finished the test.")
				print("Congratulations, you have got all of them right! Heeeeey!")
			else:
				print("You have finished the test.")
				print("Keep practising! You got " + str(correct) + " out of " + str(amount) + 	".")
			print("")
		except:
			print("That's not a number!")
			print("")
	
	#-----------------------------------------------------------------------------------------------------------------------------------------
	elif choice == '4':
		print("")
		print("How many questions do you want to answer?: ")
		amount=input("")
		print("")
		correct=0
		i=0
		try:
			while i < int(amount):
				num1 = random.randint(0,12)
				num2 = random.randint(0,12)
				n = i + 1
				print(str(n) + ". What is " + str(num1) + " times " + str(num2) + " ?")
				ans=input("   ")
				if ans == str(num1 * num2):
					correct=correct + 1
				i = i + 1
				print("")
			if amount == '0':
				print("You can't just not answer any questions at all, that's cheating!")
			elif correct == int(amount):
				print("You have finished the test.")
				print("Congratulations, you have got all of them right! Heeeeey!")
			else:
				print("You have finished the test.")
				print("Keep practising! You got " + str(correct) + " out of " + str(amount) + 	".")
			print("")
		except:
			print("That's not a number!")
			print("")
	
	#-----------------------------------------------------------------------------------------------------------------------------------------
	elif choice == '5':
		print("")
		print("How many questions do you want to answer?: ")
		amount=input("")
		print("")
		print("What integer do you want the number bonds to add up to?")
		m = 1
		while m == 1:
			fns = input("")
			try:
				if type(int(fns)) == int:
					m = 2
			except:
				print("That was not an integer! Try again:")
		print("")
		correct=0
		i=0
		try:
			while i < int(amount):
				num1 = random.randint(1,int(fns) - 1)
				n = i + 1
				print(str(n) + ". What do you have to add to " + str(num1) + " to get to " + str(fns) + " ?")
				ans=input("   ")
				if ans == str(int(fns) - num1):
					correct=correct + 1
				i = i + 1
				print("")
			if amount == '0':
				print("You can't just not answer any questions at all, that's cheating!")
			elif correct == int(amount):
				print("You have finished the test.")
				print("Congratulations, you have got all of them right! Heeeeey!")
			else:
				print("You have finished the test.")
				print("Keep practising! You got " + str(correct) + " out of " + str(amount) + ".")

			print("")
		except:
			print("That's not a number!")
			print("")

        #-----------------------------------------------------------------------------------------------------------------------------------------
	else:
		print("That is not a choice!")

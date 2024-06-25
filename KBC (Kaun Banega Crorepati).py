question1 = ["Which planet is closest to the Sun?", "Earth", "Mercury", "Mars", "Jupiter"]
question2 = ["What is the capital city of India?", "Mumbai", "New Delhi", "Kolkata", "Chennai"]
question3 = ["How many sides does a triangle have?", 3, 2, 4, 9]
question4 = ["Which animal is known as the 'king of the jungle'?", "Elephant", "Monkey", "Lion", "Tiger"]
question5 = ["How many days are there in a week?", 3, 6, 7, 14]
question6 = ["Which is the largest planet in our solar system?", "Jupiter", "Saturn", "Uranus", "Neptune"]
question7 = ["What is the opposite of 'hot'?", "Cold", "Warm", "Dry", "Cool"]
question8 = ["Which of these is a primary color?", "Red", "Orange", "Green", "Blue"]
question9 = ["What is the chemical symbol for water?", "H2O", "CO2", "O2", "H2"]
question10 = ["How many seasons are there in a year?", 2, 4, 6, 8]


Price_pool = [10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 10000000]

print("Welcome to Kaun Banega Crorepati")
print("You have to answer 10 questions correctly to win the prize money")
print(f"If you answer a question incorrectly, you will be disqualified and the game will end.\n\n")
print("Here is your first question for Rs. 10,000")
print("a.", question1[0])
print("1.", question1[1],                   "2.", question1[2], 
      "3.", question1[3],                   "4.", question1[4])
answer1 = int(input("Enter your answer (1-4): "))
if(answer1 == 2):
  print("CONGRATULATIONS!!! You won 10,000 rupees.\n")
else:
  print("You lost")
  exit()

print("Here is your second question for Rs. 20,000")
print("b.", question2[0])
print("1.", question2[1],                   "2.", question2[2],
      "3.", question2[3],                   "4.", question2[4])
answer2 = int(input("Enter your answer (1-4): "))
if(answer2 == 2):
  print("CONGRATULATIONS!!! You won 20,000 rupees.\n")
else:
  print("You lost")
  exit()

print("Here is your third question for Rs. 40,000")
print("c.", question3[0])
print("1.", question3[1],                   "2.", question3[2],
      "3.", question3[3],                   "4.", question3[4])
answer3 = int(input("Enter your answer (1-4): "))
if(answer3 == 1):
  print("CONGRATULATIONS!!! You won 40,000 rupees.\n")
else:
  print("You lost")
  exit()

print("Here is your fourth question for Rs. 80,000")
print("d.", question4[0])
print("1.", question4[1],                   "2.", question4[2],
      "3.", question4[3],                   "4.", question4[4])
answer4 = int(input("Enter your answer (1-4): "))
if(answer4 == 3):
  print("CONGRATULATIONS!!! You won 80,000 rupees.\n")
else:
  print("You lost")
  exit()

print("Here is your fifth question for Rs. 1,60,000")
print("e.", question5[0])
print("1.", question5[1],                   "2.", question5[2],
      "3.", question5[3],                   "4.", question5[4])
answer5 = int(input("Enter your answer (1-4): "))
if(answer5 == 3):
  print("CONGRATULATIONS!!! You won 1,60,000 rupees.\n")
else:
  print("You lost")
  exit()

print("Here is your sixth question for Rs. 3,20,000")
print("f.", question6[0])
print("1.", question6[1],                   "2.", question6[2],
      "3.", question6[3],                   "4.", question6[4])
answer6 = int(input("Enter your answer (1-4): "))
if(answer6 == 1):
  print("CONGRATULATIONS!!! You won 3,20,000 rupees.\n")
else:
  print("You lost")
  exit()

print("Here is your seventh question for Rs. 6,40,000")
print("g." ,question7[0])
print("1.", question7[1],                   "2.", question7[2],
      "3.", question7[3],                   "4.", question7[4])
answer7 = int(input("Enter your answer (1-4): "))
if(answer7 == 4):
  print("CONGRATULATIONS!!! You won 6,40,000 rupees.\n")
else:
  print("You lost")
  exit()

print("Here is your eighth question for Rs. 12,50,000")
print("h.", question8[0])
print("1.", question8[1],                   "2.", question8[2],
      "3.", question8[3],                   "4.", question8[4])
answer8 = int(input("Enter your answer (1-4): "))
if(answer8 == 4):
  print("CONGRATULATIONS!!! You won 12,50,000 rupees.\n")
else:
  print("You lost")
  exit()

print("Here is your ninth question for Rs. 25,00,000")
print("i.", question9[0])
print("1.", question9[1],                   "2.", question9[2],
      "3.", question9[3],                   "4.", question9[4])
answer9 = int(input("Enter your answer (1-4): "))
if(answer9 == 1):
  print("CONGRATULATIONS!!! You won 25,00,000 rupees.\n")
else:
  print("You lost")
  exit()

print("Here is your tenth question for Rs. 1,00,00,000")
print("j.", question10[0])
print("1.", question10[1],                   "2.", question10[2],
      "3.", question10[3],                   "4.", question10[4])
answer10 = int(input("Enter your answer (1-4): "))
if(answer10 == 2):
  print("CONGRATULATIONS!!! You won 1,00,00,000 rupees.\n")
else:
  print("You lost")
  exit()

print("THANKS FOR PLAYING WITH US!!!")
print("THIS AMOUNT THAT YOU HAVE WON WIL BE TRANSFERED TO YOUR BANK ACCOUNT IN 24 HOURS!!!")
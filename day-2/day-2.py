#DAY-2


# Data types

#1-String

# print("Hello"[-1])
# print("Hello"[4])

#2-Numbers(Integer)

# print("1234" + "567")
# print(123+456)

#3-Float
# print(3.14159)

#-Boolean
# True
# False



# TYPE CASTING | changing Data type of one type to Another

# print(len(str(1234)))


# print(70 +float("100.5"))

#Day-1 Exercise-2.1 | Data type Exercise



# number = input("Type a two digit number: ")
# addition = int(number[0])+int(number[1])
# print(addition)

# OR

# first_number = int(number[0])
# second_number = int(number[1])

# print(first_number + second_number)



# print(3 *  (3 + 3)/3 -3)

#Day-2 Exercise 2.2

# Measuring BMI

# height = float(input("Enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# # bmi = float(weight)/(float(height) * float(height))

# # OR

# bmi = weight/height ** 2

# print(int(bmi))

 


# print(round(8/3, 2)) 
# print(8 // 3)  #output : 2
# 


# score = 0
# height = 1.8
# isWinning = True

# # f-String
# print("=======================code============================")

# print(f"Your score is {score}, your heigh is {height}, you are winning is {isWinning}")

# Day 2-CHALLENGE

# 1 year = 365 days
# 1 year = 52 wees
# 1 year = 12 months

# If you have to leave util your age of 90, then calculate how many weeks, years, days and months you have left if your current age is input you give.




# age = input("What is your current age? ")

# leftYear = 90 - int(age)

# yearInDays = leftYear * 365;
# yearInMonth = leftYear * 12
# yearInWeeks = leftYear * 52

# print(f"You have {yearInDays} days, {yearInWeeks} weeks, {yearInMonth} months left")

# Day-2 final Projects | TipCalculator


print("Welcome to the tip calculator!.")

totalBills = float(input("What was the total bills? ETB: "))
percentage = float(input("What percentage tip would you like to give? 10, 12, 15? "))

people = float(input("How many people to split the bills? "))

tip = totalBills * (percentage/100)

# print(f"Total tip is: {tip}")

totalBillsWithTip = round(((totalBills + tip)/people),2);


result = print(f"Each person should pay: {(totalBillsWithTip)} ETB")
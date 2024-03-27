# height = input("Enter your height in m: ")
# weight = input("enter your weight in kg: ")

# bmi = int(weight)/(int(height) * int(height))

# print(bmi)


# Day 3 3.4 Exercise Love Calculator

print("Welcome to Love Calculator!")

name1 = input("What is your name? ").lower()
name2 = input("What is thier name? ").lower()

newName = name1+name2;


true = "TRUE".lower()
love = "LOVE".lower()

t = newName.count(true[0])
r = newName.count(true[1])
u = newName.count(true[2])
e = newName.count(true[3])

l = newName.count(love[0])
o = newName.count(love[1])
v = newName.count(love[2])
el = newName.count(love[3])

trueValue = t+r+u+e;

loveValue = l + o +v +el;

love_score = str(trueValue)+str(loveValue)
love_score = int(love_score)

if love_score < 10 or love_score >90:
    print(f"Your score is {love_score} you go together like coke and mentos.")
elif love_score >= 40 and love_score >=50:    
    print(f"Your score is {love_score} you are alright together.")

else:
    print(f"Your score is {love_score}.")




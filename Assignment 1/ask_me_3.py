print("Hello there,please enter your name here:")
name=input()
print("Well hello " + name)

if name == "Jack" or name == "Jackie":
    print("Hello " + name)
    print("Goodbye" + name)
else:
    print("Hello friend")
    print("Enter your age here: ")
    age= int(input())
if age < 18:
    print("Sorry, you are below the age of working ")
elif age>18 and age<25:
    print("You are of age to look for a job")
elif age>= 25 and age <30:
    print("You should be having a job already")
elif age>30 and age<60:
    print("You should think about having a family")
elif age>=60 and age<90:
    print("You should retire")
else:
    print("Goodbye "+ name )
    print("You are " + str(age))
    print("you are alien in nature")

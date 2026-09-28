user_name=input('enter your name! ')
user_age=int(input('enter your age! '))
user_number=int(input('enter your favourite number! '))
if user_number%2==0:
    a='even'
else:
    a='odd'
print(f"Hi {user_name}! In 10 years you'll be {user_age+10}. Your favourite number squared is {user_number**2},and it is {a}.")

#The python understand default input as string that is why it returns string. Python can not do math operations on string that is why we should convert it into integer or float.

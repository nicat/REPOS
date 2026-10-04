#Grading system

sc=int(input("Enter your score: "))
if sc>=90:
    print("A")
elif sc>=75:
    print("B")
elif sc>=50:
    print('c')
else:
    print('F')

#Multiplication Table
a=int(input('Enter number: '))
for i in range(1,11):
    print(f'{i}*{a}={i*a}')

#Password retry System
cr='12345'
s=1
ps=input('Enter password: ')
while ps!=cr and s!=3:
    ps=input('Enter password again: ')
    s+=1
if s!=3:
    print('Correct password')
else:
    print('you have reached password limit')
    


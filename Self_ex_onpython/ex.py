#1
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are!"
      " \n\t\tUp above the world so high,"
      " \n\t\tLike a diamond in the sky."
      " \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

#2
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


#12
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

#14
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)


#21
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

#30

b = int(input("Input the base : "))
h = int(input("Input the height : "))
area = b*h/2
print("area = ", area)


#33
def sum(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum

print(sum(2, 1, 2))
print(sum(3, 2, 2))
print(sum(2, 2, 2))
print(sum(1, 2, 3))

#34

def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum

print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))


#48

n = "246.2458"
print(float(n))
print(int(float(n)))


#50

for i in range(0, 10):
    print('*', end="")
print("\n")


#58
n = int(input("Input a number: "))
sumnum = (n * (n + 1)) / 2
print("Sum of the first",n,"positive integers:",sumnum)


#59
print("Input your height: ")
height_ft = int(input("Feet: "))
height_inch = int(input("Inches: "))
height_inch += height_ft * 12
height_cm = round(height_inch * 2.54, 1)
print("Your height is : %d cm." % height_cm)

#62
days = int(input("Input days: ")) * 3600 * 24
hours = int(input("Input hours: ")) * 3600
minutes = int(input("Input minutes: ")) * 60
seconds = int(input("Input seconds: "))
time = days + hours + minutes + seconds
print("The  amounts of seconds", time)


#89
n=1
if n == 1:
   print("\nFirst day of a Month!")
   print()


#98
import datetime
print(datetime.datetime.now())


#109
num = float(input('Enter a number: '))
print('Positive' if num > 0 else 'Negative' if num == 0 else 'zero')


#144
x = 1
if type(x) == str:
    print("it's string.")
elif type(x) == int:
    print("It's integer.")


#string ex

#1
string="hello world"
print(len(string))


#different page-ex

#1
x=[1,2,3,4,5]
total=sum(x)
print(total)


#3

list1=[3,4,5,6]
print(max(list1))


#4
list1=[3,4,5,6]
print(min(list1))


#5
a = [ "avi" ,"aba" ,"c","heloo","bye",'v','ji','helo']
count = 0
for i in a:
    if len(i) >= 2 :
        count += 1
print(count)

#8
lst = []
if len(lst) == 0:
    print('List is empty')


#9
ls = [10, 22, 44, 23, 4]
newls =ls
print(ls)
print(newls)

#14
a=list(range(0,101))
for i in a:
    if i %2!=0:
        a.remove(i)
        print(a)



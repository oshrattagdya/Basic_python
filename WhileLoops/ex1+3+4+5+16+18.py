#1
num=20
while num>0:
     if (num%2!=0):
        print(num)
     num=num-1
#3
num=int(input("enter Positive integer"))
while num>1:
    if num%2!=0:
        print(num)
    num=num-1

#4
x=int(input("enter Positive integer"))
y=int(input("to see odd number press 1,even number press 2"))
while x>0 :
    if y==1 and x%2==1:
        print (x)
    elif y==2 and x%2==0:
        print(x)
    x = x - 1
else :
    print("error")

#5
guessnumber=int(input("please choose number between 1-1000"))
start=1
end=1000
middle=(start+end)//2

#16
x=int(input("enter number"))
sum=0
count=0
while x!="q":
    sum=sum+(int(x))
    count=count+1
    x=input("enter number")

else:
print(sum//count)

#18
x=int(input("enter number"))
sum=0
big=sum>x
small=sum<x
while x!="done":
    print


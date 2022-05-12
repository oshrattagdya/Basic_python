#6
sum = 0
for i in range(1, 14):
    sum += i
print(sum)
#
# # #7
for i in range(1, 11):
    print(i * 1, i * 2, i * 3, i * 4, i * 5, i * 6, i * 7, i * 8, i * 9, i * 10)
#
#8
num1 = input("enter number")
num2 = input("enter number")
for i in range(5):
    if num1[i] == num2[i]:
        print(num1[i],end= ",")

# 9
num1=input("enter number , 5 numbers")
num2=input("enter number")
for i in range(5):
    if num2[0]==num1[i]:
        print(num1[i])

# 10
sum=0
for i in range (5):
    sum+=int(input("enter number"))
print(sum//5)


# #11
for num in range(1,100):
    for i in range(2,num):
        if (num%i)==0:
            break
    else:
        print(num)


#12
for i in range(1, 11):
    print(i * 1, i * 2, i * 3, i * 4, i * 5, i * 6, i * 7, i * 8, i * 9, i * 10)
    
#13
for i in range (100,5000,4):
    print(i)

#14
for i in range(5,2500):
    if i%6==0:
       print(i)

#15
str=input("oshrat tagadya")
for i in range(0):
    print(str)
#17
x=int(input("enter number"))
y=x-4
for i in range(x):
    for j in range(y):
        print("*",end=" ")
    print()





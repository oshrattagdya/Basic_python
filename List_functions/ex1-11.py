#1
#השאלה מבקשת לכתוב תוכנית הקולטת מס מהמתמש ושולחת פונקציה שמחזירה אם חיובי או שלילי
#תשובה
def even_not_even(x):
    if x%2==0:
        print(0)
    if x%2==1:
        print(1)

num=int(input("enter number"))
even_not_even(num)

#2
#השאלה מבקשת לכתוב תוכנית הקלוטת מס ושולחת פונקציה המחזירה את הממוצע
#תשובה
def count_num(x,y):
    z=x=y/2
    print(z)

num1=int(input("enter number"))
num2=int(input("enter number"))
count_num(num1,num2)

#3
def len_str(x):
    if x==-999:
        print("dont match")
    else:
        print(len(x))
num=int(input("enter number"))
len_str(num)

#4
#כתוב תוכנית המחשבת את חלוקת העודף לפי שטרות של 20,10,5,ושקל
def change_moeny(c):
    x=c//20
    coins=c-(x*20)
    y=coins//10
    coinsof5=c-(x*20+y*10)
    b=(coinsof5//5)
    coinsof1=c-(x*20+y*10+b*5)
    n=coinsof1//1
    return ("notes of 20=",x,"coins of 10=",y,"coins of 5=",b,"coins of 1=",n)

print(change_moeny(76))

#5
#כתבו פונקציה שמחשבת חזקה של 2 מספרים
def strong_num(x,y):
    return(x**y)

#6






#9
num1=50
num2=33
choice=input("a-biggest_divider\nb-smallest_divider\nc-pow\nd-sqrt\nexit")
while choice!="e":

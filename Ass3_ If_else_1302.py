"""
a = int(input("enter a number:"))
if a>0:
    print("positive")

age = int(input("enter a age:"))
if age>=18 :
    print("Eligible to vote")

a = int(input("enter a number:"))
if a%7==0:
    print(a,"is divisible by 7")

a = int(input("enter a number"))
if a>40:
    print("pass")

Temp = int(input("temperature is :"))
if Temp>45:
    print("True")

a = input("enter a string:")
if len(a) >8:
    print("True")

password = input("enter a password:")
if password == "admin123":
    print("Logged In")
    
num = int(input("enter a number:"))
if num%10==0:
    print("multiple of 10")

balance = int(input("enter a balance:"))
minimumlimit = 1000
if balance<1000:
    print("a warning")

num = int(input("enter a number:"))
if num%2==0:
    print("even")
else:
    print("odd")

a = int(input("enter a number:"))
b = int(input("enter b number:"))
if a>b:
    print("largest number")
else:
    print("smallest number")

marks = int(input("enter a mark:"))
if marks>75:
    print("Pass")
else:
    print("Fail")

a = int(input("enter a number:"))
if a>0:
    print("positive")
else:
    print("negative")

ch = input("enter a character:")
if ch in "aeiouAEIOU":
    print("vowel")
else:
    print("consonant")

year = int(input("enter a year:"))
if year%4 == 0:
    print("leap")
else:
    print("not")

pwd = input("enter a password:")
if pwd == "Prashant123":
    print("Valid password")
else:
    print("Invalid password")

salary = int(input("enter a salary:"))
taxable_limit = 50000
if salary>taxable_limit:
    print("taxable")
else:
    print("not")

num = int(input("enter a number:"))
if num>50:
    print("greater than 50")
else:
    print("not greater than 50")

a = int(input("enter a number:"))
b = int(input("enter b number:"))
c = int(input("enter c number:"))

if a>b:
    if a>c:
        print("largest number is:",a)
    else:
        print("largest number is:",c)
else:
    if b>c:
        print("largest number is:",b)
    else:
        print("largest number is:", c)
                    
num = int(input("enter a number:"))
if num>0:
    print("positive")
else:
    if num<0:
        print("negative")
    else:
        print("zero")
        
marks = int(input("enter a marks:"))
if marks>90:
    print("pass")
else:
     if marks>75:
        print("pass")
     else:
          if marks>60:
             print("pass")
          else:
               if marks<60:
                  print("fail")


a = int(input("enter a side:"))
b = int(input("enter a side:"))
c = int(input("enter a side:"))
if a== b==c:
    print("equilateral")
else:
    if a==b or b==c or a==c:
        print("isosceles")
    else:
        print("scalene")

ch = input("enter a character:")
if ch >= "A" and ch <= "z":
    print("uppercase")
else:
    if ch>="a"and ch<="z":
        print("lowercase")
    else:
        if ch>="0 "and ch <="9":
            print("digit")
        else:
            print("special character")
           
unit = int(input("enter a unit:"))
if unit<100:
    bill = unit*5
else:
    if unit<200:
        bill = unit*10
    else:
     if unit<300:
          bill = unit*15
    print(bill)
   
user = input("enter a user:")
psw = input("enter a password:")
if user == "Prashant":
    psw == "admin1"
    print("valid")
else:
    print("invalid")
      
a = 45
b = 30
c = 35
if a>40 and b>25 and c>30:
    print("Pass")
else:
     print("failed")
    
a = 20
b = 40
c = 35
if a>b and a>c:
    print(a)
else:
    if b>a and b>c:
         print(b)
    else:
         print(c)

age = int(input("enter a age:"))
salary = int(input("enter a salary:"))
creditscore = int(input("enter a score:"))
if age>20:
    print("eligible")
else:
    if salary>40000:
            print("eligible")
    else:
        if creditscore> 800:
                print("eligible")
        else:
             print("not eligible")
            
d = int (input("enter day number:"))
if d == 1:
    print("Monday")
elif d == 2:
    print("Tuesday")
elif d == 3:
    print("wednesday")
elif d == 4:
    print("Thursday")
elif d == 5:
    print("Friday")
elif d == 6:
    print("Saturday")
elif d == 6:
    print("Sunday")
else:
    print("invalid day")



m = int(input("enter month number:"))
if m == 1:
    print("January")
elif m == 2:
    print("February")
elif m == 3:
    print("March")
elif m == 4:
    print("April")
else:
    print("invalid month")

    
per = int(input("enter a percentage:"))
if per>90:
    print("A+")
elif per>80:
    print("A")
elif per>70:
    print("B")
else:
    print("failed")
 
exp = int(input("enter exp year:"))
if exp>5:
    print("90% bonus")
elif exp>3:
    print("80% bonus")
else:
    print("no experience")
   
colour = input("enter traffic signal color:")
if colour == "red":
    print("stop")
elif colour=="green":
    print("go")
elif colour=="yellow":
    print("ready")
else:
    print("invalid signal colour")
   

temp = int(input("enter a temp:"))
if temp <5 :
    print("cold")
elif temp <25:
    print("warm")
elif temp<30:
    print("hot")
else:
    print("invalid temp")
    

salary = int(input("enter employee salary:"))
if salary<20000:
    print("low salary")
elif salary<=50000:
    print("middle salary")
elif salary<= 80000:
    print("high salary")
else:
    print("very high salary")

     

amount = int(input("enter a amount:"))
if amount<10000:
    print("discount 10%")
elif amount <20000:
    print("discount 25%")
else:
    print("Not discount")
   

num = int(input("enter a number:"))
if num<10:
    print("single-digit")
elif num<100 and num>10:
    print("double-digit")
else:
    print("multi digit")



perf = int(input("enter performance rating:"))
if perf>90:
    print("excellent")
elif perf>80:
    print("good")
elif perf>70:
    print("average")
elif perf>60:
    print("poor")
else:
    print("bad")
    
num = int(input("enter a number:"))
if num%5==0 and num%11==0:
    print("is divisible ")
else:
    print("is not divisible")
     
age = int(input("enter a age:"))
salary = int(input("enter a salary:"))
creditscore = int(input("enter a score:"))
if age>20 and salary>40000 and creditscore>700:
    print("is eligible")
else:
    print("not eligible")

   
user = input("enter a name:")
pasw = input("enter a password:")
if user=="Prashant" and pasw== "admin123":
    print("valid")
else:
    print("invalid")

          

m = int(input("enter marks sub 1:"))
m = int(input("enter marks sub 2:"))
m = int(input("enter marks sub 3:"))
average = m+m+m/3
if m>40 and average>50:
    print("pass")
else:
    print("failed")

   
num = int(input("enter a number:"))
if num>10 and num<100:
    print("correct")
else:
    print("incorrect")
     

atten = int(input("enter exam attecdance:"))
med = input("enter a medical")
if atten>=75  or med == "yes":
    print("eligible")
   
date = int(input("enter a date:"))
month= int(input("enter a month:"))
year = int(input("enter a year:"))
if date>1 and month<1 or month<12 and year<1:
    print("validate")
else:
    print("invalidate")

   
email = input("enter a email:")
if "@" in email and "." in email:
    print("valid")
else:
    print("invalid")

    

age = int(input("enter a age:"))
health = input("enter health:")
income = int(input("enter a income:"))
if age>20 and health == "good" and income>40000:
    print("eligible for insurance")
else:
    print("not eligible for insurance")
      """

year = int(input("enter a year:"))
if year%4==0 and year%400 == 0 and year%100 == 0:
    print("complete leap year")
else:
    print("not complete leap year")



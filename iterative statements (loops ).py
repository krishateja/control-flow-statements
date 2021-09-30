#assignment-1
num=int(input("enter one number:"))
i=1
while i<=num:
    print(i)
    i=i+1
#assignment-2
n=int(input("enter one number:"))
i=1
while i<=10:
    print(n,"X",i,"=",n*i)
    i=i+1

#assignment-3
numbers = input("enter lower and upper limit:")
a = numbers.split()
print(a)
b = int(a[0])
c = int(a[1])
print(type(b))
while b <= c:
    if b % 5 == 0:
        print(b)
    b = b + 1

#assignment-4
a=input("Enter ten values:")
b=a.split()
i=0
while i<=9:
    if int(b[i])%2==0:
        print(b[i])
    i=i+1

#assignment-5
i=1
count=0
sum=0
while i<=100:
      if i%6==0:
            print(i)
            count=count+1
            sum= sum+i
      i=i+1

print("count:",count)
print("sum:",sum)

#assignment-6
i=1
sum=0
while i<=100:
      if i%9==0:
            print(i)
            sum=sum+i
      i=i+1
print("sum:",sum)

#assignment-7
a=input("enter name and five subjects marks:")
b=a.split()
print(b)
print("student name:",b[0])
i=1
sum= 0
while i<=5:
      print(int(b[i]))
      sum=sum+(int(b[i]))
      i=i+1
print("sum:",sum)
avg=sum/5
print(avg)
print("a" if avg>=90 else "b" if avg<90 and avg>=80 else ("c" if avg<80 and avg>=70 else d))
#assignment-8
i=1
count=0
sum=0
while i<=100:
      if i%2==1 and i%5==0:
            print(i)
            count=count+1
            sum=sum+i
      i=i+1
print("count:",count)
print("sum:",sum)
#class work
num=int(input("enter one number:"))
i=1
c=0
while i<=num:
    if num%i==0 :
        c=c+1
    i=i+1
if c==2:
    print("prime")
else:
    print("not prime")
#nested while
num=int(input("enter one number:"))
i=3
while i<=num:
    j=1
    c=0
    while j<=i:
        if i%j==0 :
            c=c+1
        j=j+1
    if c==2:
        print(i,"prime")
    i=i+1

i=1
while i<=5:
    j=1
    while j<=5:
        print(j,end=" ")
        j=j+1
    print()
    i=i+1
#any table
num=int(input("enter any number:"))
i=1
while i<=10:
    print(num,"X",i,"=", num*i)
    i=i+1
# nested while table
num=int(input("Enter any number"))
i=1
while i<=10:
    j=1
    while j<=num:
        print(j,"X",i,"=",i*j,end="          ")
        j=j+1
    print()
    i=i+1
#assignment factorial
num=int(input("Enter one number:"))
i=1
fact=1
while i<=num:
    fact=fact*i
    i=i+1
print(fact)
#assignment on fibonacci series
num=int(input("enter one number:"))
i=0
j=1
l=0
while l<=num:
    print(i)
    k=i+j
    i=j
    j=k
    l=l+1
#5 students marks:
i=1
while i<=5:
    a=input("student name:")
    b=input("class:")
    j=1
    sum=0
    while j<=5:
        c=int(input("enter sub marks"))
        sum=sum+c
        j=j+1
    print("total:",sum)
    avg=sum/5
    print(avg)
    print("a" if avg >= 90 else "b" if avg < 90 and avg >= 80 else ("c" if avg < 80 and avg >= 70 else "d"))
    i=i+1
#assignment 1
num=int(input("enter one number:"))
i=3
while i<=num:
    j=2
    while j<i:
        if i%j==0:
            break
        j=j+1

    else:
        print(i,"is a prime number")
    i=i+1
# assignment 2
num=int(input("enter number"))
i=1
while i<=num:
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i+1
# assignment 3
num=int(input("enter number"))
i=1
while i<=num:
    j=num
    while j>=i:
         print("*",end=" ")
         j=j-1
    print()
    i=i+1

#assignment 4
num=int(input("enter one number:"))
i=0
while i<num:
    j=num-1-i
    while j>0:
        print(end=" ")
        j=j-1
    k=i+1
    while k>0:
        print("*",end=" ")
        k=k-1
    print()
    i=i+1
#student marks
num=int(input("enter number of students:"))
i=1
while i<=num:
    sname=input("enter a student name:")
    sclass=input("enter student class")
    j=1
    total=0
    while j<=5:
        list=["maths","telugu","hindi","englisg","science"]
        a="enter " +list[j-1] + " marks "
        marks=int(input(a))
        total=total+marks
        j=j+1
    avg=total/5
    grade= "A+" if avg >= 85 else  "A" if avg >= 60 and avg < 85  else "B"
    print("student name:",sname)
    print("student class:",sclass)
    print("total:",total)
    print("avg:",avg)
    print("grade:",grade)
    print("^^^^^^^^^^^^^^^^^^^^^^^")
    i=i+1
#student marks with break statement

while True:
    sname=input("enter a student name:")
    sclass=input("enter student class")
    j=1
    total=0
    while j<=5:
        list=["maths","telugu","hindi","englisg","science"]
        a="enter " +list[j-1] + " marks "
        marks=int(input(a))
        total=total+marks
        j=j+1
    avg=total/5
    grade= "A+" if avg >= 85 else  "A" if avg >= 60 and avg < 85  else "B"
    print("student name:",sname)
    print("student class:",sclass)
    print("total:",total)
    print("avg:",avg)
    print("grade:",grade)
    print("^^^^^^^^^^^^^^^^^^^^^^^")
    b=input("are you going to stop yes/no")
    if b == "no":
        print("thank you for using python code")
        print("data will store in data base")
        break

#for loop
for i in "india":
    print(i)
for i in "12345":
    print(i)

list=["india","uk","usa"]
for i in list:
    print(i)
import time
for i in list:
    print(i)
    for j in i:
        print(j)
        time.sleep(2)

list1=["apple","banana","orange"]
z=iter(list1)#iter link to the variable
print(z)
print(next(z))# next will give the first iteration
print(next(z))# next will give the second iteration
print(next(z))# next will give the third iteration
print(next(z))


u=input("enter one number:")
for i in u:
    print(i)

for i in reversed(u):
    print(i)

u=input("enter one number:")
sum=0
for i in u[ : :-1]:
    print(i)
    sum=sum+int(i)
print(sum)

l1=["teja","raja","chandu","vinod"]
print(l1)
l1.reverse()
print(l1)
for i  in  range(1,10,1):
    print(i)
for j in range(2,50,2):
    print(j)
for k in range(1,10,2):
    print()
#prime in for loop
num=int(input("enter a number"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print(i,"is prime")
else:
    print(i,"is not prime")
# prime series
num=int(input("enter a number"))
for i in range(3,num+1):
    count=0
    for j in range(1,i+1):
        if (i)%j==0:
          count=count+1
    if count==2:
        print(i,"is prime")
    else:
        print(i,"is not prime")
# only one table
num=input("enter one number:")
for i in range(1,11):
    print(int(num),"X",i,"=",int(num)*i)
# series of tables
num=int(input("enter one number:"))
for i in range(1,11):
    for j in range(2,num):
      print(j,"X",i," =", i*j,   end="    ")
    print()

#febinocci series count number
num=input("enter one number:")
a=0
b=1
for i in range(0,int(num)):
    k=a+b
    print(a)
    a=b
    b=k

# febonacci series less than given number
num=int(input("enter one number:"))
a=0
b=1
print(a,b,sep="\n")
for i in range(2,num):
    k=a+b
    if k<10:
      print(k)
    a=b
    b=k
# febonacci series less than the given number and sum of those numbers
num=int(input("enter one number:"))
a=0
b=1
sum=1
print(a,b,sep="\n")
for i in range(2,num):
    k=a+b
    if k<num:
      print(k)
      sum=sum+k
    a=b
    b=k
print(sum)
#factorial numbers
num=int(input("enter one number:"))
fact=1
for i in range(num,0,-1):
    fact=fact*i
print(fact)
# upper and lower limits
a=int(input("enter lower limit:"))
b=int(input("enter upper limit:"))
for i in range(a,b):
    if i%5==0:
        print(i)

a=input("enter lower and upper limits:")
b=a.split()
print(b)
c=int(b[0])
d=int(b[1])
for i in range(c,d):
    if i%5==0:
        print(i)
# even numbers
num=int(input("enter one number:"))
for i in range(1,num+1):
    if i%2==0:
        print(i)
#odd number
num=int(input("enter one number:"))
for i in range(1,num+1):
    if i%2==1:
        print(i)
#using sum and count in for loop
sum=0
count=0
for i in range(1,101):
    if i%6==0:
        print(i)
        sum=sum+i
        count=count+1
print(sum)
print(count)
#using one input taking name and marks
std=input("enter student name and student marks")
a=std.split(" ",1)
print(a)
b=(a[1])
print(b)
c=b.split()
print(c)
print(len(c))
sum=0
for i in range(0,5):
    print(int(c[i]))
    sum=sum+int(c[i])
print("sum:",sum)
avg=sum/len(c)
print("avg",avg)
grade="a"if avg>90 else "b" if avg<89 and avg>70 else c
print("grade",grade)
#odd number and multiple of five
sum=0
count=0
for i in range(1,101):
    if i%2==1 and i%5==0:
        print(i)
        sum=sum+i
        count=count+1
print(sum)
print(count)

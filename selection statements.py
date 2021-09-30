#assignment-1

a=input("Enter student name and their marks:")
c=a.split()
print(c)
d=int(c[1])
e=int(c[2])
f=int(c[3])
print("student name:",c[0])
print("subject-1 marks:",d)
print("subject-2 marks:",e)
print("subject-1 marks:",f)
print(type(d))
total=d+e+f
print(total)
avg=total/3
print(avg)
if avg>=95:
    print("grade:A+")
elif avg<95 and avg>=90:
    print("grade:A")
elif avg<90 and avg>=80:
    print("grade:B")
elif avg<80 and avg>=70:
    print("grade:C")
else:
    print("grade:D")

#assignment 2

des=input("Enter the designstion:")
year=input("Enter years of experiance")
year=int(year)
if des == "PM":
    if year>=5:
        print("hike is 20%")
    elif year<5 and year>=3:
        print("hike is 17%")
    elif year<3 and year>=2:
        print("hike is 10%")
    elif year<2 and year>=1:
        print("hike is 5%")
    else:
        print("you have to spend  ONE more YEAR with us")
elif des=="tm":
    if year>=5:
        print("hike is 18%")
    elif year<5 and year>=3:
        print("hike is 15%")
    elif year<3 and year>=2:
        print("hike is 8%")
    elif year<2 and year>=1:
        print("hike is 3%")
    else:
        print("you have to spend more time with us")
elif des=="dm":
    if year>=5:
        print("hike is 17%")
    elif year<5 and year>=3:
        print("hike is 14%")
    elif year<3 and year>=2:
        print("hike is 7%")
    elif year<2 and year>=1:
        print("hike is 2%")
    else:
        print("you have to spend more time with us")
else:
    print("no hike")

a=20
b=10
c=30
d=45
r=a if a>b and a>c and a>d  else b if b>c and b>d else (c if c>d else d)
print(r)
#assignment on nested if
a=input("Enter student name,their marks and attendence :")
c=a.split()
print(c)
d=int(c[1])
e=int(c[2])
f=int(c[3])
print("student name:",c[0])
print("subject-1 marks:",d)
print("subject-2 marks:",e)
print("subject-1 marks:",f)
print("student attendence:",c[4])
atd=int(c[4])
print(type(d))
print(type(atd))
total=d+e+f
print(total)
avg=total/3
print(avg)
if atd>=90:
    print(avg,"      ","increasing is 5%","       ","total avg=",avg+(0.05*avg))
    if avg>=95:
        print("grade=A+")
    elif avg<95 and avg>=90:
        print("grade=A")
    elif avg<90 and avg>=80:
        print("grade=B")
    elif avg<80 and avg>=70:
        print("grade=C")
    elif avg<70 and avg>=60:
        print("grade=D")
    else:
        print("No grade")
elif atd<90 and atd>=80:
    print(avg, "increasing 3%", "total avg=", avg + (0.03 * avg))
    if avg >= 95:
        print("grade=A+")
    elif avg < 95 and avg >= 90:
        print("grade=A")
    elif avg < 90 and avg >= 80:
        print("grade=B")
    elif avg < 80 and avg >= 70:
        print("grade=C")
    elif avg < 70 and avg >= 60:
        print("grade=D")
    else:
        print("No grade")
elif atd<80 and atd>=70:
    print(avg, "increasing 2%", "total avg=", avg + (0.02 * avg))
    if avg >= 95:
        print("grade=A+")
    elif avg < 95 and avg >= 90:
        print("grade=A")
    elif avg < 90 and avg >= 80:
        print("grade=B")
    elif avg < 80 and avg >= 70:
        print("grade=C")
    elif avg < 70 and avg >= 60:
        print("grade=D")
    else:
        print("No grade")
else:
    "improve your attendence"
#assignment on nested if(comprehension programme)
a=input("Enter student name,student marks and attendence :")
c=a.split()
print(c)
d=int(c[1])
e=int(c[2])
f=int(c[3])
print("student name:",c[0])
print("subject-1 marks:",d)
print("subject-2 marks:",e)
print("subject-1 marks:",f)
print("student attendence:",c[4])
atd=int(c[4])
print(type(d))
print(type(atd))
total=d+e+f
print(total)
avg=total/3
print(avg)
if atd>=90:
    print(avg, "increasing 5%", "total avg=", avg + (0.05* avg))
    print("A"if avg>90 else "B" if avg<90 and avg>=80 else ( "C" if avg<80 and avg>=70 else "D"))

elif atd<90 and atd>=80:
    print(avg, "increasing 3%", "total avg=", avg + (0.03 * avg))
    print("A" if avg > 90 else "B" if avg < 90 and avg >= 80 else ("C" if avg < 80 and avg >= 70 else "D"))

elif atd<80 and atd>=70:
    print(avg, "increasing 2%", "total avg=", avg + (0.02* avg))
    print("A" if avg > 90 else "B" if avg < 90 and avg >= 80 else ("C" if avg < 80 and avg >= 70 else "D"))

else:
    print("improve your attendence")










1
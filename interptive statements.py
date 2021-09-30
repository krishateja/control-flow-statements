num=int(input("enter one number;"))
i=2
while i<num:
    if num%i==0:
        print("is not prime")
        break
    i=i+1
else:
    print("prime number")
#break(it will stop the loop upto that number)
for i in range(1,10):
    if i==5:
        break
    print(i)
#continue(it will skip the number and print  remaining all numbers)
for i in range(1,10):
    if i==5:
        continue
    print(i)
#exit(it will terminate the complite program)
for i in "hyderabad":
    if i=="a":
        exit()
    print(i)
#pass(it will ignore the condition and print all numbers)
for i in range(10):
    if i==5:
        pass
    print(i)
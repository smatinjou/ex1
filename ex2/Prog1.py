
x=int(input("enter x number ---> x = "))
y=int(input("enter x number ---> y = "))

z=[]

for i in range(x+1,y):
    if i%2==0:
        z.append(i)
print(z)


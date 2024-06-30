n=int(input("Enter a no:"))
a=0
b=1
while b<n:
 c=a+b
 a=b
 b=c
if b==n or a==n:
 print ("Fibonacci Number")
else:
 print("Not a Fibonacci Number")
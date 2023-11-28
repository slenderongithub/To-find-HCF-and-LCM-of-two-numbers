#WAP to find the HCF and LCM of two numbers

a=int(input("enter any number"))
b=int(input("enter another number"))

if(a>b):
    t=a
    a=b
    b=t
for i in range(1,a+1):
    if(a%i==0) and (b%i==0):
        hcf=i

print("HCF of ",a, "and",b,"is= ",hcf)
print("LCM of ",a, "and",b,"is= ",(a*b)/hcf)


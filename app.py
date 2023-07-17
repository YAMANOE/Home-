#Q1
i=1
while i<=3:
    x=input("enter the name : ")
    i+=1
    y=len(x)
    f=1
    n=0
    while f<=y:
        if x[n]=="l" :
            x=x[0:n]+'*'+x[n+1:]
        elif x[n]=="u":
            x=x[0:n]+'*'+x[n+1:]
        elif x[n]=="u" and "l":
            x=x[0:n]+'*'+x[n+1:]    

        n=n+1
        f=f+1    
    print(x)

# --------------------------------------------
#Q2

z=2
c=1
m=0
while c<=3:
    a=int(input("inter the number : "))
    c+=1
    while m<=a:
        if a%2==0:
            print("even")
            break
        else :
            print ("odd")
            break
    while z<=a:
      if a%z==0:
        print("not prime")
        z+=1
        break
else : 
   print("prime ")
print("llll")
   











    
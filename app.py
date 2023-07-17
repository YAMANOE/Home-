f=1
n=0
i=0
while i<=3:
    x=input("enter the name : ")
    i+=1
    y=len(x)
    while f<=y:
        if x[n]=="l" and "u":
            x=x[0:n]+'*'+x[n+1:]
            n+=1
            f+=1    
        print(x)

    
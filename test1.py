a=input()
b=int(input())
l=[]
c=0
for i in a:
    if i not in l:
        l.append(i)
    if c>=3 and i in l:
        print(i,end="")
    else:
        c+=1
    
        
    
    

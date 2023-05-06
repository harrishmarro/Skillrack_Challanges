import re
tag=re.compile(r'<[^>]+>')
def remove_tag(s):
    k = tag.sub('',s)
    return k
a=int(input())
b=int(input())
l=[]
l2=[]
m=''
r,c=map(int,input().split(','))
ch=input()
for i in range(a):
    l.append(input())
for i in range(b):
    s=input()
    result=remove_tag(s)
    if result=='':
        continue
    else:
        m+=result
m=m.replace(' ','_')
m.strip()
print(m)
stri=''
count=0
for i in range(len(m)):
    if count<c :
        stri+=m[i]
        count+=1
    else:
        l2.append(stri)
        count=1
        stri=''
        stri+=m[i]
for i in range(len(l)):
    l4=[]
    for j in range(len(l[i])):
        l3=[]
        for k in range(len(l2)):
            for z in range(len(l2[k])):
                if l[i][j]==l2[k][z]:
                    l3.append([k+1,z+1])
        '''if ch=='L':
            l4=max(l3)
            print(*l4,sep=",",end=",")
        else:
            l4=min(l3)
            print(*l4,sep=",",end=",")'''
        if ch=='L':
            l4+=max(l3)
        else:
            l4+=min(l3)
    print(*l4,sep=",")
    l4=[]

       
    
                    

            
            

            
    
        
        
        
        




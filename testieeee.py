tB=int(input())
l1=[];n1=[]
l2=[];n2=[]
l3=[];n3=[]
l4=[];n4=[]
l5=[];n5=[]
c1=int(input())
for i in range(c1):
    n,a=map(str,input().split())
    n1.append(n)
    l1.append(int(a))
c2=int(input())
for i in range(c2):
        
    n,a=map(str,input().split())
    n2.append(n)
    l2.append(int(a))
c3=int(input())
for i in range(c3):
    
    n,a=map(str,input().split())
    n3.append(n)
    l3.append(int(a))
c4=int(input())
for i in range(c4):
    
    n,a=map(str,input().split())
    n4.append(n)
    l4.append(int(a))
c5=int(input())
for i in range(c5):
    
    n,a=map(str,input().split())
    n5.append(n)
    l5.append(int(a))
print(l1,l2,l3,l4,l5)
fL=[]
fl2=[]
nl=[]
for i in l1:
    # nl=[]
    for j in l2:
        for k in l3:
            for l in l4:
                for m in l5:
                    if(i+j+k+l+m>tB):
                        continue
                    else:
                        fL.append(i+j+k+l+m)
                        nl.append(n1[l1.index(i)])
                        nl.append(n2[l2.index(j)])
                        nl.append(n3[l3.index(k)])
                        nl.append(n4[l4.index(l)])
                        nl.append(n5[l5.index(m)])
                        fl2.append(nl)
                        nl=[]

a=max(fL)
b=fl2[(fL.index(a))]
for i in b:
    print(i,end=' ')
    

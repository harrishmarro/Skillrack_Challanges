r,c=map(int,input().split())
l=[]
l2=[]
s=0
for i in range(r):
    l.append(list(map(int,input().split())))
for i in range(c):
    l1=[]
    for j in range(r):
        l1.append(l[j][i])
    l2.append(l1)
for i in range(len(l)):
    if l[i]== l[len(l)-1-i]:
        h=1
    else:
        h=0
        break
for j in range(len(l2)):
    if l2[i]==l2[len(l2)-1-i]:
        v=1
    else:
        v=0
        break
if s==1 and h==1:
    print("S")
elif s==1 and h==0:
    print("V")
elif s==0 and h==1:
    print("H")
else:
    print("-1")
    


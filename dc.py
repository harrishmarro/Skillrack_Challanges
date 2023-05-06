def test(l,i,a,c):
    count=c
    if l[i-1]>l[a] or i<=0:
        print(count,end=" ")
    else:
        count+=1
        test(l,i-1,a,count)
    

l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    c=0
    test(l,i,i,c)    

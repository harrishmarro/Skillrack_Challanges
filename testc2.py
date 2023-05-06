'''l,r=map(int,input().split())
l=list(map(int,input().split()))
wt=[(2**i)for i in l]
if r==1:
    print(sum(wt)%((10**9)+7))
else:
    print(max(wt)%((10**9)+7))'''
    
l,r=map(int,input().split())
l=list(map(int,input().split()))
wt=[(2**i)for i in l]
if r==1:
    print(sum(wt)%((10**9)+7))
else:
    print(max(wt)%((10**9)+7))

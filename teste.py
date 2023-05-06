a=int(input())
b=int(input())
h=' o '
rh='(o '
lh=' o)'
ob='/|\ '
rhb='<|\ '
lhb='/|>'
bh='<|>'
rhlh=' |>'
lhrh='<| '
ri='< \ '
ro='/ \ '
li='/ >'
head=h
body=ob
leg=ro
l=[head,body,leg]
for i in range(b):
    s=input()
    if s[0:3]=='say':
        print(s[3:].strip())
    else:
        if s=='left hand to head':
            head=lh
        elif s=='left hand to hip':
            body=lhb
        elif s=='left hand to start':
            body=ob
        elif s=='left leg in':
            leg=li
        elif s=='left leg out':
            leg=ro
        elif s=='right hand to hip':
            body=rhb
        elif s=='right hand to hip' and head==lh:
            body=lhrh
        elif s=='right hand to start':
            body=ob
        elif s=='right hand to head':
            head=rh
            body=rhlh
        elif s=='right leg in':
            leg=ri
        elif s=='right leg out':
            leg=ro
        l=[head,body,leg]
        for i in l:
            print(i)
    

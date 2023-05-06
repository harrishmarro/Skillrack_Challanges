s,n=map(str,input().split())
l=[]
for i in range(len(s)):
    if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i] == 'u':
        l.append(i)
for i in range(int(n)):
    for j in range(len(s)):
        print(s[j],end="")
    print()

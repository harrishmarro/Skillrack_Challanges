a=int(input())
s=''
for i in range(1,a+1):
    s+=str(i)
print('0')
for i in range(a-1):
    print(s[a-i-1:a]+'0'+s[a:a-2-i:-1])
print(s[::]+'0'+s[::-1])


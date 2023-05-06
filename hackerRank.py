def isBalanced(s):
    try:
        l=[]
        if (s[0] in ['}',']',')']) or (s[-1] in ['{','[','(']) :
            return "NO"
        for i in s:
            if i=='(' or i=='[' or i=='{':
                l.append(i)
            elif l==[] and (i==')' or i=='}' or i==']'):
                if ((i==')' and l[-1]=='(') or (i=='}' and l[-1]=='{') or (i==']' and l[-1]=='[')):
                    return "NO"
            elif (i==')' and l[-1]=='(') or (i=='}' and l[-1]=='{') or (i==']' and l[-1]=='['):
                    l.pop()
            else:
                return "NO"
        return "YES"
    except(Exception):
        return "NO"

            

t = int(input().strip())

for t_itr in range(t):
    s = input()
    result = isBalanced(s)
    print(result)
    

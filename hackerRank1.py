

def arrayManipulation(n, queries):
    l=[]
    for i in range(n+1):
        l.append(0)
    for i in range(len(queries)):
        for j in range(queries[i][0],(queries[i][1])+1):
            if l[j]==0:
                l[j]=queries[i][2]
            else:
                l[j]+=queries[i][2]      
    return max(l)

if __name__ == '__main__':
   

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)


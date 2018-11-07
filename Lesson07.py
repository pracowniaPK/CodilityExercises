def brackets(S):
    s = []
    for c in S:
        if c == ')' and (len(s) < 1 or s.pop() != '('):
            return 0
        if c == ']' and (len(s) < 1 or s.pop() != '['):
            return 0
        if c == '}' and (len(s) < 1 or s.pop() != '{'):
            return 0
        if c == '(' or c == '[' or c == '{':
            s.append(c)
    if len(s) == 0:
        return 1
    return 0

def nesting(S):
    sum = 0
    for c in S:
        sum = sum + 1 if c == '(' else sum - 1
        if sum < 0:
            return 0
    return 1 if sum == 0 else 0

def fish(A, B):
    r = []
    l = []
    
    for i in range(len(A)):
        if B[i] == 1:
            r.append(A[i])
        else:
            while True:
                if len(r) == 0:
                    l.append(A[i])
                    break
                f = r.pop()
                if A[i] < f:
                    r.append(f)
                    break
                
    return len(r) + len(l)
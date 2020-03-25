from math import floor

def CountDiv(a, b, k):
    a = a if a % k == 0 else a + (k - (a % k))
    total = floor((b - a)/k) + 1
    return total

def GenomicRangeQuery(S, P, Q):
    lists = {
        "A": [0],
        "C": [0],
        "G": [0],
        "T": [0],
        }
    values = {
        "A": 1,
        "C": 2,
        "G": 3,
        "T": 4,
        }
    
    for s in S:
        for l in lists:
            lists[l].append(lists[l][-1])
        lists[s][-1] += 1
    
    ans = []
    for p, q in zip(P, Q):
        changed = []
        for k in values:
            if lists[k][p] != lists[k][q+1]:
                changed.append(values[k])
        ans.append(min(changed))

    return ans

def MinAvgTwoSlice(A):
    global_min = 10**4
    min_idx = 0
    for i in range(len(A)-1):
        
        if A[i]+A[i+1] < global_min:
            global_min = A[i]+A[i+1]
            min_idx = i
        try:
            if (A[i]+A[i+1]+A[i+2])*2/3 < global_min:
                global_min = (A[i]+A[i+1]+A[i+2])*2/3
                min_idx = i
        except IndexError:
            continue
        
    return min_idx
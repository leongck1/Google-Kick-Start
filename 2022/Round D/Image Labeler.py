# Time Complexity = O(NlogN + M) where NlogN is due to sorting of A and M is due to the for loop of M - 1.

def median(data):
    if len(data) % 2 == 0:
        index_1 = int((len(data) - 1) // 2)
        index_2 = index_1 + 1
        median = (data[index_1] + data[index_2]) / 2
    elif len(data) % 2 == 1:
        index = int((len(data) - 1) / 2)
        median = data[index]
    return median

T = int(input())
for i in range(1, T + 1):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A = sorted(A, reverse=True)
    result = 0
    for k in range(M - 1):
        result += A[k]
    result += median(A[M - 1:])
    print(f"Case #{i}: {result}")

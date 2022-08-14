# Time Complexity = O(NlogN + M) where NlogN is due to sorting of A and M is due to the for loop of M - 1.

def median(data: list):
    if len(data) % 2 == 0:  # Check if the length of the list is even)
        index = int((len(data) - 1) // 2)
        median = (data[index] + data[index + 1]) / 2
    else:  # If the length of the list is odd
        index = int((len(data) - 1) / 2)
        median = data[index]
    return median

T = int(input())
for i in range(1, T + 1):
    N, M = list(map(int, input().split()))
    A = sorted(list(map(int, input().split())), reverse=True)
    result = 0
    for k in range(M - 1):
        result += A[k]
    result += median(A[M - 1:])
    print(f"Case #{i}: {result}")

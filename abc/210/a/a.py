N, A, X, Y = map(int, input().split())

if N <= A:
    ans = N * X
else:
    ans = A * X + (N - A) * Y
    
print(ans)
N, K, A = input().split()

ans = (int(A) + int(K) - 1) % int(N)

if ans == 0:
    ans = int(N)
print(ans)
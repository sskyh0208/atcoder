A, B, C = map(int, input().split())

count = 1
ans = 0
while ans < B:
    ans = C * count
    if ans >= A and ans<= B:
        break
    count += 1
else:
    ans = '-1'

print(ans)
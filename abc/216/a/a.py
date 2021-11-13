X, Y = map(str, input().split('.'))

if 0 <= int(Y) <= 2:
  print(X+'-')
elif 7 <= int(Y) <= 9:
  print(X+'+')
else:
  print(X)
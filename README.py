# first_code
n, k = map(int, input().split())
scores = list(map(int, input().split()))
ith = scores [i- 1]
count = 0
for j in scores:
  if j == ith and scores > 0:
    count += 1
print(count)

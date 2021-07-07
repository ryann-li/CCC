M = int(input())
N = int(input())
K = int(input())
d = []

for i in range(K):
    b = input().split()
    d.append(b[0])

print(d)

count = 0
for i in range(K):
    if d[i] == "R" or "C":
        count += 1

if (count % 2) == 0:
    print("0")
else:
    print("1")







    





















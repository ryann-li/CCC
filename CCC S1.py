n = int(input())
vertical = list(input().split())
horizontal = list(input().split())
v_list = []
h_list = []

for i in range(n+1):
    v = int(vertical[i])
    v_list.append(v)
    
for i in range(n):
    h = int(horizontal[i])
    h_list.append(h)

count = 0
for i in range(n):
    x = (h_list[i])
    y = (v_list[i] + v_list[i+1])
    count += (x*y/2)

print(count)

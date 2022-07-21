ans = []
for num in range(1000, 3001):
    num_str = str(num)
    is_ok = True
    for char in num_str:
        if int(char) % 2:
            is_ok = False
            break
    if is_ok:
        ans.append(str(num))
print(",".join(ans))

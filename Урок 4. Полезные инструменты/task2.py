a = [15, 1, 16, 16, 3, 1, 9, 18, 32, 11, 17]
b = [a[i] for i in range(1, len(a)) if a[i] > a[i-1]]
print(a)
print(b)

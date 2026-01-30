# 1. Count to 5
i = 1
while i <= 5:
    print(i)
    i += 1

# 2. Counting down
i = 3
while i > 0:
    print(i)
    i -= 1

# 3. Loop through a string index
s = "Hi"
i = 0
while i < len(s):
    print(s[i])
    i += 1

# 4. Powers of 2
n = 1
while n < 10:
    print(n)
    n *= 2

# 5. Removing from list
L = [1, 2, 3]
while L:
    print(L.pop())
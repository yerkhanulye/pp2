# 1. Stop list at item
for x in ["a", "b", "c"]:
    if x == "b": break
    print(x)

# 2. Stop range
for i in range(10):
    if i == 4: break

# 3. Finding first even
for n in [1, 3, 4, 5]:
    if n % 2 == 0:
        print(n)
        break

# 4. Character search
for s in "Hello":
    if s == "l": break

# 5. Nested break (inner only)
for i in range(2):
    for j in range(10):
        if j == 1: break
    print(i)
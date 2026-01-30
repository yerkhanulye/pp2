# 1. Skip item in list
for x in [1, 2, 3]:
    if x == 2: continue
    print(x)

# 2. Skip specific letter
for char in "Python":
    if char == "y": continue
    print(char)

# 3. Print only odd
for i in range(5):
    if i % 2 == 0: continue
    print(i)

# 4. Skip first element
for i in range(5):
    if i == 0: continue
    print(i)

# 5. Skip based on list content
for x in ["skip", "show", "skip"]:
    if x == "skip": continue
    print(x)
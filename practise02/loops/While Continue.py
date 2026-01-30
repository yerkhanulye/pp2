# 1. Skip number 3
i = 0
while i < 5:
    i += 1
    if i == 3: continue
    print(i)

# 2. Skip even
i = 0
while i < 6:
    i += 1
    if i % 2 == 0: continue
    print(i)

# 3. Skip positive (printing 0 and negatives)
i = 3
while i > -3:
    i -= 1
    if i > 0: continue
    print(i)

# 4. Skip specific characters
s = "abc"
i = -1
while i < len(s)-1:
    i += 1
    if s[i] == 'b': continue
    print(s[i])

# 5. Redundant check skip
i = 0
while i < 10:
    i += 1
    if i < 8: continue
    print(i) # Prints 8, 9, 10
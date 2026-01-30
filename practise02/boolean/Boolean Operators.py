# 1. 'and' with multiple conditions
print(1 > 0 and 5 < 10 and 2 == 2) # True

# 2. 'or' with variables
a, b = False, True
print(a or b) # True

# 3. 'not' with a comparison
print(not(10 > 5)) # False

# 4. Combining and/or
print((5 > 1 or 2 > 10) and 3 == 3) # True

# 5. Negating a boolean variable
is_logged_in = False
print(not is_logged_in) # True
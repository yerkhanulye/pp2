# 1. Direct boolean assignment
is_ready = True

# 2. bool() with numbers (non-zero is True)
print(bool(100)) # True

# 3. bool() with empty collections (False)
print(bool([])) # False

# 4. bool() with None (False)
print(bool(None)) # False

# 5. Logical result of a function
def check(): return True
print(check()) # True
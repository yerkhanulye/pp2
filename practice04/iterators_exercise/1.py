def squares_up_to(n):
    for i in range(n + 1):
        yield i * i


n = int(input())
for num in squares_up_to(n):
    print(num)
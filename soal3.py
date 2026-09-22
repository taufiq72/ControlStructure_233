n = int(input("Masukkan nilai n untuk deret Fibonacci: "))

a, b = 0, 1
print("Deret Fibonacci:")

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
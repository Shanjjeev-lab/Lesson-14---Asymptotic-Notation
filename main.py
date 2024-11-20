def o1Time(n):
    iteration = 0
    iteration += 1
    print(f"For {n} input size, the iteration is {iteration}")
    return n * (n + 1) / 2

print(o1Time(5))
print(o1Time(100))

def onTime(n):
    iteration = 0
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
        iteration += 1
    print(f"For {n} input size, the iteration is {iteration}")
    return sum

print(onTime(4))
print(onTime(10))

def onSquareTime(n):
    iteration = 0
    for _ in range(1, n + 1):
        for _ in range(1, n + 1):
            print("*", end=" ")
            iteration += 1 
        print()
    print(f"For {n} input size, the iteration is {iteration}")

onSquareTime(5)
onSquareTime(6)
def ordenar(nums):
    nums.sort()
    print(nums)

nums = []

for i in range(0, 4):
    num = int(input(f"Ingrese número {i}: "))
    nums.append(num)

ordenar(nums)

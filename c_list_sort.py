base_list: list[int] = []
for x in range (10,100+1,10):
    base_list.append(x)
print("base_list :")
print(f"{base_list} ", end=" ")

SENTINEL: int = -999
while True:

    num = float(input("Enter num :"))
    if num == SENTINEL:
        break

    base_list.append(num)
base_list.sort()
print(base_list)
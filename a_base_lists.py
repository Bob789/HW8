#solution a
base_list: list[int] = []
for x in range (100):
    base_list.append(x + 1)
print("base_list :")
print(f"{base_list} ", end=" ")

#solution b
print()
print("First element", f"{base_list[0]} ")

#solution c
print("Last element", f"{base_list[-1]} ")

#solution d
print(f"There are {len(base_list)} elements in the list.")

#solution e
print("Element from 3 to 12: ", f"{base_list[2:12]} ")

#solution f
print("From 80 to end list :" ,f"{base_list[79:]} ")

#solution g
print("From start list untill 17 element", f"{base_list[:17]} ")

#solution h
print("Reverse element :", f"{base_list[::-1]} ")

#solution i
print("Even element :", f"{base_list[1:100:2]} ")

#solution j
print("Element divided by 3:", f"{base_list[2:100:3]} ")

#solution k
print("Element divided by 7:", f"{base_list[6:100:7]} ")

#solution l
print("Element divided by 10:", f"{base_list[9:100:10]} ")

#solution m
print("Element divided by 3 from 99-66:", f"{base_list[98:64:-3]} ")

#solution n
middle_index = len(base_list) // 2
base_list.insert(middle_index, 999)
print("Add element 999 :", f"{base_list} ")

#solution o
base_list.pop(-1)
print("Remove element 100 :", f"{base_list} ")


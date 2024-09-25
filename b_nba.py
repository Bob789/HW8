# solution a
base_list: list[float] = []
index: int = 0
height: float = 0
SENTINEL: int = 999
while True:

    height = float(input("Enter height :"))
    if height == SENTINEL:
        break
    if not 1.6 <= height <= 3:
        continue

    if height == 999:
        break
    base_list.append(height)

print("base_list :")
print(f"{base_list} ", end=" ")

print(f"The number of players included in the sample is : {len(base_list)}")
print(f"The highest players is: {max(base_list)}")
print(f"The lowest height: {min(base_list)}")
# import statistics
#print(f"mean == {statistics.mean(grades)}")
average_height: float = sum(base_list) / len(base_list)
print(f"The average height is: {average_height:.2f}")

count_bigger_then_2: int = 0
for x in range(len(base_list)):
    if base_list[x] > 2:
        count_bigger_then_2 += 1
print(f"The numbers which bigger then 2 are : {count_bigger_then_2}")

count_bigger_then_average: int = 0
for x in range(len(base_list)):
    if base_list[x] > average_height:
        count_bigger_then_average += 1
print(f"The numbers which bigger then average are : {count_bigger_then_average}")

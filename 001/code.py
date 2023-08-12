def check(List_Ele, My_List, target):
    for i in range(len(My_List)):
        for j in range(i + 1, len(My_List)):
            if (My_List[i] + My_List[j]) == target:
                return i, j
    return None

List_Length = int(input("Enter the length of the list: "))
My_List = []
for i in range(List_Length):
    ele = int(input(f"Enter element {i+1}: "))
    My_List.append(ele)

target = int(input("Enter the targeted element: "))
result = check(List_Length, My_List, target)

if result is not None:
    target1, target2 = result
    print("index:", f"[{target1}, {target2}]")
    print("Values:", f"{[My_List[target1],My_List[target2]]}")
else:
    print("No pair found that sums up to the target.")

lst = [1, 0, 13, 0, 0, 0, 5]
# lst = [0]
# lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
print("Origin list: ", lst)

zero_qty = lst.count(0)
i = 0
while i < zero_qty:
    lst.remove(0)
    lst.append(0)
    i += 1
print("Modified list: ", lst)

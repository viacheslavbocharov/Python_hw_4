# lst = []
# lst = [0]
# lst = [0, 1, 7, 2, 4, 8, 0]
lst = [0, 1, 7, 2, 4, 8]
print("Origin list: ", lst)
result = None

if len(lst) != 0:
    result = sum(lst[::2])*lst[-1]
else:
    result = 0

equation = []
i = 1
for el in lst[::2]:
    if i == 1: equation.append('(')
    equation.append(el)
    if i == len(lst[::2]):
        equation.append(')*')
        equation.append(lst[-1])
        equation.append('=')
        equation.append(result)
        break
    equation.append('+')
    i += 1

for i in equation:
    print(i, end='')
print()


print("The sum of elements with even indexes multiplied by the last element: ", result)

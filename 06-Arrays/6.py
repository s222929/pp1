array = (2 , 3 , 7, 5, 4)
x = len(array)
print(array, x, array[0], array[1], array[4], array[len(array)-2])
print(array[0] + array[-1])
print(array[len(array)//2])
for i in array:
    print(i, end=" ")
for i in range (len(array)//2+1):
    print(array[i], end=" ")
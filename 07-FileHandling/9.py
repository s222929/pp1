file = open('numbers.txt','r')
sum = 0
for i in file:
    sum = sum + int(i)
file.close()
print(sum)

    


# 5 - misol


list = [1,5,6,4,7,3,9,8,3]

fth = list[0]
lst = list[-1]
print(fth, lst)


# 6 - misol


list = [1,"son", 3, "bir"]

for x in list:
    if type(x) == int:
        print(x)



# 7 - misol


# example true

list =[1,3,5,2,7,4,8,3,9,1,30,26]

n = len(list)
for x in range(n):
    for y in range(0, n - x - 1):
        if list[y] > list[y + 1]:
            list[y], list[y + 1] = list[y + 1],list[y]
print(list)

# example false

list =[1,3,5,2,7,4,8,3,9,1,30,26]

n = len(list)
for x in range(n):
    for y in range(0, n - x - 1):
        if list[y] < list[y + 1]:
            list[y], list[y + 1] = list[y + 1],list[y]
print(list)
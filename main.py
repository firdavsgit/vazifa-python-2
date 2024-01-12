# 1 - misol

num = int(input("son:"))

half = num // 2
if num % 2 == 0:
    print(half, half)
else:
    print(half, half + 1)


# 2 - misol

list = [1,3,2,4,4,1]
element = int(input("choose number:"))
def qoshish(lst, element):
    i = 0
    while i < len(lst):
        if lst[i] == element:
            lst.append(lst.pop(i))
        return lst


print(qoshish(list,element))

# 3 - misol

lst = [1,5,3,6,2,7,8,9,3]

sum_of_lst = 0

for x in lst:
    sum_of_lst += x

print(sum_of_lst)


# 4 - misol

list = ["barselona", "Real madrid", "Bavarya", "Liverpool"]

club = " club ".join(list)
print(club)




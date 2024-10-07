n = int(input("Enter the number of elements in the list: "))
my_list = []
for i in range(n):
    a = int(input("Enter element "))
    my_list.append(a)

print("Your list:", my_list)
num=int(input("Enter the number whose frequency is to counted:"))
counter=0
sum=0
def frequency():
    for i in my_list:
        sum = sum + i
        if (i == num):
            counter = counter + 1
    print("the frequency of number is", counter)

print("the sum of all elements are",sum)
for i in my_list:
    print(my_list[i-1])







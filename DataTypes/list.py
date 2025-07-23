# ======================= list: List data type
# Lists are ordered collections of items that can be of different data types.
# Lists are defined using square brackets [] and can contain any data type, including other lists.
# For example, [1, 2, 3], ["apple", "banana", "cherry"], [[1, 2], [3, 4]] are all lists.
# Lists can also be empty.
# Lists are mutable, meaning you can change their content after creation.
# Lists can be used to store multiple items in a single variable.
# Lists can be indexed, meaning you can access individual items using their position in the list.
# Lists can be nested, meaning you can have lists within lists.
# Lists are versatile and can be used to store collections of items, such as numbers, strings, or even other lists.
# Lists are commonly used to store multiple items in a single variable.
# Examples of list data type
list_var1 = [1, 2, 3] # list of integers
list_var2 = ["apple", "banana", "cherry"] # list of strings
list_var2.append("date") # adding a new item to the list
# change list_var1 to a list of floats
list_var1 = [1.0, 2.0, 3.0]
# push a new item to list_var2
list_var3 = [[1, 2], [3, 4]] # list of lists

print("List examples:", list_var1, list_var2, list_var3)



# List items are ordered, changeable, and allow duplicate values.

# Ordered: Items in a list have a defined order, and that order will not change unless you explicitly change it.
# For example, if you have a list of numbers, they will always appear in the same order unless you modify the list.
# Example


# Changeable: You can change, add, or remove items in a list after it has been created.
# For example, you can add a new item to the end of the list, or remove an item from the middle.




# Allow duplicates: You can have multiple items with the same value in a list.
# For example, [1, 2, 3, 3, 4] is a list with five items, but the value 3 appears twice.
"""Matlab list ke andar jo items tum dalte ho, wo ek fixed order me store hote hain
aur jab tum list ko print karte ho ya use karte ho, wo wahi order me aate hain."""

list_of_fruits = ["apple", "banana", "cherry", "date"]
print("List of fruits:", list_of_fruits)

#====================== accessing items in a list
first_fruit = list_of_fruits[0]  # accessing the first item in the list store in first_fruit then print
second_fruit = list_of_fruits[1]  # accessing the second item in the list store in second_fruit then print
print("First fruit:", first_fruit)
print("Second fruit:", second_fruit)
# access directly using index
print("Third fruit:", list_of_fruits[2])  # accessing the third item in the list



#======================= Changeable example
list_of_friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
list_of_friends[0] = "Bilal"  # changing the first item in the list
print("list of friends ", list_of_friends)

# add new friends in list

new_friend = "Muhammad Ibrahim" # store in new variable 
list_of_friends.append(new_friend) # then use append function to store in list
print(list_of_friends)

# without remove any friend in in list and new friend 3 position

list_of_friends.insert(3, "zahid") # then use insert function to add in list
print(list_of_friends)


list_of_second_group = ["Babar", "Shaheen", "Rizwan", "Faheem Ashraf"]
list_of_second_group.append("Hasan Ali")
list_of_second_group[0] = "shahid Afridi" # if you use this method to add new player in list anypostion thne old remove and new add
# if you want to add new player withou remove anyplayer in list then use insert method
list_of_second_group.insert(0, "Babar Azam")
print("group of pak players ", list_of_second_group)


list_of_cars = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan", "BMW", "Mercedes", "Audi", "Volkswagen", "Hyundai"]
# delete a car from the list
list_of_cars.remove("Ford")  # remove Ford from the list
print("List of cars:", list_of_cars)

removed_car = list_of_cars.pop(2)  # remove the car at index 2 and store it in removed_car
# pop mean remove item from list and store in variable
print("Removed car:", removed_car)

# delete last car from the list
last_car = list_of_cars.pop()  # remove the last car from the list and store it in last_car
print("Last car removed:", last_car)

# difference between remove and pop

"""remove() ka use hota hai value ke basis par item ko delete karne ke liye Tum value doge, python list me search karega aur pehla matching item delete karega Agar wo value list me nahi hai to error dega"""

"""pop() ka use hota hai index ke basis par item ko delete karne ke liye Tum index doge, python uss index par item ko delete karega aur usse return karega Agar index valid nahi hai to error dega Tum index specify kar sakte ho, agar nahi doge to by default last item remove karega Ye remove ki hui value ko return bhi karta hai, jo tum kisi variable me store kar sakte ho"""
# remove() removes the first occurrence of a value from the list, while pop() removes an item at a specific index and returns it.
# If you want to remove an item by value, use remove(). If you want to remove an item by index and get the removed item, use pop().
from lists.linked_list import LinkedList


shopping_list = LinkedList()

shopping_list.append("eggs")
shopping_list.append("milk")
shopping_list.append("flour")

print(shopping_list)



shopping_list.insert(1,"butter")
shopping_list.append("tortillas")
shopping_list.append("bucket")

print(shopping_list)

shopping_list.prepend("ATM")
shopping_list.remove("bucket")
print(shopping_list)

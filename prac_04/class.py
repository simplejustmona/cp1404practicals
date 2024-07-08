"""
names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))

while True:
    name_to_remove = input("Who do you want to remove? ")
    if name_to_remove == "":
        break
    if name_to_remove in names:
        names.remove(name_to_remove)
        print(f"{name_to_remove} has been removed.")
    else:
        print(f"{name_to_remove} is not in the list.")

    print("Updated list: " + ", ".join(names))

print("Final list: " + ", ".join(names))
"""

#create atm withdrawal program.use if else statement to check if the amount is valid and if the balance is sufficient.
# ATM withdrawal program
# withdrawal_amount = float(input("Enter the amount to withdraw: "))
# balance = 1000000.0 
# if withdrawal_amount <= 0:
#      print("Invalid amount. Please enter a positive number.")
# elif withdrawal_amount > balance:
#         print("Insufficient balance.") 
# else:
#     balance -= withdrawal_amount
#     print(f"Withdrawal successful. New balance: {balance}")


# Initial inventory
#create inventory management program. use loops statement to update /display a list of stock items 
# inventory = ["Bread", "Milk", "Eggs", "Soap"]
# def display_inventory():
#     print("\nCurrent Inventory:")
#     if inventory:
#         for i, item in enumerate(inventory, start=1):
#             print(f"{i}. {item}")
#     else:
#         print("Inventory is empty.")
#         print("You can add items to the inventory.")

# while True:
#     display_inventory()
    
#     print("\nMenu:")
#     print("1. Add an item")
#     print("2. Remove an item")
#     print("3. Change an item")
#     print("4. Exit")
    
#     choice = input("Enter your choice (1-4): ")

#     if choice == "1":
#         new_item = input("Enter the item to add: ")
#         inventory.append(new_item)
#         print(f"'{new_item}' has been added to the inventory.")

#     elif choice == "2":
#         try:
#             pos = int(input("Enter the item number to remove: "))
#             if 1 <= pos <= len(inventory):
#                 removed = inventory.pop(pos - 1)
#                 print(f"'{removed}' has been removed.")
#             else:
#                 print("Invalid item number.")
#         except ValueError:
#             print("Please enter a valid number.")

#     elif choice == "3":
#         try:
#             pos = int(input("Enter the item number to change: "))
#             if 1 <= pos <= len(inventory):
#                 new_name = input("Enter the new name: ")
#                 inventory[pos - 1] = new_name
#                 print("Item updated successfully.")
#             else:
#                 print("Invalid item number.")
#         except ValueError:
#             print("Please enter a valid number.")

#     elif choice == "4":
#         print("Exiting Inventory Manager.")
#         break
#     else:
#         print("Invalid choice. Please select between 1 and 4.")

# find factorial of a number using recursion of 5    
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number to find its factorial: "))
if n < 0:
    print("Input positive number")
else:
    print(f"Factorial is {factorial(n)}")
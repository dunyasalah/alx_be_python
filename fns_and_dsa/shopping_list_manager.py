# fns_and_dsa/shopping_list_manager.py

shopping_list = []  # Global list

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if not choice.isdigit():
            print("Invalid choice. Please enter a number.")
            continue

        choice = int(choice)

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f'"{item}" added to the list.')
        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f'"{item}" removed from the list.')
            else:
                print(f'"{item}" not found in the list.')
        elif choice == 3:
            if shopping_list:
                print("Current shopping list:")
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
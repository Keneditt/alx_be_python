def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        
        # Get and validate menu choice as a number
        while True:
            choice_input = input("Enter your choice (1-4): ")
            if choice_input.isdigit() and 1 <= int(choice_input) <= 4:
                choice = int(choice_input)
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        
        if choice == 1:
            # Prompt for and add an item
            item = input("Enter item to add: ").strip()
            if item:
                if item in shopping_list:
                    print(f"'{item}' is already in the list!")
                else:
                    shopping_list.append(item)
                    print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty!")
                
        elif choice == 2:
            # Prompt for and remove an item
            if not shopping_list:
                print("Your shopping list is empty!")
                continue
                
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
                    
        elif choice == 3:
            # Display the shopping list
            if not shopping_list:
                print("Your shopping list is empty!")
            else:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                    
        elif choice == 4:
            print("Goodbye!")
            break
        
        print()  # Add empty line for better readability

if __name__ == "__main__":
    main()
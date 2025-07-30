# shopping_list_manager.py

def main():
    shopping_list = []
    
    while True:
        # Display menu
        print("\nShopping List Manager")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")
        
        # Get user choice
        try:
            choice = input("Enter your choice (1-4): ")
            
            # Add item
            if choice == '1':
                item = input("Enter item to add: ").strip()
                if item:
                    shopping_list.append(item)
                    print(f"'{item}' added to the list.")
                else:
                    print("Item name cannot be empty!")
            
            # Remove item
            elif choice == '2':
                if not shopping_list:
                    print("Your shopping list is empty!")
                    continue
                    
                item = input("Enter item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' removed from the list.")
                else:
                    print(f"'{item}' not found in the list.")
            
            # View list
            elif choice == '3':
                if not shopping_list:
                    print("Your shopping list is empty!")
                else:
                    print("\nCurrent Shopping List:")
                    for i, item in enumerate(shopping_list, 1):
                        print(f"{i}. {item}")
            
            # Exit program
            elif choice == '4':
                print("Exiting program. Goodbye!")
                break
            
            # Invalid choice
            else:
                print("Invalid choice. Please enter a number between 1-4.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
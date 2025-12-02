tasks = []

def show_menu():
    print("\n----- TO-DO LIST MENU -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Clear All Tasks")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice")
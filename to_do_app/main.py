todos = []

file = open('todos.txt', 'r')
todos = file.readlines()
file.close()

while True:
    user_action = input("Type add, show, edit or exit:")
    user_action = user_action.strip()
 
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()            
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'complete':
            number = int(input("Number of the todo to complete"))
            todos.pop(number - 1)
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
            
        case 'exit':
            break
 
print("Bye!")
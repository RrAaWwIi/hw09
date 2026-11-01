document = ""
undo_stack = []
redo_stack = []

while True:
    command = input("type/undo/redo/quit: ").lower().strip()

    if command == "type":
        text = input("Enter text: ")

        undo_stack.append(document)
        document += text

        redo_stack.clear()
        print("Document:", document)

    elif command == "undo":
        if undo_stack:
            redo_stack.append(document)
            document = undo_stack.pop()
            print("Document:", document)
        else:
            print("Nothing to undo")

    elif command == "redo":
        if redo_stack:
            undo_stack.append(document)
            document = redo_stack.pop()
            print("Document:", document)
        else:
            print("Nothing to redo")

    elif command == "quit":
        break

    else:
        print("Unknown command")

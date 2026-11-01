def check_brackets(line):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for index, char in enumerate(line):
        if char in "([{":
            stack.append((char, index))

        elif char in ")]}":
            if not stack or stack[-1][0] != pairs[char]:
                print(f"Problem at position {index}: {char}")
                print(line)
                print(" " * index + "^")
                return

            stack.pop()

    if stack:
        char, index = stack[-1]
        print(f"Problem at position {index}: {char}")
        print(line)
        print(" " * index + "^")
    else:
        print("Balanced")


line = input("Enter a line of code: ")
check_brackets(line)

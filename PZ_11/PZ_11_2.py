with open("text18-29.txt", "r") as file:
    lines = file.readlines()
    text = "".join(lines)
    print("Исходный текст:")
    print(text)
    print(f"количество символов: {len(text)}")

with open("new_text.txt", "w") as new_file:
    new_file.writelines(lines[:2] + [lines[-1] + "\n"] + lines[2:-1])

import brainfuck

FILENAME = "addSubtract.txt"

with open(FILENAME, "r") as f:
    text = f.read()

func = brainfuck.to_function(text)

print(func("86+86"))
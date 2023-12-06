
f = open("input.txt", "r")

lines = f.readlines()

sum = 0

for line in lines:
    for char in line:
        if char.isdigit():
            output = int(char) * 10
            break
    
    for char in reversed(line):
        if char.isdigit():
            output += int(char)
            break
    sum += output

print(sum)
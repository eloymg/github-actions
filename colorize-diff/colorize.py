import fileinput
lines = []
for line in fileinput.input():
    lines.append(line)
table = False
plus = False
minus = False
for i in lines:
    i = i.replace('"',"")
    match i[0:5]:
        case "┌───┬":
            table = True
            print(" " + i[:-1])
        case "│ + │":
            plus = True
            print("+" + i[:-1])
        case "│ - │":
            minus = True
            print("-" + i[:-1])
        case "│   │":
            if plus and table:
                print("+" + i[:-1])
            elif minus and table:
                print("-" + i[:-1])
            else:
                print(" "+i[:-1])
        case "├───┼":
            plus = False
            minus = False
            print(" "+i[:-1])
        case "└───┴":
            table = False
            plus = False
            minus = False
            print(" " + i[:-1])
        case _:
            if i[0:3] == "[+]":
                print("+"+i[:-1])
            elif i[0:3] == "[-]":
                print("-"+i[:-1])
            elif "[+]" in i:
                print("+"+i[1:-1])
            elif "[-]" in i:
                print("-"+i[1:-1])
            else:
                print(i[:-1])
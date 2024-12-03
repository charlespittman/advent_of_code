""" 
--- Day 8: Matchsticks ---

Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. He needs to know how much space it will take up when stored.

It is common in many programming languages to provide a way to escape special characters in strings. For example, C, JavaScript, Perl, Python, and even PHP handle special characters in very similar ways.

However, it is important to realize the difference between the number of characters in the code representation of the string literal and the number of characters in the in-memory string itself.

For example:

    "" is 2 characters of code (the two double quotes), but the string contains zero characters.
    "abc" is 5 characters of code, but 3 characters in the string data.
    "aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
    "\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.

Santa's list is a file that contains many double-quoted string literals, one on each line. The only escape sequences used are \\ (which represents a single backslash), \" (which represents a lone double-quote character), and \x plus two hexadecimal characters (which represents a single character with that ASCII code).

Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file?

For example, given the four strings above, the total number of characters of string code (2 + 5 + 10 + 6 = 23) minus the total number of characters in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.
"""

def get_input(file=None):
    data = [
        "123 -> x",
        "456 -> y",
        "x AND y -> d",
        "x OR y -> e",
        "x LSHIFT 2 -> f",
        "y RSHIFT 2 -> g",
        "NOT z -> h",
        "NOT y -> i",
    ]

    if file:
        with open("input") as f:
            data = file.readlines()

    return data


def parse_line(line):
    name = None
    op = None
    input1 = None
    input2 = None

    input, name = line.split("->")
    name = name.strip()
    input = input.split()

    if len(input) == 1:
        op = "SET"
        input1 = input[0]
    if len(input) == 2:
        op = input[0]
        input1 = input[1]
    if len(input) == 3:
        op = input[1]
        input1 = input[0]
        input2 = input[2]
    if input1 and input1.isdecimal():
        input1 = int(input1)
    if input2 and input2.isdecimal():
        input2 = int(input2)

    return name, op, input1, input2


def solve():
    data = get_input()

    for line in data:
        name, op, input1, input2 = parse_line(line)
        gates[name] = Gate(name, op, input1, input2)

    return gates


solution = solve()
for k, v in gates.items():
    print(k, v)

print(gates["x"].value())
print(gates["d"])

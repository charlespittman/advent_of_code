""" 
--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

    123 -> x means that the signal 123 is provided to wire x.
    x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
    p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
    NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i

After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456

In little Bobby's kit's instrquctions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
"""

test_input = [
    "x -> z",
    "123 -> x",
    "456 -> y",
    "x AND y -> d",
    "x OR y -> e",
    "x LSHIFT 2 -> f",
    "y RSHIFT 2 -> g",
    "NOT x -> h",
    "NOT y -> i",
]


def get_input(use_sample_data=False):
    if use_sample_data:
        return test_input
    else:
        with open("input") as f:
            return f.readlines()


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


def get_gates(data):
    gates = {}
    for line in data:
        name, op, input1, input2 = parse_line(line)
        gates[name] = (op, input1, input2)
    return gates


def solve(gate):
    if isinstance(gates[gate], int):
        return gates[gate]
    print(gate)
    op = gates[gate][0]
    input1 = gates[gate][1]
    input2 = gates[gate][2]

    immediate1 = isinstance(input1, int)
    immediate2 = isinstance(input2, int)

    print("1: name={}, op={}, input1={}, input2={}".format(gate, op, input1, input2))

    if isinstance(input1, int):
        pass
    elif iswire(input1):
        input1 = solve(input1)

    if isinstance(input2, int):
        pass
    elif iswire(input2):
        input2 = solve(input2)

    print("2: name={}, op={}, input1={}, input2={}".format(gate, op, input1, input2))

    if op == "SET":
        gates[gate] = input1
        return input1
    if op == "NOT":
        return input1 ^ 65535
    if op == "AND":
        return input1 & input2
    if op == "OR":
        return input1 | input2
    if op == "LSHIFT":
        return input1 << input2
    if op == "RSHIFT":
        return input1 >> input2

    # for line in data:
    #     print(g)
    #     name, op, input1, input2 = parse_line(line)
    #     print("name={}, op={}, input1={}, input2={}".format(name, op, input1, input2))
    #     # print(type(input1), type(input2))
    #     # print(iswire(input1), iswire(input))
    #     if iswire(input1):
    #         input1 = g.get(input1, None)
    #     if iswire(input2):
    #         input2 = g.get(input2, None)
    #     if op == "SET" and input1:
    #         g[name] = input1
    #     if op == "NOT" and input1:
    #         g[name] = input1 ^ 65535
    #     if op == "AND" and input1 and input2:
    #         g[name] = input1 & input2
    #     if op == "OR" and input1 and input2:
    #         g[name] = input1 | input2
    #     if op == "LSHIFT" and input1 and input2:
    #         g[name] = input1 << input2
    #     if op == "RSHIFT" and input1 and input2:
    #         g[name] = input1 >> input2
    #     print(g)
    # return g


def iswire(w):
    if str(w).islower():
        return True
    return False


if __name__ == "__main__":
    data = get_input(use_sample_data=False)
    gates = get_gates(data)
    # print(gates)
    print(gates["a"])
    print(solve("a"))

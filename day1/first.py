#!/usr/bin/env python3

from common import parse_input_lines

import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'input'

def parse_instruction(raw_instruction, filename = 'input'):
    direction = raw_instruction[0]
    clicks = int(raw_instruction[1:])

    return direction, clicks

lines = parse_input_lines('day1', filename)

start = 50
password = 0 

print(f"Initial position: {start}\n")

for raw_instruction in lines:
    direction, clicks = parse_instruction(raw_instruction)

    if direction == 'R':
        start += clicks
    elif direction == 'L':
        start -= clicks

    # Normalize to 0-99
    start = start % 100

    print (f"Instruction: {raw_instruction.strip()} -> {direction} {clicks} ->\t New position: {start}")

    if start == 0:
        print("Landed on 0")
        password += 1


print(f"\nFinal password: {password}")

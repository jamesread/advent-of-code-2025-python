def parse_input_lines(day, filename):
    filename = f"{day}/{filename}"

    input_file = open(filename, "r")

    input_lines = input_file.readlines()

    return input_lines

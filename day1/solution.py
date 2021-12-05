def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return lines

def count_increase(lines):
    prev_line = 0
    number_of_increase = 0
    for line in lines:
        line = int(line)
        if line > prev_line:
            number_of_increase+=1
        prev_line = line
    return number_of_increase-1

def generate_sums_of_three(lines):
    sums_of_three =[]
    for i, val in enumerate(lines):
        if i+2 == len(lines): break
        sums_of_three.append(int(lines[i]) + int(lines[i+1]) + int(lines[i+2]))
    return sums_of_three

print(count_increase(generate_sums_of_three(read_file('data'))))

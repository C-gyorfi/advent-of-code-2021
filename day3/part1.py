def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return lines

def process_numbers(lines):
    one = []
    zero = []
    result_g = ""
    result_e = ""

    for line in lines:
        line = line.strip()
        if len(one) == 0:
          for i in range(len(line)):
            one.append(0)
            zero.append(0)
        for n in range(len(line)):
            if line[n] == '1':
                one[n] += 1
            else:
                zero[n] += 1
    for n in range(len(line)):
        if one[n] > zero[n]:
            result_g += '1'
            result_e += '0'
        else:
            result_g += '0'
            result_e += '1'

    return int(result_g, 2) * int(result_e, 2)

print(process_numbers(read_file('data')))


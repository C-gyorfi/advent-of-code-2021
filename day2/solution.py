def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return lines

def get_position_multiply(lines):
    x = 0
    y = 0
    for line in lines:
        if line.startswith('forward'): x += int(line[-2])
        if line.startswith('down'): y+= int(line[-2])
        if line.startswith('up'): y-= int(line[-2])
    return x*y

def get_position_using_aim(lines):
    x = 0
    y = 0
    aim = 0
    for line in lines:
        if line.startswith('forward'): 
            x += int(line[-2])
            y += (int(line[-2]) * aim)
        if line.startswith('down'): aim+= int(line[-2])
        if line.startswith('up'): aim-= int(line[-2])
    return x*y

print(get_position_using_aim(read_file('data')))
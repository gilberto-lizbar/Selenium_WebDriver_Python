# Open the file
file = open("test.txt")
# Read all contents of file
# print(file.read())
# Read contents by passing parameters
# print(file.read(2))

# print(file.readline())
# print(file.readline())

# file.close()

# *************Read Line with while loops*********************************
# Print line by line using readLine method
'''line = file.readline()
while line != "":
    print(line)
    line = file.readline()
file.close()'''

# *************Read Line with for loop*********************************
# Print line by line using readLine method
'''for line in file.readlines():
    print(line)'''


def get_lines_list():
    line = []
    for line in file.readlines():
        print(line)
    return line


def get_number_lines():
    with open('test.txt', 'r') as file1:
        count = sum(1 for line in file1)
        print(f'Total number of lines: {count}')
    return count

lines = get_lines_list()
print(lines[3])
print(get_number_lines())
print("*********")
file.close()

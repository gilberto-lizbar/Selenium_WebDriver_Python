# open the file as 'r 'read mode, 'open with' closes the file at the end of execution
# not necessary to add close() method at the end
with open("test.txt", "r") as reader:  # reader is the object created for the file it can
    # be named as any name
    content = reader.readlines()  # ['abc\n', 'b\n', 'c\n', 'd\n', 'e\n', 'textssss\n']
    reversed(content)  # this adds a reverse operator to iterate, instead iterate starting 1st
    # element 'abc' it will start from the last element 'textssss'
    with open("test.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)  # this method will write the reversed content into test.txt
            print(line)

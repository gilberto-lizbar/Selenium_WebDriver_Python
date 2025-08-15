num = 10
flag = False

while num > 1:
    if num > 5:
        num = num - 1
        print(num)
        continue
    else:
        if num < 5:
            flag = True
            print("condition satisfied")
            break
    num = num - 1

print("{},{}".format("While loop ended flag is equal to = ", flag))

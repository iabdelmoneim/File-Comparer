import output




# You can specifiy the path for files of the SAV ROLES or what you would like to compare
f1 = open("C:/Users/Ibrahim Abdelmoneim/Desktop/Tickets logs/ObjectSummary_2021-11-16_09-21-24(UTC).json", "r")
f2 = open("C:/Users/Ibrahim Abdelmoneim/Desktop/Tickets logs/ObjectSummary_2022-01-05_10-45-30(UTC).json", "r")


i = 0

for line1 in f1:
    i += 1

    for line2 in f2:

        # matching line1 from both files
        if line1 == line2:
            # print IDENTICAL if similar
            print("Line ", i, ": IDENTICAL")
        else:
            print("Line ", i, ":")
            # else print that line from both files
            print("\tFile 1:", line1, end='')
            print("\tFile 2:", line2, end='')
        break

# closing files
f1.close()
f2.close()

f = open('C:/Users/Ibrahim Abdelmoneim/Desktop/Tickets logs/New5.txt', 'w')
print(output, file=f)

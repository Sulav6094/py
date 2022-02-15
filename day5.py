# a=open("text.txt")
# b=a.read()
# print(b)
# s=open("text.txt","w")
# s.writelines(b)
# file = open("filename.txt", "r")

# outfile = ""

# for line in range(1, 10):
#     if line % 2 == 0:
#         outfile += file.readline()
#     else:
#         file.readline()

# file = open("filename.txt", "w")
# file.write(outfile)
# file.close()

# file = open("teams.txt", "r")

# outfile = ""

# for line in range(1, 10):
#     if line == 1 or line==4:
#         outfile += file.readline()
#     else:
#         file.readline()
# print (outfile)
file = open("teams.txt", "r")
a=file.readlines()
outfile = "This is a new line \n"

for l in a:
    outfile+=l
print(outfile,a)

# for line in range(1, 10):
#         outfile += file.readline()

file = open("teams.txt", "w")
file.write(outfile)
file.close()

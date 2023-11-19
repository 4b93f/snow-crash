import sys

str = open('/home/user/level09/token')

str = str.read()
print(str)


res = ""
for count, value in enumerate(str):
        c = ord(value[0])
	print(chr((c - count)))

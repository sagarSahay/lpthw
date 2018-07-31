from sys import argv

script, filename = argv

print(f"We're going to read form file {filename}")

print("Opening the file..")
target = open(filename, 'r')

print("Here's the content")

print(target.readlines())

target.close()

# Write a program to read a file and display its contents. 
print("1:")

file = open("assessment5.2.py", "r")

content = file.read()
print(content)

file.close()


# Write a program to count the number of lines in a file.
print("2:")

file = open("assessment5.2.py", "r")

lines = file.readlines()
print("Number of lines:", len(lines))

file.close()



# Write a program to count how many times each word appears in a file.
print("3:")

file = open("assessment5.2.py", "r")

text = file.read()
words = text.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

file.close()



# Write a program to write 5 user-entered sentences to a file.
print("4:")

file = open("sentences.txt", "w")

for i in range(5):
    sentence = input("Enter a sentence: ")
    file.write(sentence + "\n")

file.close()


# Write a program to append a list of strings to an existing file.
print("5:")

lines = ["Hello\n", "Welcome\n", "Python File Handling\n"]

file = open("list.txt", "a")

file.writelines(lines)

file.close()



# Write a program to read a file and print only lines containing a specific word.
print("6:")

file = open("assessment5.2.py", "r")

word = input("Enter word to search: ")

for line in file:
    if word in line:
        print(line)

file.close()



# Write a program to replace a specific word in a file and save changes. 
print("7:")

file = open("list.txt", "r")
text = file.read()
file.close()

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

text = text.replace(old_word, new_word)

file = open("list.txt", "w")
file.write(text)
file.close()





# Write a program to merge the contents of two text files into a third file.
print("8:")
file1 = open("list.txt", "r")
file2 = open("sentences.txt", "r")
file3 = open("merge.txt", "w")

file3.write(file1.read())
file3.write(file2.read())

file1.close()
file2.close()
file3.close()


# Write a program to read a CSV file and display its content in a formatted way.
print("9:")
import csv

file = open("industry.csv", "r")
reader = csv.reader(file)

for row in reader:
    print(" | ".join(row))

file.close()


# Write a program to back up a file by copying its contents into another file.
print("10:")

source = open("sample.txt", "r")
backup = open("backup.txt", "w")

backup.write(source.read())

source.close()
backup.close()

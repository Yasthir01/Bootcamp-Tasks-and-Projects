""" A program that counts the number of characters, words, lines and vowels in a file"""


f = open('input.txt', 'rt')

# count the number of characters in the file
content = f.read()
char_content = content.replace(" ", "")  # replace the empty spaces with no spaces 
num_characters = len(char_content)  # the length will be the number of characters
print(f"The number of characters in the file: {num_characters}")

# count the number of words in the file
num_words = content.split()  # convert the content into a list
print(f"The number of words in the file: {len(num_words)}")

# count the number of lines in the file
num_lines = content.split('\n')  # split the content at each new line to get a list of lines
print(f"The number of lines in the file: {len(num_lines)}")

# count the number of vowels in the file
vowel_counter = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for letter in content:
	if letter in vowels:
		vowel_counter += 1
print(f"The number of vowels in the file: {vowel_counter}")

f.close()

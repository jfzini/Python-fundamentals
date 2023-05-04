# Types of file manipulation in Python
# open('file.path', 'mode')
# open('path', 'r') => read only
# open('path', 'w') => creates a new file and overwrite if already exists
# open('path', 'x') => creates a new file or returns error if already exists
# open('path', 'a') => creates a new file or add to the final of the file if already exists
# 't' => text
# 'b' => binary
# 'file'.close() => always close a file after opening it

text = open('text_file.txt', 'r')
content = text.read()
text.close()

print(content)
print(type(content))

text = open('text_file.txt', 'r')
content = text.readlines()
text.close()

print(content)
print(type(content))

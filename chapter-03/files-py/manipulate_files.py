# Types of file manipulation in Python
# open('file.path', 'mode')
# open('path', 'r') => read only
# open('path', 'w') => creates a new file and overwrite if already exists
# open('path', 'x') => creates a new file or returns error if already exists
# open('path', 'a') => creates a new file or add to the final of the file if already exists
# 't' => text
# 'b' => binary
# 'file'.close() => always close a file after opening it

# obj = open('test.js', 'r')  # it can read js files but not sure if i can use this further
# obj_content = obj.read()
# obj.close()
# print(obj_content)

# text = open('text_file.txt', 'r')
# content = text.read()
# text.close()

# print(content)
# print(type(content))

# text = open('text_file.txt', 'r')
# content = text.readlines()
# clean_content = []
# for line in content:
#     clean_content.append(line.rstrip())
# text.close()

# print(clean_content)

# text = open('text_file.txt', 'a')
# text.write('Fortaleza \n')
# text.close()

text = open('text_file.txt', 'a')
lines = ['São Luís \n', 'Palmas\n', 'Belém\n']
text.writelines(lines)
text.close()

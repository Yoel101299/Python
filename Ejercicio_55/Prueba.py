with open('spam.txt', 'w') as file:
    file.write('Spam and eggs!')

print(file.closed)
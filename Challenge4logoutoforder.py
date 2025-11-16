file_name = input("Enter the name of the file to append to: ")
user_sentence = input("Enter a sentence: ")

with open(file_name, 'a') as file:
  file.write(user_sentence + "\n")  # Add a newline character after each sentence

file_contents = file.read()

print(file_contents)
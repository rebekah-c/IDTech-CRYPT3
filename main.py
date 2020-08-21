alphabet = "abcdefghijklmnopqrstuvwxyz"
partial_one = ""
partial_two = ""
new_alphabet = ""

message = input("Secret message: ")
index = int(input("How many indexes do you want to shift the cipher by? "))
if index == 0:
  new_alphabet = alphabet
# If user enters positive number, shift original alphabet by number
elif index > 0:
  partial_one = alphabet[:index]
  partial_two = alphabet[index:]
  new_alphabet = partial_two + partial_one
  print(new_alphabet)
else:
  partial_one = alphabet[:(26+index)]
  partial_two = alphabet[(26+index):]
  new_alphabet = partial_two + partial_one
  print(new_alphabet)

new_message = ""
for x in range(0, len(message)):
  m_index = alphabet.find(message[x])
  if m_index < 0:
    new_message = new_message + message[x]
  else:
    new_message = new_message + new_alphabet[x]
print(new_message)
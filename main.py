alphabet = "abcdefghijklmnopqrstuvwxyz"
message = "wpau iwt ephhldgs udg iwt uxghi rajt xh tctgvxots"
def decode(message):
  for i in range(0, len(alphabet)):
    new_alphabet = alphabet[i:] + alphabet[:i]
    attempt = ""
    for x in range(0, len(message)):
      index = alphabet.find(message[x])
      if index < 0:
        attempt = attempt + message[x]
      else:
        attempt = attempt + new_alphabet[index]
    print("Key: " + str(i) + " " + attempt)
decode(message)
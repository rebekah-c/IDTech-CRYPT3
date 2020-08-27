numbers = [0x69, 0x44, 0x54, 0x65, 0x63, 0x68]
text = ""
for x in numbers:
  text = text + chr(x)
print(text)

csi = "\x1b["
color = "34m"
colored_text = csi + color + text
print(colored_text)

message = "secret"
decoded = []
for x in message:
  character = ord(x)
  decoded.append(hex(character))
print(decoded)

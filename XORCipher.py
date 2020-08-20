code = "1001001010100001"
key = "1001110100010101"
print("Code " + code)
print("Key " + key)

code_int = [
  int(i)
  for i in str(code)
]
print(code_int)

key_int = [
  int(i)
  for i in str(key)
]
print(key_int)

cipher_integers = []
for x in range(0, len(code_int)):
  cipher_bit = code_int[x] ^ key_int[x]
  cipher_integers.append(cipher_bit)
  cipher = "".join(
    str(b) for b in cipher_integers
  )
print(cipher)

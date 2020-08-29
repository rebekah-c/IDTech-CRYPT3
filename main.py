def pad_message(message, block_size=4):
  message_list = []
  chunk = 0
  block_count = len(message)//block_size+1
  for x in range (block_count * block_size):
    chunk = chunk << 8
    if x < len(message):
      chunk = chunk + ord(message[x])
    else:
      chunk = chunk + 0
    if chunk.bit_length() > (block_size-1)*8:
      message_list.append(chunk)
      chunk = 0
  return message_list

def rebuild_message(message_list, block_size=4):
  message = ""
  for x in range(0, len(message_list)):
    chunk = message_list[x]
    for i in range(block_size):
      number = (chunk >> (8*(block_size-1-i)))%2**8
      # print(str(bin(chunk))+" chunk")
      # print(bin(number))
      message = message + chr(number)
    # print(message)
  print(message)
  return message

def apply_shift(message_list, key, block_size=4):
  cipher_list = []
  bit_max = block_size*8
  for x in range(0, len(message_list)):
    chunk = message_list[x]
    #print(chunk % (2 ** key))
    #print(2 ** key)
    #print(chunk)
    carry = chunk % (2 ** key)
    carry = carry << (bit_max - key)
    #print(carry)
    cipher = (chunk >> key) + carry
    #print(bin(cipher))
    cipher_list.append(cipher)
  return cipher_list

def undo_shift(cipher_list, key, block_size=4):
  message_list = []
  bit_max = block_size*8
  for x in range(0, len(cipher_list)):
    chunk = cipher_list[x]
    carry = chunk % (2 ** (bit_max - key))
    #print(bin(carry))
    carry = carry << key
    #print(bin(carry))
    number = (chunk >> (bit_max - key)) + carry
    #print(bin(number))
    message_list.append(number)
  return message_list

def main():
  print("Start")
  message = "Here is a top secret message"
  print(message)
  decoded = pad_message(message)
  print(decoded)
  rebuild_message(decoded)
  
  cipher_list = apply_shift(pad_message(message), 5)
  print(cipher_list)
  cipher = rebuild_message(cipher_list)
  print(cipher)
  message_list = undo_shift(cipher_list, 5)
  print(message_list)
  
if __name__ == "__main__":
  main()
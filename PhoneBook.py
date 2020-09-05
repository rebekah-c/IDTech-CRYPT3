def new_hash(message):
  digest = 0
  if message == "":
    digest = -1
  for x in message:
    digest += ord(x)
  digest = digest % max_size
  return digest

#list of tuples
phone_book = [
  ("Alice", 4082553555),
  ("", 0000000000),
  ("Diane", 9838978345),
  ("Bob", 6503879023),
  ("", 0000000000),
  ("Eve", 7642398541),
  ("Charlie", 5052358763)
]
max_size = 19
while len(phone_book) < max_size-1:
  phone_book.append(("", 0000000000))
phone_book.append(("Bill", 8976543898))
print(phone_book)

sorted_book = sorted(phone_book, key=lambda phone_book:phone_book[0])
while sorted_book[0][0] == "":
  del(sorted_book[0])

# Hash sort
phone_hash = []
hash_book = [("", 0) for _ in range(max_size)]
#print(hash_book)
for i in range(len(phone_book)):
  name = phone_book[i][0]
  digest = new_hash(name)
  if digest == -1:
    continue
  phone_hash.append(digest)
  new_index = digest
  while hash_book[new_index] != ("", 0):
    new_index = (new_index+1) % max_size
  hash_book[new_index] = phone_book[i]
print("Hash book: ")
print(hash_book)

search_name = input("Look up which name: ")
search_count = 0
for i in range(len(phone_book)):
  search_count += 1
  if phone_book[i][0] == search_name:
    print("Unsorted book search: ")
    print(phone_book[i][0])
    print(search_count)
    break
  if search_count == max_size:
    print("Not found")

search_index = int(len(sorted_book)/2)
search_max = len(sorted_book)-1
search_min = 0
search_count = 0
for i in range(len(sorted_book)):
  search_count += 1
  if search_name == sorted_book[search_index][0]:
    print("Sorted book search: ")
    print(sorted_book[search_index][0])
    print(search_count)
    break
  elif search_name < sorted_book[search_index][0]:
    search_max = search_index
    search_index -= int((search_index - search_min)/2 + 0.5)
  elif search_name > sorted_book[search_index][0]:
    search_min = search_index
    search_index += int((search_max - search_index)/2 + 0.5)
  if search_count == len(sorted_book):
    print("Not found alphabetically")

# Search hash phonebook
hash_index = new_hash(search_name)
search_count = 0
for x in range(len(hash_book)):
  search_count += 1
  if hash_book[hash_index][0] == search_name:
    print("Hash book search: ")
    print(hash_book[hash_index][1])
    print(search_count)
    break
  hash_index = (hash_index + 1) % max_size
  if search_count == max_size:
    print("Not found--hash")

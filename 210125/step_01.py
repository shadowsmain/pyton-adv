name = 'иван'
alphabet = {chr(el) for el in range (ord('а'), ord('я') + 1)}
alphabet_2 = [chr(el) for el in range (ord('а'), ord('я') + 1)]
alphabet_3 = {chr(el): el for el in range (ord('а'), ord('я') + 1)}

print (type(alphabet), type(alphabet_2), type(alphabet_3))

print ('z' in alphabet, 'r' in alphabet)
print ('z' in alphabet_2, 'r' in alphabet_2)
print ('z' in alphabet_3, 'r' in alphabet_3)

print(alphabet)
print(alphabet_2)
print(alphabet_3.keys())
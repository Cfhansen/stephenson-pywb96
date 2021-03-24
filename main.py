###solution to exercise 96 from ben stephenson's "the python workbook".

def good(password):
  uppercase = False
  lowercase = False
  number = False

  uppercases = []
  for i in range(65,91):
    uppercases.append(chr(i))
  lowercases = []
  for i in range(97,123):
    lowercases.append(chr(i))
  numbers = []
  for i in range(48,58):
    numbers.append(chr(i))

  for i in password:
    if i in uppercases:
      uppercase = True
    if i in lowercases:
      lowercase = True
    if i in numbers:
      number = True

  if uppercase and lowercase and number and (len(password) >= 8):
    return True
  else:
    return False

mypass = str(input('Enter a password: '))
print(f'Is that a good password: {good(mypass)}.')

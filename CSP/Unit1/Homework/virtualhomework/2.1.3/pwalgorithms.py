# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

def two_words(password):
  words = get_dictionary()
  guesses = 0
  for w in words:
    for i in words:
      guesses+=1
      if (w+i == password or i+w == password):
        return True, guesses
  return False, guesses

def two_words_and_digit(password):
  words = get_dictionary()
  guesses = 0 
  for w in words:
    for i in words:
      for j in range(10):
        guesses+=1
        if (w+i+str(j) == password or i+w+str(j) ==password):
          return True, guesses
  return False, guesses
        
      
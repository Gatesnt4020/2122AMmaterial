# a213_pw_analyzer.py
import time
import pwalgorithms as pwa

password = input("Enter password: ")
ui = input("1 or 2 word or 2 with digit pass ")
if ui == "1":
  print("Analyzing a one-word password ...")
elif ui == "2":
  print("Analyzing a two-words password ...")
else:
  print("Analyzing a two-words and digit password ...")
time_start = time.time()

# attempt to find password
if ui == "1":
  found, num_guesses = pwa.one_word(password)
elif ui == "2":
  found, num_guesses = pwa.two_words(password)
else:
  found, num_guesses = pwa.two_words_and_digit(password)
time_end = time.time()

# report results
if (found):
  print(password, "found in", num_guesses, "guesses")
else: 
  print(password, "NOT found in", num_guesses, "guesses!")
print("Time:", format((time_end-time_start), ".8f"))
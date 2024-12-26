def main():
  file_path = './books/frankenstein.txt'
  text = get_book_text(file_path)
  words = get_text_count(text)
  character_count = get_character_count(text)
  print_report(file_path, words, character_count)

def get_book_text(file_path):
  with open(file_path) as f:
    return f.read()

def get_text_count(text):
  return len(text.split())

def get_character_count(text):
  payload = {}
  for char in text:
    key = char.lower()
    if key in payload:
      payload[key] += 1
    else:
      payload[key] = 1

  return payload

def print_report(file_path, word_count, character_count):
  print(f"--- Begin report of {file_path} ---")
  print(f"{word_count} words found in the document \n")

  for char in character_count:
    print(f"The '{char}' character was found {character_count[char]} times")

  print(f"--- End report ---")


main()
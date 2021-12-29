from PyDictionary import PyDictionary

dictionary = PyDictionary()


def find_meaning(words):
    meaning = dictionary.meaning(words)
    for key, value in meaning.items():
        meaning_list = value
        print(f"{key} :")
        for item in meaning_list:
            print(item)


word = input("Enter the word whose meaning you want to find: ")
find_meaning(word)

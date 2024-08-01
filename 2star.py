def sort_words_alphabetical(words):
    return sorted(words)
input_user = input("Enter a list of words separated by spaces: ")
words_list = input_user.split()
sorted_words = sort_words_alphabetical(words_list)
print("Sorted words:", ' '.join(sorted_words))

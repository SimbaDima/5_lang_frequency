import re
import sys


def load_data_from_file(file_path):
    try:
        with open(file_path) as object_file:
            data_of_file = object_file.read()
            return data_of_file
    except FileNotFoundError:
            return None


def get_most_frequent_words(data_of_file):
    mass_of_word_match_pattern = re.findall(r'\b\w{1,50}\b', data_of_file)
    dictionary_of_frequncys = {}
    for word in mass_of_word_match_pattern:
        count = dictionary_of_frequncys.get(word, 0)
        dictionary_of_frequncys[word] = count + 1

    array_sorted_in_wane_by_count = sorted(dictionary_of_frequncys.items(),
                                           key=lambda x: -x[1])

    ten_elements_of_array_sorted = array_sorted_in_wane_by_count[0:10]
    return ten_elements_of_array_sorted


def deduce_frequent_word_and_count(ten_elements_of_array_sorted):
    for element in ten_elements_of_array_sorted:
        print(element[0], element[1])


if __name__ == '__main__':
    try:
        object_file_of_user = load_data_from_file(sys.argv[1])
        mass_most_frequent_words = get_most_frequent_words(object_file_of_user)
        deduce_frequent_word_and_count(mass_most_frequent_words)
    except IndexError:
        print("enter by path to file in which to be text")

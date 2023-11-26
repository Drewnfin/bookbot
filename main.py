def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    chars_dict = get_char_dict(text)
    chars_sorted_list = sort_dict_to_list(chars_dict)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{num_words} words found in the document\n")

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The {item['char']} character was found {item['num']} times")
    
    print("--- End report ---") 

def sort_on(d):
    return d["num"]


def sort_dict_to_list(dict):
    sorted_list = []
    for c in dict:
        sorted_list.append({"char": c, "num": dict[c]})
    #sort not working properly
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_char_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
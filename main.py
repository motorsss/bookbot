def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count(text)
    num_char = get_chars_dict(text)
    chars_sorted = sortchar(num_char)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for w in chars_sorted:
        print(f"The '{w['char']}' character was found {w['num']} times")
    
    print("--- End report ---")


def count(path):
    words = path.split()
    return len(words) 

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def sortchar(dic):
    alp = []
    for chr in dic:
        if chr.isalpha():
            alp.append({"char": chr, "num": dic[chr]})      
        else:
            continue
    alp.sort(reverse=True, key=sort_on)
    return alp
    


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
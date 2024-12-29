def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_letter_count(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    letter_list=list(letter_count.items())
    letter_list.sort(reverse= True, key= sort_on)

    for letter, freq in letter_list:
        if letter.isalpha():
            print(f"The '{letter}' character was found {freq} times")
    
    print(f"--- End report ---")

def get_letter_count(text):
    letter_freq = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in letter_freq:
            letter_freq[lower_char]+=1
        else:
            letter_freq[lower_char]=1

    return letter_freq

    

def sort_on(item):
    return item[1]




def get_num_words(text):
    words = text.split()
    return len(words)



def get_book_text(path):    
    with open(path) as f:
        return f.read()

if __name__ == "__main__":        
    main()
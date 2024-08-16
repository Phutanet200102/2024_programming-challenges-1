import string


def pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(set(s.lower()))

def check(s):
    if not pangram(s):
        return "Not a Pangram"
    
    words = s.split()
    longest_word = max(words, key=len)
    return longest_word

def main():
    input_string = input("Input Word: ")
    result = check(input_string)
    print("Output: ",result)

if __name__ == "__main__":
    main()

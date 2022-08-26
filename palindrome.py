def is_palindrome(string: str) -> bool:
    string = string.replace(" ","").lower()
    return string == string[::-1]

def run():
    word = input("Por favor ingresa una palabra: ")
    print(is_palindrome(word))

if __name__ == "__main__":
    run()
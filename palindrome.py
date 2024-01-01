def cleaned_up_palindrome(string):
    cleaned_string = ''.join(filter(str.isalpha, string)).lower()
    return cleaned_string == cleaned_string[::-1]

text = str(input("Enter your text if it is a Palindrome or not: "))


palindrome = cleaned_up_palindrome(text)

if palindrome:
    print(f'"{text}" is a palindrome!')
else:
    print(f'"{text}" is not a palindrome.')

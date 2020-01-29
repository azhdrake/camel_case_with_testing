def filter_out_line_breaks(word):
    filtered_word = ""
    for char in word:
        if char != '\n' and char != '\t':
            filtered_word += char
    return filtered_word

def camel_case(sentence):
    words = sentence.split(' ')

    lower_list = [filter_out_line_breaks(word) for word in words]
    Cap_list = [word.capitalize() for word in lower_list]

    new_string = ''

    for word in Cap_list:
        new_string += str(word)

    new_string = new_string[0].lower() + new_string[1:]
    return new_string

def main():
    user_input = input("Enter sentence")
    print(camel_case(user_input))

if __name__ == '__main__':
    main()

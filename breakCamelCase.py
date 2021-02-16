#codewars kata kyu 6
"""Complete the solution so that the function will break up camel casing, using a space between words"""

def breakCamelCase(input_text):
    word_list = []
    start = None
    for index in range(len(input_text)):
        if ord(input_text[index]) >= 65 and ord(input_text[index]) <= 90:
            word_list.append(input_text[start:index])
            start = index
    word_list.append(input_text[start:len(input_text)])
    print(word_list)
    print(' '.join(word_list))

if __name__ == "__main__":
    breakCamelCase('camelCaseExample')

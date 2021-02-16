import string
def to_jaden_case(input_text):
    print(string.capwords(input_text, ' '))

if __name__ == "__main__":
    to_jaden_case('this Is a test')

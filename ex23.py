import sys 
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) # main() calls itself, this is called recursion



def print_line(line, encoding, errors):
    next_lang = line.strip() # strip() removes the trailing newline character
    raw_bytes = next_lang.encode(encoding, errors=errors) # encode() returns a bytes object
    cooked_string = raw_bytes.decode(encoding, errors=errors) # decode() returns a string object
    print(raw_bytes, "<===>", cooked_string)



languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
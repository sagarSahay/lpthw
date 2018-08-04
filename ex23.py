import sys

script, encoding, error = sys.argv


def main(language_file, encoding_param, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding_param, errors)
        return main(language_file, encoding_param, errors)


def print_line(line, encoding_param, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding_param, errors=errors)
    cooked_string = raw_bytes.decode(encoding_param, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding=encoding)
main(languages, encoding, error)





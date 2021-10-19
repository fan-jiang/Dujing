# This Python file uses the following encoding: utf-8

import argparse
import Convert


def update_file():
    parser = argparse.ArgumentParser(
        description='Generate a classic book with the desired format.')
    parser.add_argument('sort', type=str, help='simplified or tranditional')
    parser.add_argument('book', type=str, help='a book file')
    args = parser.parse_args()
    filePath = args.book
    sort = args.sort
    try:
        book = None
        with open(filePath, 'r') as file:
            book = file.read().decode("utf-8")
        if sort == 'Simplified':
            book = Convert.Convert(book)
        else:
            book = Convert.CheckedToneMarker.mark_checked_tone_chars(
                book)
        with open(filePath, 'w') as file:
            file.write(book.encode("utf-8"))
    except IOError:
        print("IOError occurs while handling the file (" + filePath + ").")


if __name__ == '__main__':
    update_file()

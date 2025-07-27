from stats import (
    character_counter,
	character_list,
    words_counter,
)


def get_book_text():
	with open("/home/blaise/Workspace/repos/bookbot/books/frankenstein.txt") as f:
		file_contents = f.read()

	return file_contents


def generate_report(book):
	report_text = f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {words_counter(book)} total words
--------- Character Count -------
"""
	count_dict = character_counter(book)
	char_list = character_list(count_dict)

	for c in char_list:
		report_text += f"{c['char']}: {c['num']}\n"

	report_text += "============= END ==============="
	return report_text


if __name__ == "__main__":
	# print(get_book_text())
	book = get_book_text()
	# print(words_counter(book))
	# print(character_counter(book))
	print(generate_report(book))

from stats import words_counter


def get_book_text():
	with open("/home/blaise/Workspace/repos/bookbot/books/frankenstein.txt") as f:
		file_contents = f.read()

	return file_contents


if __name__ == "__main__":
	# print(get_book_text())
	print(words_counter(get_book_text()))

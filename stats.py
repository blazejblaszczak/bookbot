def words_counter(book):
	num_words = len(book.split())

	return f'{num_words} words found in the document'

if __name__ == "__main__":
	print(words_counter())

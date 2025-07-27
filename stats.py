def words_counter(book):
	num_words = len(book.split())

	return f'{num_words} words found in the document'


def character_counter(book):
	lower_book = book.lower()
	unique_chars = set(lower_book)
	count_dict = {}
	for c in unique_chars:
		char_count = lower_book.count(c)
		count_dict[c] = char_count

	return count_dict



if __name__ == "__main__":
	# print(words_counter())
	test_text = 'BaNAna'
	print(character_counter(test_text))

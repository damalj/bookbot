
import re
from stats import count_words, char_counts

def get_book_text(filepath: str) -> str:
	"""Return the contents of the file at `filepath` as a string.

	Raises FileNotFoundError if the file does not exist. Other IOErrors
	will propagate to the caller.
	"""
	with open(filepath, "r", encoding="utf-8") as f:
		return f.read()



if __name__ == "__main__":
	# Quick demo: try to read `books/frankenstein.txt` if available
	try:
		text = get_book_text("books/frankenstein.txt")
		# print(f"Read {len(text)} characters from books/frankenstein.txt")
		print(f"Found {count_words(text)} total words")
		print(char_counts(text))
	except FileNotFoundError:
		print("books/frankenstein.txt not found; demo skipped")
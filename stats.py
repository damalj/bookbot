def count_words(text: str) -> int:
	"""Return the number of words in `text`.

	"""
	if not text:
		return 0
	# Split on any whitespace to approximate word boundaries.
	return len(text.split())


def char_counts(text: str) -> dict[str, int]:
	"""Return a dictionary mapping each character to its occurrence count.

	The function lowercases the input text first, then counts every
	character (including spaces and punctuation). Returns an empty
	dictionary for empty input.
	"""
	if not text:
		return {}
	text = text.lower()
	counts: dict[str, int] = {}
	for ch in text:
		counts[ch] = counts.get(ch, 0) + 1
	return counts
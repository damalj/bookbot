def count_words(text: str) -> int:
	"""Return the number of words in `text`.

	"""
	if not text:
		return 0
	# Split on any whitespace to approximate word boundaries.
	return len(text.split())
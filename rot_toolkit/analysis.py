import string

ENGLISH_FREQ = {
    'e': 12.7, 't': 9.1, 'a': 8.2, 'o': 7.5,
    'i': 7.0, 'n': 6.7, 's': 6.3, 'h': 6.1, 'r': 6.0
}

COMMON_WORDS = ["the", "and", "is", "to", "of"]


def score_text(text):
    text = text.lower()

    # Common words score
    word_score = sum(word in text for word in COMMON_WORDS)

    # Valid characters ratio
    valid_chars = sum(c.isalpha() or c.isspace() for c in text)
    ratio_score = valid_chars / max(len(text), 1)

    # Frequency score
    freq_score = 0
    for char, expected in ENGLISH_FREQ.items():
        observed = text.count(char) / max(len(text), 1) * 100
        freq_score += max(0, 1 - abs(observed - expected) / 100)

    return word_score * 2 + ratio_score + freq_score


def analyze_text(text):
    from .core import rot_process

    results = []

    for shift in range(1, 26):
        decrypted = rot_process(text, -shift)
        score = score_text(decrypted)
        results.append((shift, decrypted, score))

    results.sort(key=lambda x: x[2], reverse=True)
    return results
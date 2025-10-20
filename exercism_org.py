"""From https://exercism.org"""


def find_anagram(target: str, candidate_words: list[str]) -> list[str]:
    """From https://exercism.org/tracks/python/exercises/anagram"""
    anagram_words = []

    for candidate in candidate_words:
        if sorted(candidate.lower()) == sorted(target) and candidate.lower() != target.lower():
            anagram_words.append(candidate)

    return anagram_words


if __name__ == "__main__":
    print(find_anagram("stone", ["stone", "tones", "banana", "tons", "notes", "Seton"]))

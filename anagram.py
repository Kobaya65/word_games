"""From https://exercism.org/tracks/python/exercises/anagram"""


def main() -> None:
    """Main function of that module."""
    target = "stone"
    candidate_words = ["stone", "tones", "banana", "tons", "notes", "Seton"]
    anagram_words = []

    for candidate in candidate_words:
        if sorted(candidate.lower()) == sorted(target) and candidate.lower() != target.lower():
            anagram_words.append(candidate)

    print(anagram_words)


if __name__ == "__main__":
    main()

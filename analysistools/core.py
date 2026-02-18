import argparse

def read_file(file):
    """
    Read the contents of a text file.

    Args:
        file (str): Path to the text file.

    Returns:
        str: The full contents of the file as a string.
    """
    f = open(file, "r")
    read_f = f.read()
    f.close()
    return read_f


def split_text_into_words(text):
    """
    Split a string of text into a list of words.

    Args:
        text (str): A string of text.

    Returns:
        list: A list of word strings.
    """
    t = text.split()
    return t


def split_text_into_sentences(text):
    """
    Split a string of text into a list of sentences.

    Args:
        text (str): A string of text.

    Returns:
        list: A list of sentence strings, split on '.', '!', or '?'.
    """
    for punct in ['.', '!', '?']:
        text = text.replace(punct, punct + '|')
    sentences = [s.strip() for s in text.split('|') if s.strip()]
    return sentences


def get_capital_words(words):
    """
    Count the occurrences of capitalized words in a list of words.

    Args:
        words (list): A list of word strings.

    Returns:
        dict: A dictionary mapping capitalized words to their frequency counts.
    """
    counter = {}
    capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for word in words:
        if word[0] in capital:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
    return counter


def print_word_counts(counts):
    """
    Print a dictionary of word counts.

    Args:
        counts (dict): A dictionary mapping words to their frequency counts.

    Returns:
        None
    """
    print(counts)


def main():
    parser = argparse.ArgumentParser(description="Count capitalized words in a file")
    parser.add_argument("filename", help="Path to the text file")
    parser.add_argument("--top", type=int, help="Only show the top N words")
    parser.add_argument("--sentences", action="store_true", help="Print sentences instead of word counts")
    args = parser.parse_args()

    text = read_file(args.filename)

    if args.sentences:
        sentences = split_text_into_sentences(text)
        for sentence in sentences:
            print(sentence)
    else:
        words = split_text_into_words(text)
        counts = get_capital_words(words)

        if args.top:
            counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True)[:args.top])

        print_word_counts(counts)

if __name__ == "__main__":
    main()
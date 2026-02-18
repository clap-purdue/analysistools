

def compute_ttr(words):
    """
    Compute the Type-Token Ratio (TTR) from a list of words.

    TTR = types / tokens

    Args:
        words (list): A list of word strings.

    Returns:
        float: The TTR score, a value between 0 and 1 where higher
               values indicate greater lexical diversity.
    """
    types = set(words)
    tokens = len(words)
    return len(types) / tokens


def compute_rttr(words):
    """
    Compute the Root Type-Token Ratio (RTTR) from a list of words.

    RTTR = types / sqrt(tokens)

    Args:
        words (list): A list of word strings.

    Returns:
        float: The RTTR score, where higher values indicate greater
               lexical diversity. Less sensitive to text length than TTR.
    """
    types = set(words)
    tokens = len(words)
    return len(types) / (tokens ** 0.5)
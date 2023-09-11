import string
from collections import Counter
from pathlib import Path


def main(filename: str) -> None:

    txt = Path(filename).read_text()
    words: list[str] = list()

    for line in txt.split("\n"):
        for s in string.punctuation:  # !"#$%&\'()*+,-./:;<=>?@[\\]^_‘{|}~
            line = line.replace(s, " ")
        words += line.lower().split()

    counts = Counter(words)
    print(counts.most_common(10))


if __name__ == "__main__":
    main("data/lorem_ipsum.txt")

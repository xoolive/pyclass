import string
from pathlib import Path


def main(filename: str) -> None:

    txt = Path(filename).read_text()
    counts: dict[str, int] = dict()

    for line in txt.split("\n"):
        for s in string.punctuation:  # !"#$%&\'()*+,-./:;<=>?@[\\]^_‘{|}~
            line = line.replace(s, " ")
        for word in line.lower().split():
            if word in counts.keys():
                counts[word] += 1
            else:
                counts[word] = 1

    count_generator = ((value, key) for key, value in counts.items())
    for value, key in sorted(count_generator, reverse=True)[:10]:
        print("{}: {}".format(key, value))


if __name__ == "__main__":
    main("data/lorem_ipsum.txt")

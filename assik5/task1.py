import string
from collections import Counter

def analyze():
    with open("text.txt", "r") as f:
        line = f.readlines()
    text = "".join(line)
    for char in string.punctuation:
        text = text.replace(char, "")
    words = text.split()
    frequency = Counter(words)
    with open("analysis.txt", "w") as f:
        f.write(f"Total lines: {len(line)}\n")
        f.write(f"Total words: {len(words)}\n\n")
        f.write("Word frequencies:\n")
        for word, count in frequency.items():
            f.write(f"{word}: {count}\n")

if __name__ == "__main__":
    analyze()
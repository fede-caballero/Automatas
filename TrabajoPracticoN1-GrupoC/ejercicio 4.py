import re

def analyze_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    text_without_punctuation = re.sub(r"[^\w\s]", "", text)
    unique_words = set()
    words = text_without_punctuation.lower().split()
    total_words = len(words)

    for word in words:
        unique_words.add(word)

    max_count = 0
    most_common_word = ""

    for word in unique_words:
        count = words.count(word)
        if count > max_count:
            max_count = count
            most_common_word = word
    print(f"The amount of words is: {total_words}")
    return most_common_word, max_count


file_path = "./Archivos_Texto/texto.txt"
most_common_word, count = analyze_text(file_path)

print(f"The most common word is '{most_common_word}' with {count} occurrences.")

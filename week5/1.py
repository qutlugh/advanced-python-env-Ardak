import string
from collections import Counter

def analyze_text_file(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()

        total_lines = len(lines)
        
        full_text = " ".join(lines)
        translator = str.maketrans('', '', string.punctuation)
        clean_text = full_text.translate(translator).lower()
        
        words = clean_text.split()
        total_words = len(words)
        word_freq = Counter(words)

        with open(output_file, 'w') as f:
            f.write(f"Total Lines: {total_lines}\n")
            f.write(f"Total Words: {total_words}\n")
            f.write("Word Frequencies:\n")
            for word, count in word_freq.items():
                f.write(f"{word}: {count}\n")
                
        print(f"Task 1 Complete. Results saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")

analyze_text_file("text.txt", "analysis.txt")
import string

def create_sample_file(filename):
    """Create a small practice text file."""
    sample_text = """Hello world! This is a sample text.
    This text is for testing: hello, HELLO, and more hello."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(sample_text)

def read_and_count_words(filename):
    """Read file, normalize text, and count word frequencies."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}

    # Normalize: lowercase and remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split into words
    words = text.split()

    # Count word frequencies
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq

if __name__ == "__main__":
    filename = "practice.txt"
    create_sample_file(filename)  # Create a sample file
    frequencies = read_and_count_words(filename)

    # Print the dictionary
    print("Word Frequencies:")
    for word, count in frequencies.items():
        print(f"{word}: {count}")

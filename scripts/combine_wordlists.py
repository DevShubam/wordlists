import os

def combine_wordlists(input_files, output_file):
    """
    Combines multiple TXT word list files into a single file.

    - Ensures all words are lowercase.
    - Removes duplicate words.
    - Strips non-ASCII characters.
    - Sorts words alphabetically.

    Args:
        input_files (list): List of input file paths.
        output_file (str): Path to the output file.
    """
    combined_words = set()

    # Read words from all input files
    for file in input_files:
        if os.path.exists(file):
            with open(file, "r", encoding="utf-8") as f:
                for line in f:
                    # Clean each word
                    word = line.strip().lower()
                    # Remove non-alphanumeric characters (if needed)
                    word = "".join(c for c in word if c.isalnum())
                    if word:
                        combined_words.add(word)
        else:
            print(f"File not found: {file}")

    # Sort the words alphabetically
    sorted_words = sorted(combined_words)

    # Write to the output file
    with open(output_file, "w", encoding="utf-8") as f:
        for word in sorted_words:
            f.write(word + "\n")

    print(f"Combined wordlist saved to: {output_file}")

# usage
if __name__ == "__main__":
    # List of input wordlist files
    input_files = ["wordlist1.txt", "wordlist2.txt"]

    # Output file
    output_file = "combined_wordlist.txt"

    # Combine the wordlists
    combine_wordlists(input_files, output_file)

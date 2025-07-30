# Write a Python program to count the frequency of words in a file.

def word_frequency(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().lower()
            
        # Remove punctuation and split into words
        import string
        translator = str.maketrans('', '', string.punctuation)
        words = content.translate(translator).split()
        
        # Count word frequency
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1
            
        return frequency
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

# Example usage:
# freq = word_frequency('sample.txt')
# print("Word frequencies:")
# for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
#     print(f"{word}: {count}")

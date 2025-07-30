# Write a Python program to find the longest words.

def find_longest_words(filename, num_words=1):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
            
        if not words:
            print("The file is empty.")
            return []
            
        # Sort words by length in descending order
        words.sort(key=len, reverse=True)
        
        # Get the longest word(s)
        max_length = len(words[0])
        longest_words = [word for word in words if len(word) == max_length]
        
        # If we want more than one longest word
        if num_words > 1:
            words = sorted(list(set(words)), key=len, reverse=True)
            return words[:num_words]
            
        return list(set(longest_words))  # Remove duplicates
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage:
# longest = find_longest_words('sample.txt')
# print("Longest word(s):", longest)
# top5 = find_longest_words('sample.txt', 5)
# print("Top 5 longest words:", top5)

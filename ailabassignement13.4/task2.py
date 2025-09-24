# Function to join words into a sentence
def make_sentence(words):
    sentence = ""
    for word in words:
        sentence += word + " "
    return sentence.strip()  # remove trailing space

# Example usage
words = ["AI", "helps", "in", "refactoring", "code"]
result = make_sentence(words)
print(result)
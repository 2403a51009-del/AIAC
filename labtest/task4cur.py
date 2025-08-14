import string

def preprocess_text(text):
    # Define a simple list of English stop words
    stop_words = set([
        'a', 'an', 'the', 'and', 'or', 'but', 'if', 'while', 'with', 'to', 'of', 'at', 'by', 'for', 'from', 'in', 'on', 'off', 'out', 'over', 'under', 'as', 'is', 'it', 'this', 'that', 'these', 'those', 'he', 'she', 'they', 'we', 'you', 'i', 'me', 'him', 'her', 'them', 'us', 'my', 'your', 'his', 'their', 'our', 'its', 'be', 'am', 'are', 'was', 'were', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'shall', 'should', 'can', 'could', 'may', 'might', 'must'
    ])
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert to lowercase
    text = text.lower()
    # Remove stop words
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

# Read input from the console
input_text = input("Enter text: ")
processed_text = preprocess_text(input_text)
print("Processed text:", processed_text)

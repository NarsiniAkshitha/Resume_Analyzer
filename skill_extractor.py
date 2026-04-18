import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Initialize
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()


# Load skills from dataset file

def load_skills(file_path="skills.txt"):
    with open(file_path, "r") as file:
        skills = [line.strip().lower() for line in file]
    return skills

# Extract skills

def extract_skills(text):
    text = text.lower()

    # Load skills dynamically
    skills = load_skills()

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stopwords
    filtered_tokens = [word for word in tokens if word not in stop_words]

    # Stemming
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

    found_skills = []

    # Match skills
    for skill in skills:
        if " " in skill:
            # Multi-word skill
            if skill in text:
                found_skills.append(skill)
        else:
            # Single-word skill (use stemming)
            if stemmer.stem(skill) in stemmed_tokens:
                found_skills.append(skill)

    return list(set(found_skills))
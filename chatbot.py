from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
pairs = []
questions = []
answers = []

with open("data.txt", "r") as f:
    for line in f:
        if "|" in line:
            q, a = line.strip().split("|")
            questions.append(q)
            answers.append(a)

# TF-IDF on questions ONLY
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def get_response(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)

    idx = similarity.argmax()
    score = similarity[0][idx]

    if score < 0.3:
        return "Sorry, I didn't understand that."

    return answers[idx]   # 🔥 FIX: return answer
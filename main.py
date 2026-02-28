import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample resumes and job description data (you can replace it with your data)
data = {
    'resume_id': [1, 2, 3],
    'resume_text': [
        "Experienced data scientist with skills in Python, machine learning, and data analysis.",
        "Software developer with expertise in Java, cloud computing, and project management.",
        "Data analyst with proficiency in SQL, Python, and data visualization."
    ]
}

job_description = "Looking for a data scientist skilled in Python, machine learning, SQL, and data analysis."

df = pd.DataFrame(data)
print("Resumes:\n", df)

documents = df['resume_text'].tolist()
documents.append(job_description)

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)

similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

df['similarity_score'] = similarity_scores
print("\nResume similarity Scores: \n", df[['resume_id', "similarity_score"]])

thresold = 0.2
matching_resumes = df[df['similarity_score'] >= thresold]
print("\nResumes matching the job requirements:\n", matching_resumes[['resume_id', 'similarity_score']])
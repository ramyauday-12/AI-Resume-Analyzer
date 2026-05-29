# List of predefined skills
# Later we can store in database/API
skills_list = [

    "python",
    "java",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "streamlit",
    "power bi",
    "machine learning",
    "ai",
    "nlp",
    "git"
]


# Function to extract skills
def extract_skills(text):

    # Convert all text to lowercase
    # Makes matching easier
    text = text.lower()

    # Empty list to store found skills
    found_skills = []

    # Check each skill
    for skill in skills_list:

        # If skill exists in resume text
        if skill in text:

            # Add skill to list
            found_skills.append(skill)

    # Return detected skills
    return found_skills
# Function to compare resume and JD skills
def compare_skills(resume_skills, jd_skills):

    # Convert list into set
    # Sets make comparison easier
    resume_set = set(resume_skills)

    jd_set = set(jd_skills)


    # Find common skills
    matched_skills = resume_set.intersection(
        jd_set
    )


    # Find skills present in JD
    # but absent in resume
    missing_skills = jd_set - resume_set


    # Match percentage formula
    if len(jd_set) > 0:

        match_percentage = (
            len(matched_skills)
            / len(jd_set)
        ) * 100

    else:

        match_percentage = 0


    return (
        matched_skills,
        missing_skills,
        match_percentage
    )
# Generate suggestions
def suggest_improvements(missing_skills):

    suggestions = []

    # Create suggestion for each skill
    for skill in missing_skills:

        suggestions.append(
            f"Add projects or experience related to {skill}"
        )

    return suggestions
# Import NLP libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Function to compare text similarity
def calculate_similarity(
        resume_text,
        job_description
):

    # Store both texts
    text_data = [
        resume_text,
        job_description
    ]

    # Convert text into numbers
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        text_data
    )

    # Calculate similarity score
    similarity = cosine_similarity(
        vectors
    )

    # Return percentage
    return similarity[0][1] * 100
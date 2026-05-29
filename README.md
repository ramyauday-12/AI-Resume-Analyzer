# AI Resume Analyzer + Job Matcher

An AI-powered Resume Analyzer built using Python and Streamlit that compares resumes with Job Descriptions (JD), calculates ATS-style match scores, identifies missing skills, and provides improvement suggestions.

---

# Features

- Upload Resume PDF
- Extract text from PDF resumes
- Detect technical skills automatically
- Compare resume skills with Job Description
- Calculate Match Percentage
- NLP-based Resume-JD Similarity
- Identify Missing Skills
- Generate Improvement Suggestions
- Visualization Dashboard
- Downloadable Analysis Report

---

# Tech Stack

- Python
- Streamlit
- PyPDF2
- scikit-learn
- NLTK
- Matplotlib

---

# Project Structure

```bash
AI-Resume-Analyzer/
│
├── app.py
├── parser.py
├── skills.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# How It Works

1. User uploads a resume PDF
2. Resume text is extracted using PyPDF2
3. Skills are identified from resume and JD
4. Skills are compared
5. Match score is calculated
6. NLP similarity is calculated using TF-IDF and cosine similarity
7. Missing skills and suggestions are displayed
8. User can download the analysis report

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/AI-Resume-Analyzer.git
```

## Open Project Folder

```bash
cd AI-Resume-Analyzer
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Streamlit App

```bash
streamlit run app.py
```

---

# Sample Features

## Resume Analysis

- Skill Match Percentage
- Resume-JD Similarity
- Missing Skills Detection
- Improvement Suggestions

## Visualization

- Progress Bars
- Bar Chart Comparison

## Report Generation

- Download ATS-style analysis report

---

# Future Improvements

- ATS Resume Optimization
- DOCX Resume Generation
- AI Resume Rewriting
- Better Skill Extraction
- Resume Formatting Checker
- Cloud Deployment

---

# NLP Techniques Used

- TF-IDF Vectorization
- Cosine Similarity

---

# Screenshots

Add project screenshots here after deployment.

---

# Author

Ramya Udayakumar

---

# License

This project is developed for educational and portfolio purposes.
# Import Streamlit library for UI
import streamlit as st

# Import PDF extraction function
from parser import extract_text

# Import functions from skills.py
from skills import (
    extract_skills,
    compare_skills,
    suggest_improvements,
    calculate_similarity
)

# Import chart library
import matplotlib.pyplot as plt

import textwrap

# Sidebar
st.sidebar.title(
    "AI Resume Analyzer"
)

st.sidebar.write(
    "Upload your resume and compare it with a Job Description."
)

# Main page title
st.title(
    "Resume Analysis Dashboard"
)


# Upload Resume PDF
uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)


# Job Description input box
job_description = st.text_area(
    "Paste Job Description"
)


# Continue only if resume uploaded
if uploaded_file:

    # Extract text from PDF
    text = extract_text(uploaded_file)

    # Expandable section
    with st.expander(
        "View Extracted Resume Text"
    ):
        st.write(text)


    # Extract skills from resume
    resume_skills = extract_skills(text)


    # Continue only if JD entered
    if job_description:

        # Extract skills from JD
        jd_skills = extract_skills(
            job_description
        )


        # Create 2 columns
        col1, col2 = st.columns(2)


        # LEFT COLUMN
        with col1:

            st.subheader(
                "Detected Resume Skills"
            )

            for skill in resume_skills:

                st.success(skill)


        # RIGHT COLUMN
        with col2:

            st.subheader(
                "Job Description Skills"
            )

            for skill in jd_skills:

                st.info(skill)


        # Compare resume and JD skills
        matched, missing, score = compare_skills(
            resume_skills,
            jd_skills
        )


        # Match percentage heading
        st.subheader(
            "Match Percentage"
        )

        # Show score value
        st.write(
            f"{score:.2f}%"
        )

        # Create progress bar
        st.progress(
            int(score)
        )


        # Calculate NLP similarity
        similarity = calculate_similarity(
            text,
            job_description
        )


        # Similarity heading
        st.subheader(
            "Resume-JD Similarity"
        )

        # Display similarity %
        st.write(
            f"{similarity:.2f}%"
        )

        # Similarity progress bar
        st.progress(
            int(similarity)
        )


        # Chart section
        st.subheader(
            "Analysis Visualization"
        )


        # Graph labels
        labels = [
            "Skill Match",
            "Similarity"
        ]


        # Graph values
        values = [
            score,
            similarity
        ]


        # Create chart
        fig, ax = plt.subplots()


        # Create bar graph
        ax.bar(
            labels,
            values
        )


        # Y axis label
        ax.set_ylabel(
            "Percentage"
        )


        # Graph title
        ax.set_title(
            "Resume Analysis Score"
        )


        # Display chart
        st.pyplot(fig)


        # Create 2 columns
        col3, col4 = st.columns(2)


        # LEFT COLUMN
        with col3:

            st.subheader(
                "Matched Skills"
            )

            for skill in matched:

                st.success(skill)


        # RIGHT COLUMN
        with col4:

            st.subheader(
                "Missing Skills"
            )

            for skill in missing:

                st.error(skill)


        # Generate suggestions
        suggestions = suggest_improvements(
            missing
        )


        # Suggestions heading
        st.subheader(
            "Suggestions"
        )


        # Display suggestions
        for suggestion in suggestions:

            st.write(
                suggestion
            )
        
        # Create downloadable report
        report = (
            "====================================\n"
            "AI RESUME ANALYSIS REPORT\n"
            "====================================\n\n"

            f"MATCH PERCENTAGE:\n"
            f"{score:.2f}%\n\n"

            f"RESUME-JD SIMILARITY:\n"
            f"{similarity:.2f}%\n\n"

            "------------------------------------\n"
            "MATCHED SKILLS\n"
            "------------------------------------\n"
            f"{chr(10).join(matched)}\n\n"

            "------------------------------------\n"
            "MISSING SKILLS\n"
            "------------------------------------\n"
            f"{chr(10).join(missing)}\n\n"

            "------------------------------------\n"
            "SUGGESTIONS\n"
            "------------------------------------\n"
            f"{chr(10).join(suggestions)}\n\n"

            "====================================\n"
            "Generated using AI Resume Analyzer\n"
            "===================================="
        )


        # Download button
        st.download_button(

            label="Download Report",

            data=report,

            file_name="resume_analysis_report.txt",

            mime="text/plain"
        )
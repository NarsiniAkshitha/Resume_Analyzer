from  file_reader import extract_text_from_pdf, extract_text_from_txt
from skill_extractor import extract_skills
from matcher import match_skills
from matcher_tfidf import match_tfidf 
def main():
    print("=== Resume Analyzer & Job Matcher ===")

    resume_path = input("Enter resume file path: ").strip().strip('"')
    jd_path = input("Enter job description path: ").strip().strip('"')

    # Extract resume text
    if resume_path.endswith(".pdf"):
        resume_text = extract_text_from_pdf(resume_path)
    else:
        resume_text = extract_text_from_txt(resume_path)

    # Extract JD text
    jd_text = extract_text_from_txt(jd_path)

    # Extract skills
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(jd_text)

    # Match
    matched, missing, skill_score = match_skills(resume_skills, job_skills)

    print("Matched Skills:", matched)
    print("Missing Skills:", missing)
    print("Skill Match Score:", skill_score)

if __name__ == "__main__":
    main()
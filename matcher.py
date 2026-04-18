def match_skills(resume_skills, job_skills):
    matched = []
    missing = []

    for skill in resume_skills:
        if skill in job_skills:
            matched.append(skill)

    for skill in job_skills:
        if skill not in resume_skills:
            missing.append(skill)

    # Skill score
    if len(job_skills) > 0:
        skill_score = (len(matched) / len(job_skills)) * 100
    else:
        skill_score = 0

    return matched, missing, round(skill_score, 2)
            

        



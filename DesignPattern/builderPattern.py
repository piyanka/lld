class Resume:

    def __init__(self):
        self.name = None
        self.email = None
        self.education = None
        self.skills = None
        self.experience = None
        self.projects = None
        self.certifications = None
        self.social_links = None

    def __str__(self):
        return f"""
        Name : {self.name},
        Email: {self.email},
        Education: {self.education},
        Skills:  {self.skills},
        Experience: {self.experience},
        Projects: {self.projects},
        Certifications: {self.certifications},
        Social_links: {self.social_links} 
        """
    
class ResumeBuilder:

    def __init__(self):
        self.resume = Resume()

    def set_name(self, name):
        self.resume.name = name
        return self
    
    def set_email(self, email):
        self.resume.email = email
        return self
    
    def set_education(self, education):
        self.resume.education = education
        return self
    
    def set_skills(self, skills):
        self.resume.skills = skills
        return self
    
    def set_experience(self, experience):
        self.resume.experience = experience
        return self
    
    def set_projects(self, projects):
        self.resume.projects = projects
        return self
    
    def set_certifications(self, certifications):
        self.resume.certifications = certifications
        return self
    
    def set_social_links(self, social_links):
        self.resume.social_links = social_links
        return self
    
    def build(self):
        return self.resume 
    
builder = ResumeBuilder()

resume = (
    builder
    .set_name("Priyanka Kumari")
    .set_email("yadavpriyanka@gmail.com")
    .set_education("BTech in Electrical Engineering")
    .set_skills(["Python", "MERN"])
    .set_experience("Teaching assistant at Coding Ninja")
    .set_projects(["Student Progress Manager", "Tweetopia", "Moviemate"])
    .set_certifications(["expertice in DSA in Python", "Internship completion at coding ninja"])
    .set_social_links(["github.com/piyanka", "linkedin.com/yadavpriyanka"])
    .build()
)

print(resume)
    




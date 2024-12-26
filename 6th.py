import pandas as pd
import random
from faker import Faker

fake = Faker()

subjects = [
    "Marathi", "Urdu", "Hindi", "English", "History", "Science", "Geography", 
    "Drawing", "Sports", "Environmental Studies", "Math", "Computer"
]

career_map = {
    "Marathi": ["Media and Journalism", "Entertainment and Arts", "Literature and Education", "Government and Administrative Services"],
    "Urdu": ["Media and Journalism", "Entertainment and Arts", "Literature and Education", "Government and Administrative Services"],
    "Hindi": ["Media and Journalism", "Entertainment and Arts", "Literature and Education", "Government and Administrative Services"],
    "English": ["Media and Journalism", "Entertainment and Arts", "Literature and Education", "Government and Administrative Services", "Corporate and Business Communication"],
    "History": ["Historian", "Archaeologist", "Museum Professional", "Cultural Heritage Manager", "Genealogist", "Documentary Filmmaker"],
    "Science": ["Healthcare and Medicine", "Research and Development", "Agriculture and Food Sciences", "Education and Academia", "Allied Healthcare Professions", "Interdisciplinary Fields"],
    "Geography": ["Urban and Regional Planner", "Environmental Consultant", "Cartographer", "Geospatial Analyst", "Meteorologist", "Geologist", "Disaster Management Specialist", "Archaeologist", "Geographic Information Systems (GIS) Specialist", "Geotechnical Engineer"],
    "Drawing": ["Fine Artist", "Graphic Designer", "Concept Artist", "Animator", "Fashion Designer", "Comic Artist/Cartoonist", "Product Designer", "Architect", "Storyboard Artist", "Set Designer/Illustrator for Theatre or Film", "Visual Development Artist", "3D Artist"],
    "Sports": ["Professional Athlete", "Sports Coach", "Sports Nutritionist/Dietitian", "Physical Therapist", "Fitness Trainer"],
    "Environmental Studies": ["Environmental Scientist"],
    "Math": ["Engineering", "Research and Development (R&D)", "Mathematics and Actuarial Science", "Architecture", "Aviation and Aerospace", "Finance and Investment"],
    "Computer": ["Software Developer", "Artificial Intelligence (AI) / Machine Learning Engineer"]
}

rows = []
num_rows = 10000  
for _ in range(num_rows):
    
    interests = {subject: random.randint(20, 80) for subject in subjects}  
    top_subject = max(interests, key=interests.get)  
    recommended_careers = career_map[top_subject]

    recommended_career = random.choice(recommended_careers)
    
    math_computer_relation = abs(interests["Math"] - interests["Computer"])

    grade = 6

    row = {**interests, "Interest": top_subject, "Recommended Career": recommended_career, 
    }
    rows.append(row)

df = pd.DataFrame(rows)

df.to_csv("6th_student_interest_career.csv", index=False)

print("Dataset created and saved as '6th_standard_student_interest_career.csv'")

import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Define subjects and corresponding careers
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

# Generate dataset
rows = []
num_rows = 100000

for _ in range(num_rows):
    interests = {subject: random.randint(1, 100) for subject in subjects}  # Marks between 1 and 100
    top_subject = max(interests, key=interests.get)  # Subject with highest interest
    recommended_careers = career_map[top_subject]

    # Randomly pick a career from the possible careers
    recommended_career = random.choice(recommended_careers)

    # Add row without Student ID column
    row = {**interests, "Interest": top_subject, "Recommended Career": recommended_career}
    rows.append(row)

# Convert to DataFrame
df = pd.DataFrame(rows)

# Save to CSV
df.to_csv("student_interest_career.csv", index=False)

print("Dataset created and saved as 'DG.csv'")


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
num_rows = 10000  # Dataset size for 7th-grade students

for _ in range(num_rows):
    # Generate marks for each subject with slightly higher values than 6th-grade
    interests = {subject: random.randint(30, 90) for subject in subjects}  # Marks between 30 and 90
    top_subject = max(interests, key=interests.get)  # Subject with highest interest
    recommended_careers = career_map[top_subject]

    # Randomly pick a career from the possible careers
    recommended_career = random.choice(recommended_careers)
    
    # Calculate relationship between Math and Computer interests
    math_computer_relation = abs(interests["Math"] - interests["Computer"])

    # Assign Grade as 7
    grade = 7

    # Add row with Grade and Math-Computer relation
    row = {**interests, "Interest": top_subject, "Recommended Career": recommended_career
            }
    rows.append(row)

# Convert to DataFrame
df_7th_std = pd.DataFrame(rows)

# Save to CSV
file_path = "7th_standard_student_interest_career.csv"
df_7th_std.to_csv(file_path, index=False)

print(f"Dataset saved to {file_path}")

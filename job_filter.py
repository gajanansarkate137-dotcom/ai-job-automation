import json

# Load job data
with open("jobs.json", "r") as file:
    jobs = json.load(file)

# Our target locations
target_locations = ["Pune", "Pimpri-Chinchwad"]

# Our target roles
target_roles = ["Data Analyst", "Junior Data Analyst", "Data Analyst Intern", "Business Analyst"]

# Filter jobs
filtered_jobs = []

for job in jobs:
    if job["location"] in target_locations:
        if job["title"] in target_roles:
            filtered_jobs.append(job)

# Show matching jobs
print("Matching Jobs:")
print("----------------")

for job in filtered_jobs:
    print(f"Job: {job['title']}")
    print(f"Company: {job['company']}")
    print(f"Location: {job['location']}")
    print(f"Apply: {job['url']}")
    print("----------------")

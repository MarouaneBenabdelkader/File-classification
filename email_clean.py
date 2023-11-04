import os
import re

# Function to clean email but preserve periods


def clean_email(email):
    return re.sub(r'[\s,-]', '', email).lower()

# Function to create directory and write emails


# Read the emails from file
with open('emails_file.txt', 'r', encoding='utf-8') as file:
    # Assuming emails are separated by a space or some other delimiter
    email_data = file.read()
    emails = email_data.split()  # This will split the emails on whitespace

# Process each email
department_emails = {}
for email in emails:
    email = clean_email(email)
    if '@' in email:  # Simple check to ensure email is valid
        # Get the department name, ensuring periods are not removed
        department = email.split('@')[1].split('.')[0]
        if department not in department_emails:
            department_emails[department] = []
        department_emails[department].append(email)


def write_emails_to_file(department, emails):
    directory = f"c:/users/Marouane/Documents/python tps/Tp3_python/emails/{department}"
    os.makedirs(directory, exist_ok=True)
    with open(f"{directory}/emails.txt", "w", encoding="utf-8") as f:
        for email in emails:
            f.write(email + "\n")


# Create directories and write emails
for department, emails in department_emails.items():
    write_emails_to_file(department, emails)

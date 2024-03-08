import csv
from mail_utils import send_email, init_config

mail_subect = "Invitation to the QPE Assistant Beta Program!"
mail_list_file = r".\mail_lists\QSD QSP Trainer List.csv"
#mail_list_file = r".\mail_lists\dev_team.csv"
html_file      = r".\messages\intro_to_trainers2.html"


with open(html_file, 'r', encoding='utf-8') as file:
    html_message = file.read()

# Open the existing CSV file for reading
with open(mail_list_file, 'r') as file:
    init_config()

    reader = csv.reader(file)
    next(reader)  # Skip the header row

    # Create a dictionary to store the names and email addresses
    data = {}
    for row in reader:
        first_name = row[1]
        last_name = row[2]
        email = row[3]
        
        data[email] = {"first_name": first_name, "last_name": last_name}        
        print(f"First Name: {first_name} Last Name: {last_name} Email: {email}")
        salutation = f"Hi there {first_name},<br>"
        print(salutation)
        send_email(mail_subect,"john.price@digamesystems.com", email, salutation + html_message)

    
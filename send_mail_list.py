import csv

from mail_utils import send_email, init_config

mail_subject = "Invitation to the QPE Assistant Beta Program!"
mail_list_file = r".\mail_lists\Los_Angeles_90012.csv"
#mail_list_file = r".\mail_lists\dev_team.csv"
html_file      = r".\messages\intro_message.html"

with open(html_file, 'r', encoding="utf8") as file:
    # Read the content of the file and assign it to a variable
    html_message = file.read()

# Open the existing CSV file for reading
with open(mail_list_file, 'r') as file:
    init_config()

    reader = csv.reader(file)
    next(reader)  # Skip the header row

    # Create a dictionary to store the names and email addresses
    data = {}
    for row in reader:
        name = row[0]
        email = row[1]
        full_name = name.split(",")
        if len(full_name) == 2:
            first_name = full_name[1]
            last_name = full_name[0]
        else:
            first_name = full_name[0]
            last_name = ""
        
        data[email] = {"first_name": first_name, "last_name": last_name}        
        print(f"First Name: {first_name} Last Name: {last_name} Email: {email}")
        salutation = f"Hi there, {first_name} {last_name},<br>"
        send_email(mail_subject,"john.price@digamesystems.com", email, salutation + html_message)


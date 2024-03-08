import csv

# Take the existing CSV file and create a new CSV file with only the names and email addresses

existing_file = r".\mail_lists\Master_Los_Angeles_90012.csv"
new_file      = r".\mail_lists\Los_Angeles_90012.csv"

# Open the existing CSV file for reading
with open(existing_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    # Create a dictionary to store the names and email addresses
    data = {}
    for row in reader:
        if (row[0].strip('"')) != '':
            name = row[0].strip('"')
        address = row[1]
        if '@' in address:  # Check if the address contains '@' to identify email addresses
            data[name] = address

# Open a new CSV file for writing
with open(new_file, 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Name', 'Email'])

    # Write the data rows
    for name, email in data.items():
        writer.writerow([name, email])
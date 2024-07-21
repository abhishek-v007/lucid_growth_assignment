import csv

# Define the relevant services
relevant_services = [
    'mass email', 'bulk email', 'high volume email sending', 
    'email blast services', 'Mail Transfer Agent', 'MTA configuration', 
    'MTA management', 'email system administration', 'email marketing', 
    'email infrastructure', 'email system assessment', 'email monitoring'
]

# Load the CSV file
with open('competitor.csv', mode='r', encoding='utf-8') as infile:
    csv_reader = csv.reader(infile)
    # Extract the column names
    headers = next(csv_reader)[1:]
    
    # Initialize a list to hold filtered company data
    filtered_companies = [headers]

    # Filter the companies based on relevant services
    for row in csv_reader:
        description = row[2]
        if any(service in description for service in relevant_services):
            filtered_companies.append(row[1:])

# Save the filtered companies to a new CSV file
with open('filtered_companies.csv', mode='w', newline='', encoding='utf-8') as outfile:
    csv_writer = csv.writer(outfile)
    csv_writer.writerows(filtered_companies)

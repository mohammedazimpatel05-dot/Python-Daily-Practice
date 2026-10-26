import csv

headers = ['Name', 'Age', 'City']
rows = [
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# Open file with newline='' to prevent blank rows
with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    
    # Write a single row (the header)
    writer.writerow(headers)
    
    # Write multiple rows at once
    writer.writerows(rows)
  

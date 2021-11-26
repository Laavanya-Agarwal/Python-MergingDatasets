import csv

# READING DATASET AND ADDING TO DATA VARIABLE
data = []
with open ("dataset_2.csv", "r") as x:
    csv_reader = csv.reader(x)
    for row in csv_reader:
        data.append(row)

# GETTING SPECIFIC ROWS FROM DATA VARIABLE
headers = data[0]
planet_data = data[1:]

# CONVERTING PL_NAME TO LOWERCASE
for row in planet_data:
    row[2] = row[2].lower()

# SORTING PL_NAME ALPHABETICALLY
planet_data.sort(key=lambda planet_data:planet_data[2])

# CREATING NEW DATASET - can add more to it
with open ("dataset_2_sorted.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)
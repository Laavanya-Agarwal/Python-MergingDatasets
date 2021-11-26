import csv

# READING DATASET1 AND ADDING TO DATA VARIABLE
dataset1 = []
with open ("dataset_1.csv", "r") as x:
    csv_reader = csv.reader(x)
    for row in csv_reader:
        dataset1.append(row)

# READING DATASET2 AND ADDING TO DATA VARIABLE
dataset2 = []
with open ("dataset_2_sorted.csv", "r") as x:
    csv_reader = csv.reader(x)
    for row in csv_reader:
        dataset2.append(row)

# GETTING SPECIFIC ROWS FROM DATA VARIABLES
headers1 = dataset1[0]
headers2 = dataset2[0]
planet_data1 = dataset1[1:]
planet_data2 = dataset2[1:]

# MERGING HEADERS
headers = headers1 + headers2

# MERING PLANET_DATAS
planet_datas = []
for index, datarows in enumerate(planet_data1):
    planet_datas.append(planet_data1[index] + planet_data2[index])

# CREATING CSV FILE FOR FINAL MERGING - can add more to it
with open ("datasets_merged.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_datas)
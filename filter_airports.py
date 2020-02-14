import csv

BANNED_COUNTRIES = ['China', 'North Korea']

intl_airports = {}

with open('intl_airports.csv') as csvfile:
    reader = csv.reader(csvfile)
    for _, _, code in reader:
        intl_airports[code] = True

filtered_rows = []

with open('airports.dat') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        country = row[3]
        code = row[4]
        if code in intl_airports and not country in BANNED_COUNTRIES:
            filtered_rows.append(row)

with open('filtered_airports.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(filtered_rows)

import csv

with open('financial.csv' , 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

#    for line in csv_reader:
#        print(line[0:5])

    with open ('new_financial.csv' , 'w') as new_file:
        csv_writer= csv.writer(new_file, delimiter ="\t")

        for line in (csv_reader):
            csv_writer.writerow(line)
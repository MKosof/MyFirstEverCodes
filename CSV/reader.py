import csv


#reading only line 0
with open('financial.csv' , 'r+') as csv_file:
    csv_reader = csv.reader(csv_file)
    for index,line in enumerate(csv_reader):
        if index ==0:
            temp=line[0:2]
        else:
            break
    print (temp)

#reading all lines
#    for line in csv_reader:
#        print(line[0:5])
#writing lines
#    with open ('new_financial.csv' , 'w') as new_file:
#        csv_writer= csv.DictWriter(new_file, delimiter ="\t")
#
#        for line in (csv_reader):
#            csv_writer.writerow(line)
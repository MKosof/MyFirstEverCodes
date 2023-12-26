import csv

with open ('financial.csv','r') as csv_file:
    csv_reader=csv.DictReader(csv_file)

#    for line in csv_reader:
#        print(line['Industry_name_NZSIOC'])


#removed year from fieldnames as i delete it afterwards as a test
    with open ('new_financial_dict.csv' , 'w') as new_file:
        fieldnames =['Industry_aggregation_NZSIOC','Industry_code_NZSIOC','Industry_name_NZSIOC','Units','Variable_code','Variable_name','Variable_category','Value','Industry_code_ANZSIC06']
        csv_writer= csv.DictWriter(new_file, fieldnames=fieldnames  ,delimiter ="\t")
        csv_writer.writeheader()

        for line in (csv_reader):
            del line['Year']
            csv_writer.writerow(line)
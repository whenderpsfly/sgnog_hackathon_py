import csv

with open('master.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    prefix_dict = {}
    final_dict = {}

    x = input("What is your prefix: " )

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            

        if row["Prefix"] == x:
            prefix_dict[row["Carrier"]] = row["Rate"]
            what_prefix = row["Prefix"]     

        line_count += 1

        print(row["Prefix"])
    
    
    carrier_ordered2 = sorted(prefix_dict.items(), key=lambda x:x[1])
    
    final_dict[what_prefix] = carrier_ordered2
    
    # print(final_dict)

    print(f'Processed {line_count} lines.')

    print("Your prefix is: " + str(list(final_dict.keys())))
    print("and your options are: " + str(list(final_dict.values()))     )
    print("The cheapest option is: " + str(  final_dict.get(what_prefix)[0]   ))


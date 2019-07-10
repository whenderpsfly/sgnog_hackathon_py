import csv
import operator
from operator import itemgetter 

process_list = []
prefix_set = {""}
each_prefix_list=[]

def ranked_similar(prefix_to_check):
    input_file =csv.DictReader(open('master.csv', mode='r'))
    for row in input_file:
        if row["Prefix"].startswith(prefix_to_check):
            prefix_set.add(row["Prefix"])
            process_list.append( tuple((row["Prefix"] ,row["Carrier"], row["Rate"] )))

    prefix_set.remove("")
    
    for prefix in prefix_set:
        each_prefix_list=list(filter( lambda x: x[0]==prefix , process_list))
        each_prefix_list.sort(key=lambda tup : tup[2])
        print_carrier_rate = list(map(itemgetter(1,2), each_prefix_list)) 
        print("The ranked rate for " , prefix , " is: " , str(print_carrier_rate))
        each_prefix_list.clear()

def ranked_exact(prefix_to_check):
    input_file =csv.DictReader(open('master.csv', mode='r'))
    process_list.clear()
    for row in input_file:
        if row["Prefix"] == prefix_to_check:
            #print("entering")
            process_list.append( tuple((row["Prefix"] ,row["Carrier"], row["Rate"] )))
        #print(process_list)
    process_list.sort(key=lambda tup : tup[2])
    print_carrier_rate = list(map(itemgetter(1,2), process_list)) 
    print("The ranked rate for " , prefix_to_check , " is: " , str(print_carrier_rate))

prefix_to_check = input("What is your prefix: " )

print("Similar prefixes: ")
ranked_similar(prefix_to_check)

print("\n\n\nExact prefixes: ")
ranked_exact(prefix_to_check)
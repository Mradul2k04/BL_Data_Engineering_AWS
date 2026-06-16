# MAPPER CODE 
import  sys
import csv


reader = csv.reader(sys.stdin)

next(reader)

for row in reader:
    status = row[1]
    print(f"{status}\t1")


#REDUCER CODE
current_key= None
count=0

for line in sys.stdin:
    key,value = line.strip().split("\t")
    value = int(value)

    if current_key == key:
        count += value
    else:
        if current_key:
            print(f"{current_key}\t {count}")

        current_key=key
        count = value

if current_key:
    print(f"{current_key}\t{count}")
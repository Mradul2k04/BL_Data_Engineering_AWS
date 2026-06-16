# MAPPER CODE 
#!/usr/bin/env python3

import sys
import csv

reader = csv.reader(sys.stdin)

next(reader)

for row in reader:
    region = row[1]
    days = int(row[2])

    print(f"{region}\t{days}")


# REDUCER CODE
#!/usr/bin/env python3

import sys

current_region = None
current_sum = 0

# Input comes from standard input (stdin)
for line in sys.stdin:
    # Remove leading/trailing whitespace and split key/value
    line = line.strip()
    if not line:
        continue
        
    region, days_str = line.split('\t', 1)
    
    try:
        days = int(days_str)
    except ValueError:
        # Ignore lines where the value is not an integer
        continue

    # Hadoop sorts mapper output by key before passing it to the reducer
    if current_region == region:
        current_sum += days
    else:
        # If there is a previous region we finished aggregating, print it
        if current_region:
            print(f"{current_region}\t{current_sum}")
        current_region = region
        current_sum = days

# Do not forget to output the last region if the loop ends!
if current_region == region:
    print(f"{current_region}\t{current_sum}")
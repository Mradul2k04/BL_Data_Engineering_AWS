import sys
## mapper 

for line in sys.stdin:
  supplier,cost=line.strip().split(",")
  print(f"{supplier}\t{cost}")

## reducer 

  #!/usr/bin/env python3

  import sys

  current_supplier = None
  total = 0
  count = 0

  for line in sys.stdin:

      supplier,cost = line.strip().split("\t")
      cost = int(cost)

      if current_supplier == supplier:

          total += cost
          count += 1

      else:

          if current_supplier:

              avg = total / count
              print(f"{current_supplier}\t{avg}")

          current_supplier = supplier
          total = cost
          count = 1

  if current_supplier:

      avg = total / count
      print(f"{current_supplier}\t{avg}")
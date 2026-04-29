results=""

for idx, i in enumerate(range(122,96,-1)):
   if idx%2==0:
      results+= chr(i).lower()
   else:
    results += chr(i).upper()

print(results, end = "")
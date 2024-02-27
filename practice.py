import csv  
response = request.get('https://cat-fact.herokuapp.com/facts')
data = response.json()
csv_file = 'data.csv'
openwith (csv_file, 'w',\n) as file:
write = csv.write(file)   
print("csv file created")

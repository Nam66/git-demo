import requests
import csv

def getCustomers():
    r = requests.get('https://db15608fed92733456359c2f7b15b23d:Topica123@nam66-store.myshopify.com/admin/api/2021-01/customers.json')
    return r.json()['customers']

customers = getCustomers()
fieldnames = [x for x in customers[0]]
data = []
for customer in customers:
	data.append([customer[key]] for key in customer)
rows = data
file = 'customers.csv'

with open(file, 'w') as csvfile:
	csvwriter = csv.writer(file)
	csvwriter.writerow(fieldsnames)
	csvwriter.writerows(rows)




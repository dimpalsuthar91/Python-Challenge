# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import numpy
import datetime
import pandas as pd
#csvpath = os.path.join('PyBank', 'budget_data_1.csv')

abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

ID = []
name = []
dob = []
dob2 = []
ssn = []
state = []

# Method 2: Improved Reading using CSV module
import csv
with open('employee_data2.csv', newline='') as csvfile1:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader1 = csv.reader(csvfile1, delimiter=',')
    next(csvreader1, None)

    for row in csvreader1:
        ID.append(row[0])
        name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])

#change name
fname = [i.split(' ', 1)[1] for i in name]
lname = [i.split(' ', 1)[0] for i in name]

# The DOB data should be re-written into DD/MM/YYYY format.
for i in dob:
    j = datetime.datetime.strptime(i, '%Y-%m-%d').strftime('%m/%d/%y')
    dob2.append(j)
#print(dob2)    


#p = '1985-12-04'
#np = datetime.datetime.strptime(p, '%Y-%m-%d').strftime('%m/%d/%y')
#print(np)

#The SSN data should be re-written such that the first five numbers are hidden from view.
ssn1 = []
for x in ssn:
    ssn1.append('***-**-' + x[7:])

state1 = []            
#print(ssn1)
for i in state:
    for k,v in abbrev.items():
        if i == k:
            state1.append(v)
#print(state1)            

combined = zip(ID, lname, fname, dob2, ssn1, state1)      

#  Open the output file
output_file = os.path.join('merged.csv')
with open(output_file, "w", newline="", encoding="utf-8") as joined:
    writer = csv.writer(joined)

    #Write the header row
    writer.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    # Write in zipped rows
    writer.writerows(combined)

df = pd.read_csv('merged.csv')
print(df.head())
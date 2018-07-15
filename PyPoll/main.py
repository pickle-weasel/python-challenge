import csv

csvpath = 'election_data.csv'

with open(csvpath, 'r') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')

    csvheader = next(reader)

    voter_id = []
    county = []
    candidate = []
    correy = []
    o_tooley = []
    li = []
    khan = []

    for row in reader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        
        
        if row[2] == 'Correy':
            correy.append(row[2])
        elif row[2] == "O'Tooley":
            o_tooley.append(row[2])
        elif row[2] == 'Li':
            li.append(row[2])
        else:
            khan.append(row[2])
            
total_votes = len(candidate)

correy_total = len(correy)
correy_percent = int(correy_total) / int(total_votes)

o_tooley_total = len(o_tooley)
o_tooley_percent = o_tooley_total / total_votes

li_total = len(li)
li_percent = li_total / total_votes

khan_total = len(khan)
khan_percent = khan_total / total_votes

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
print(f'Khan: {khan_percent:.3%} ({khan_total})')
print(f'Correy: {correy_percent:.3%} ({correy_total})')
print(f'Li: {li_percent:.3%} ({li_total})')
print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})")
print(f'-------------------------')
print(f'Winner: ')
print(f'-------------------------')
import csv

raw_data = open('election_data.csv')
csv_reader = csv.reader(raw_data, delimiter=',')
file_header = next(csv_reader)

Total_voters = 0
candidates = []
candidates_dict = {}

for row in csv_reader:
    Total_voters += 1
    if row[2] not in candidates:
        candidates.append(row[2])
    candidates_dict[row[2]] = candidates_dict.get(row[2],0)+ 1

for k,v in candidates_dict.items():
    candidates_dict[k]= str(round((v/Total_voters) * 100), 2)
maximum = max(candidates_dict, key=candidates_dict.get)

print ("Election Result")
print ("---------------------------------")
print (F"Total Votes: {Total_voters}")
print ("----------------------------------")
print ("{" + '\n'.join('{}:{}'.format(k, v) for k, v in candidates_dict.items()) + "}")
print ("----------------------------------")

print(F"Winner: {maximum}: {candidates_dict[maximum]}")

with open("out.txt", "w") as f:
    f.write("Election Result\n")
    f.write("----------------------------\n")
    f.write(F"Total Votes: {Total_voters}\n")
    f.write("-----------------------------\n")
    f.write("{" + '\n'.join('{}:{}'.format(k, v) for k, v in candidates_dict.items()) + "}\n")
    f.write("-----------------------------\n")
    f.write(F"Winner: {maximum}: {candidates_dict[maximum]}")

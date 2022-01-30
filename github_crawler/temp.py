import csv

'''with open('proxy_list.txt', 'r') as file:
    line_set = set(file.read().splitlines())
    print(line_set)

with open('proxy_list2.txt', 'w') as f:
    for item in line_set:
        f.write("\'%s\',\n" % item)'''

'''with open('builds.csv', 'r') as f:
    csvreader = csv.reader(f)
    header = next(csvreader)
    for row in csvreader:
        # with open('', 'a') as f2:
        print(row[0])'''

repos = []

with open('watchlist.txt', 'r') as file:
    line_set = set(file.read().splitlines())
    print(line_set)

with open("builds.csv", "r") as f, open("builds_intellij.csv", "a") as w:
    reader = csv.reader(f)
    header = next(reader)
    for row in f:
        repo_name = row.split(',')[16]
        if repo_name.strip() == 'T':
            print(row.split(',')[0], repo_name)
            w.write(row)
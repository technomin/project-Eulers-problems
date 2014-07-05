import csv

ifile  = open('ngosindia.csv', "rb")
reader = csv.reader(ifile)
reader.next()

for row in reader:
	fl =row[3]
	name = fl.split(" ")
	print name
	try:
		if len(name[0])>4:
			first_name = name[0]
			second_name = name[1]
		else:
			first_name = name[1]
			second_name = name[2]

		first_name = first_name.lower()
		second_name = second_name.lower()

		first_name = first_name.capitalize()
		second_name = second_name.capitalize()
		email = row[4]

	lst = [first_name, second_name, email]

	except:
		pass

ofile  = open('new3.csv', "wb")
writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for row in lst:
    writer.writerow(row)

ifile.close()
ofile.close()
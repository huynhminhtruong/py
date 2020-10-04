if __name__ == '__main__':
	file = open('./bulk_import_customers_1000.csv', 'w+')
	header = 'Extended Household Number**,Name**,fs.title.customer_name_phonetic,Address 1**,Address 2,Country**,State**,City,Postcode,Telephone,Mobile,Email,fs.title.contact_1,fs.title.contact_2,fs.title.contact_3,fs.title.comment\n'
	file.write(header)
	for i in range(0, 1001):
		file.write('asdas%dbulk,Tin,1,kak,treet,AU,ACT,can tho,1283912,+61400300700,+61400300700,zeroonea%d@gmail.com,1,2,3,no coimment\n' % (i + 1, i))
	file.close()

import csv
from nsdotpy.session import NSSession


UA = ""
password = ""
bid_amount = ""
season = ""


session = NSSession("card bidder", "1.0.0", "Ducky", UA)
mode = input("press enter to bid from a list of nations, type 'id' for card id: ")
rowcount = 0
rows = len(list(csv.reader(open('input.csv'))))

if mode.lower() == "id":
	print("bidding using id, please wait")
	with open('input.csv') as csv_file:
		csv_reader = csv.reader(csv_file)
		if session.login(UA, password):
			for row in csv_reader:
				rowcount+= 1
				print(f"({rowcount}/{rows}) bidding card {row[0]}...")
				session.bid(bid_amount, row[0], season)
		print("finished bidding!")

else:
	print("bidding using nations, please wait")
	import nationstates
	api = nationstates.Nationstates(f"card bidder by Ducky used by {UA}")
	with open('input.csv') as csv_file:
		csv_reader = csv.reader(csv_file)
		if session.login(UA, password):
			for row in csv_reader:
				rowcount+= 1
				print(f"({rowcount}/{rows}) bidding card {row[0]}...")
				nation = api.nation(row[0])
				session.bid(bid_amount, nation.dbid, season)
		print("finished bidding!")
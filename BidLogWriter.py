import csv

def main():
	data = [['bidid', 'bidprice']]
	totalBidSum = 12
	currentBid = 0
	while (currentBid < totalBidSum):
		data.append([currentBid, '233'])
		currentBid = currentBid + 1
	TestBidLogWriter(totalBidSum, data)

def TestBidLogWriter(totalBidSum, data):
	bid_log_file = open('testing bidding price.csv', 'w')
	bid_log_writer = csv.writer(bid_log_file)
	bid_log_writer.writerows(data)
	bid_log_file.close()

main()
import statistics
n = []
stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
]
stock_list = []
dates_list = []
filtered_list = []
while True: #ask date
    date_ask = input("What date would you like the search to include? (yyyy-mm-dd) \n >> ")
    # if date_ask not in stock_data:
    #     print("Error. Date not in database.")
    # else:
    dates_list.append(date_ask)
    again = input("Include another date? (yes/no) \n >> ")
    if again.lower() == "yes":
        continue
    else:
        break

while True: # ask stock
    ticker_ask = input("What stock would you like the search to include? \n >> ")
    stock_list.append(ticker_ask)
    again = input("Include another stock? (yes/no) \n >> ")
    if again.lower() == "yes":
        continue
    else:
        break
                         
for stock in stock_data:
    for date in dates_list:
        if date in stock[1]:
            for ticker in stock_list:
                if ticker in stock[0]:
                        filtered_list.append(ticker)
                        filtered_list.append(date)
                        n.append(stock[2])
                        print(f"Date: {stock[1]}, stock: {stock[0]}, price: {stock[2]}.")
try:
    print(f"Querry average price: {statistics.mean(n)}")
except statistics.StatisticsError: 
    print("Average 0: there is no search result.")

        
# for stock in stock_data:
#     for ticker in stock_list:
#         if ticker in stock[0]:
#             filtered_list.append(ticker)
#             print(filtered_list)
#             # print(f"Stock: {stock[0]}, price: {stock[2]}.") 
                # if date in stock[1]:
                #     print(f"Date: {stock[1]}, price: {stock[2]}.")
                    # n.append(stock[2])
        
# for stock in stock_data:
#     for ticker in stock_list:
#         if ticker in stock[0]:
#             print(stock[2])    
            
# print(statistics.mean(n))   
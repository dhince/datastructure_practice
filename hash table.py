stock_prices = []
with open("dhince.csv", "r") as d:
    for line in d:
        token = line.split(',')
        day = token[0]
        price = float(token[1])
        stock_prices.append([day,price])
print(stock_prices)
print(stock_prices[1][1])


#search for stock price on date 3 march
for element in stock_prices:
    if element[0] == "March 3":
        print(element[1])
#complexitiy is O(n) for searching using list
#now use dictionary to implement same thing

stock_price = {}
with open("dhince.csv", "r") as f:
    for lines in f:
        tokens = lines.split(',')
        key = tokens[0]
        value = float(tokens[1])
        stock_price [key] = value
print(stock_price)

for keys in stock_price:
    if keys == "March 9":
        print(stock_price[keys])

#complexity of search using dictionary is O(1)
#now it is time to implement hash table

def gethash(key):
    hash = 0
    for i in key:
        hash += ord(i)

    hash = hash % 100
    return hash

hash = gethash('march 9')
print(hash)

final_price =[]
prices = [15000,2000,13000,25000,35000]
for price in prices:
    if price <= 15000 and price > 5000:
       price=price-(price*0.1)
       final_price.append(int(price))
    elif price > 20000:
        price=price-(price*0.15)
        final_price.append(int(price))
    elif price < 5000:
        final_price.append(price)
print(final_price)
            
    

import random

low_limit  = 1
hi_limit = 50000
low_size = 2
hi_size = 100
size = random.randint(low_size,hi_size)


# price_list = [random.randint(low_limit, hi_limit) for _ in range(size)]

# result_price = ' '.join(map(str, price_list))
# print(result_price)

# discount = price_list[0]-price_list[-1]

# print(discount)


# test 2
price = []
for i in range (size):
    random_price = random.randint(low_limit,hi_limit)
    price.append(random_price)
    # for longer list
    if i == 1:
        price[1]=int((price[0]/2))
    elif i == 2:
        price[2]=int((price[1]/2))

    if price[0]<price[-1]:
        list_price = price[:-1]
        break

# print(price)
print(list_price)
discount = list_price[0]-list_price[-1]

print(discount)

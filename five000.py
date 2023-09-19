#1

file_f = open('penztar.txt')

shoppers_dict = {}
key_counter = 1
items_list = []
for item in file_f:
    if item.strip() == 'F':
        key_counter += 1 
        items_list = []
    else:
        items_list.append(item.strip())
    if len(items_list) > 0:
        shoppers_dict[key_counter] = items_list
    
#print((shoppers_list))

# 2

def num_of_shoppers():
    return len(shoppers_dict)

print(f'The number of shoppers is {num_of_shoppers()}.')

# 3

def num_of_items_per_shopper(num):
    return len(shoppers_dict[num])

print(f'Shopper #1 bought {num_of_items_per_shopper(1)} items.')

# 4
def user_input():
    shopping_num = int(input('Shopping number: '))
    item = input('Item: ')
    quantity = int(input('How many: '))
    return[shopping_num, item, quantity]

shopping_list = user_input()
#print(user_input())

# 5 

def item_bought_fist_and_last(lista):
    bought_item_by_shopper = [ k for k, v in shoppers_dict.items() if lista[1] in v ]
    print(f'{lista[1].capitalize()} was bought first by #{bought_item_by_shopper[0]} shopper, and it was bought last by #{bought_item_by_shopper[-1]} shopper.')
    print(f'{lista[1].capitalize()} was bought by {len(bought_item_by_shopper)} shoppers.')
item_bought_fist_and_last(shopping_list)

# 6

def price_calc_for_more(quant):
    if quant > 0:
        if quant == 1:
            return 500
        elif quant == 2:
            return 950
        elif quant == 3:
            return 1350
        else:
            return 1350 + ((quant - 3) * 400)
    else:
        return 0
    
def sum_price_calc(list):
    quantity_dict = { item:list.count(item) for item in list }
    sum_prices = [ price_calc_for_more(int(item)) for item in quantity_dict.values() ]
    return sum(sum_prices)
    
    
print(f'The price for {shopping_list[2]} {shopping_list[1]} is {price_calc_for_more(shopping_list[2])} HUF.')

# 7

def items_per_shopping(shopping_num):
    return { item: shoppers_dict[shopping_num].count(item) for item in shoppers_dict[shopping_num] }

for k, v in items_per_shopping(shopping_list[0]).items():
    print(v, k)

# 8

def sum_prices_file():
    sums_file = open('osszeg.txt', 'w')
    for k, v in shoppers_dict.items():
        one_shopper = ': '.join([str(k), str(sum_price_calc(v))])
        print(one_shopper, file=sums_file)
    
    sums_file.close()
    
sum_prices_file()

print(price_calc_for_more(8))
    

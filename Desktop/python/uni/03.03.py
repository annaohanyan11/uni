x = {'a': 1, 'b': 2, 'c': 3}

# print(x.keys())

y = list(x.values())


# x['b'] #accessing the value of 'b'

x['d'] = 4

x.update({'e': 5})

x.update({1: [1, 2, 3]})

# print(x)

# print('c' in x)

# del x['c']
# print(x)

# y = x.pop(1)
# print(y)

# z = [[1, 2], [2, 3]]
# print(dict(z))

# k = ['a', 'b', 'c'] 
# l = [1, 2, 3]

# p = dict(zip(k,l))

# print(p)




# k = dict((k, k*2) for k in range(0, 21))

# print(k)


# text = 'given a sentence, make a dictionary of all symbols and their frequencies'



# x = list(text)
# x_ = set(x)

# y = {t: x.count(t) for t in x_}

# print(y)



number = int(input("enter a number"))

if number%2 == 0:
	print("the number is even")
else:
	print("the given number is odd")	 








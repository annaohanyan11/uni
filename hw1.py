#problem_1
#Calculate the values of the Expression

x = pow(2, 10) + pow(3, 10)
y = pow(x, 0.5)

print(y)


#problem_2
#define a list

list_ = [1, 1, 2, 3, 2, 3, 1, 1, 2, 3, 4, 1]

#get the length of the list in variable 'l'

l = len(list_)

#Change the last element of the list by 5

list_[l-1] = 5

s = [5,6,7,8,9,10]

list_ = list_ + s

#Extract all odd-indexed elements of the list in the list y, and all 
#even-indexed elements of list into the list z

k = len(list_) - 1

y = [list_[i] for i in range(0,k) if i % 2 == 0]

z = [list_[i] for i in range(0,k) if i % 2 == 1]

#Get all even elements of x in the list y1 and all odd elements of $x$ in the list z1

y1 = [list_[i] for i in range(0,k) if list_[i] % 2 == 0]

z1 = [list_[i] for i in range(0,k) if list_[i] % 2 == 1]

#Find the sum of the elements of the list

k = 0
for i in list_:
	k = k + list_[i]
print(k)


#Construct a list I consisting of all reciprocals of the elements of the list

I = [1/list_[i] for i in list_]

#Find the value of the sum

k = [1/pow(3,k) for k in range(1, 11)]

print(sum(k))

#problem3

text = 'Pneumonoultramicroscopicsilicovolcanoconiosis'

#Find the number of letters in this word

print(len(text))

#Find the number of letters "o" in this word

a = text.count('o')

#Find the number of vowels (ձայնավորներ) in this word

v = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

f = [i for i in text if i in v]

print(len(f))





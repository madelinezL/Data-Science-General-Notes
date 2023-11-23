what_he_does = ' plays '
his_instrument = 'guitar'
his_name = 'Robert Johnson'
artist_intro = his_name + what_he_does + his_instrument
print(artist_intro)

word = 'friends'
find_the_evil_in_your_friends = word[0] + word[2:4] + word[-3:-1]
print(find_the_evil_in_your_friends)

print('{} a word she can get what she {} for.'.format('With', 'came'))
print('{preposition} a word she can get what she {verb} for'.format(preposition='With',verb = 'came'))
print('{0} a word she can get what she {1} for.'.format('With', 'came'))


middle = 5
1 < middle < 10
print (1 < middle < 10)

for i in range (1,10):
    for j in range (1,10):
        print('{} X {} = {}'.format(i,j,i*j))
        

Weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday']
print(Weekday[0])

fruit = ['pineapple','pear']
fruit.insert(1,'grape')
print(fruit)

a = {'key':123, 'key':123}
print(a)

num_list = [6,2,7,4,1,3,5]
print(sorted(num_list))
sorted(num_list,reverse=True)

a = []
for i in range (1,11):
    a.append(i)

b = [i for i in range(1,11)]

a = [i**2 for i in range(1,10)]
c = [j+1 for j in range(1,10)]
k = [n for n in range(1,10) if n % 2 ==0]
z = [letter.lower() for letter in 'ABCDEFGHIGKLMN']

d = {i:i+1 for i in range(4)}
g = {i:j for i,j in zip(range(1,6), 'abcde')}
g = {i:j.upper() for i,j in zip(range(1,6),'abcde')}

print(a)
print(c)
print(k)
print(z)

print(d)
print(g)
print(g)

letters = ['a','b','c','d','e','f','g']
for num, letter in enumerate(letters):
    print(letter, 'is', num+1)
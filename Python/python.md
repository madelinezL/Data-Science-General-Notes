### Basics
#### string
```Hello, World!```

#### how to slice
```word = 'friends'``` <br/>
```find_the_evil_in_your_friends = word[0] + word[2:4] + word[-3:-1]```<br/>
```print(find_the_evil_in_your_friends)```

#### how to use format
```print('{} a word she can get what she {} for.'.format('With', 'came'))``` <br/>
```print('{preposition} a word she can get what she {verb} for'.format(preposition='With',verb = 'came'))```<br/>
```print('{0} a word she can get what she {1} for.'.format('With', 'came'))```

#### list comprehension
```d = {i:i+1 for i in range(4)}``` <br/>
```g = {i:j for i,j in zip(range(1,6), 'abcde')}```<br/>
```g = {i:j.upper() for i,j in zip(range(1,6),'abcde')}```

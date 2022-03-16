# Count number of words in sentence

count = 1

stringList = []

string = input('Enter a sentence: ')

for i in string:
    if i == ' ':
        count = count + 1

print(count)

# o/p:
# Enter a sentence: a fox jumps over a fox
# 6
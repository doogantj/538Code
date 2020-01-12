import numpy as np
nameFile = "NumberNames.txt"

def eachScore(letter):
    switcher = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'f': 5,
        'e': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }
    return switcher.get(letter)

def scoreOf(name):
    letters = list(name)
    score = 0
    for N in range(len(letters)):
        score = score + eachScore(letters[N])
    return score

# Get list of number words
numberWords = []

with open(nameFile,'r') as nameFile:
    for name in nameFile:
        name = name[:-1]
        numberWords.append(name)

numbers = []
for N in range(999):
    i = N;
    N = N+1;
    # Figure out the value of the last two numbers
    if np.mod(N,100) < 20 and np.mod(N,100) > 0:
        (N - np.mod(N,100))
        numbers.append(numberWords[np.mod(N,100)-1])
    else:
        numbers.append(numberWords[(np.mod(N,100) - np.mod(np.mod(N,100),10))/10+17])
        if np.mod(np.mod(N,100),10) > 0:
            numbers[i] = numbers[i] + numberWords[np.mod(np.mod(N,100),10)-1]

    if N > 99:
        numbers[i] = numbers[i]+numberWords[27]
        hunVal = (N-np.mod(N,100))/100
        numbers[i] = numbers[i]+numberWords[hunVal-1]

i = 1
maxList = []
trueNumbers = []

for num in numbers:
    if scoreOf(num) > i:
        maxList.append(i)
        trueNumbers.append(scoreOf(num))
    i = i+1

# Print the max
print maxList[-1]

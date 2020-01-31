words = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    'hundred': 'hundred',
    'thousand': 'thousand',
    'and': 'and'
}

current = 1
sum = 0

def count_less_than_hundred(n):
    sum = 0
    if(n > 19):
        sum += len(words[int(str(n)[0] + '0')])
        if(n % 10 != 0):
            sum += len(words[int(str(n)[1])])
    else:
        sum += len(words[n])
    return sum

def words_less_than_hundred(n):
    worded = ''
    if(n > 19):
        worded += words[int(str(n)[0] + '0')]
        if(n % 10 != 0):
            worded += words[int(str(n)[1])]
    else:
        worded += words[n]
    return worded

def count(n):
    sum = 0
    worded = ''
    if(n > 999):
        sum += len(words['thousand']) + len(words[1])
        worded += words[1] + words['thousand']
    elif(n > 99):
        sum += len(words[int(str(n)[0])]) + len(words['hundred'])
        worded += words[int(str(n)[0])] + words['hundred']
        if(n % 100 != 0):
            sum += len(words['and']) + count_less_than_hundred(int(str(n)[1:]))
            worded += words['and'] + words_less_than_hundred(int(str(n)[1:]))
    else:
        sum += count_less_than_hundred(n)
        worded += words_less_than_hundred(n)
    # print(worded)
    return sum

while current <= 1000:
    sum += count(current)
    current = current + 1

print(sum)
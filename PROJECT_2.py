REPLACEMENTS = {
        '\n': ' ',
        'mr.': 'mr',
        'dr.': 'dr',
        'mrs.': 'mrs',
        'ms.': 'ms',
        '?': '.',
        ',':'',
        '!': '.',
        '"': ' ',
        "'": ' ',
        ';': '',
        '--': ' ',
        '(': '',
        ')': '',
        #'m.r.c.s.': 'mrcs',
        #'c.c.h.': 'cch',
        #'c.c': 'cc',
}
with open('/Users/mek/Desktop/MCS260/positive.txt', 'r') as f:
    positive = f.read()
positive = positive.split('\n')

with open('/Users/mek/Desktop/MCS260/negative.txt', 'r') as f:
    negative = f.read()
negative = negative.split('\n')

with open('/Users/mek/Desktop/MCS260/thehoundofthebaskervilles.txt', 'r') as f:
    text = f.read()
text = text.lower()

for key, val in REPLACEMENTS.items():
    text = text.replace(key, val)
sentences = text.split('.')

sentiments = {'Positive': 0, 'Negative': 0, 'Neutral': 0}

for s in sentences:
    count_pos, count_neg = 0, 0
    words = s.split()
    for w in words:
        if w in positive:
            count_pos += 1
        elif w in negative:
            count_neg += 1
    if count_pos > count_neg:
        sentiments['Positive'] += 1
    elif count_neg > count_pos:
        sentiments['Negative'] += 1
    else:
        sentiments['Neutral'] += 1

print('Positive: {} \nNegative: {} \nNeutral: {}'.format(sentiments['Positive'], sentiments['Negative'], sentiments['Neutral']))
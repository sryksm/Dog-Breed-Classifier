
b = ['qwe', 'wer', 'ert', 'tyu']
c = {}

for i in b:
    a = ''
    a = a + i + ' '
    a = a.strip()
    if i not in c.keys():
        c[i] = [a]

print(c)
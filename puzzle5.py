import hashlib
#input = 'abc'
input = 'abbhdwsy'
i = 0
done = False
keys = {}
while not done:
    m = hashlib.md5()
    c = input + str(i)
    c = c.encode('utf-8')
    m.update(c)
    h = m.hexdigest()
    if h.startswith('00000'):
        pos = h[5]
        if pos >= '0' and pos <='7' and keys.get(pos) == None:
            keys[h[5]] = h[6]
            print(h, len(keys))
        if len(keys) == 8:
            done = True
    else:
        done = False
    i= i+1
keys = [(k, v) for k, v in keys.items()]
keys = sorted(keys, key=lambda x: x[0])
print('keys', keys)



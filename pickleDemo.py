import pickle

#把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling

d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d2 = pickle.load(f)
f.close()
print(d2)

import json
d3 = dict(name='Bob', age=20, score=88)
json.dumps(d3)
print(d3)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)
print(json_str)
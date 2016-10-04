# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# sequence 항목을 변경하고자 할 때, copy를 만들어서 해당 동작을 수행한다.
for w in words[:]: # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
print(words)
query = "fro??"
word = "frodo"
a_sep = 0
if query[0] == '?':
    a_sep = 1
if query[-1] == '?':
    a_sep = -1

a_keyword = ""
for i in query:
    if i != '?':
        a_keyword += i
print(a_keyword)
k_len = len(a_keyword)
print(word[0: k_len])
if a_sep == 1:
    if word[0: k_len] == a_keyword:
        print("동일하다")
if a_sep == -1:
    if word[0: k_len] == a_keyword:
        print("동일하다")
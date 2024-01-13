#
# import re   #正则表达式库re
# from collections import Counter
#
# n =eval( input())
# with open('hamlet.txt', 'r', encoding='utf-8') as f:
#     text = f.read().lower()#转化为小写字母
#     text = re.sub(r'[!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~]', ' ', text)#去掉符号
#     words = text.split()
#    # words = re.findall(r'\b[a-z]+\b', text)
#     #r'\b[a-z]+\b'是一个正则表达式，它匹配任何由一个或多个小写字母组成的单词。\b是一个单词边界，[a-z]匹配任何小写字母，+表示一个或多个。
#     counter = Counter(words)
#     most_common_words = counter.most_common(n)
#     for word, count in most_common_words:
#         print(f"{word:<10}{count:>5}")
# '''
# most_common_words是一个列表，其中的每个元素都是一个元组，包含一个单词和它的计数。
# 所以，for word, count in most_common_words:这行代码会遍历most_common_words列表中的每个元组，并将元组的第一个元素赋值给word，第二个元素赋值给count。
# '''


def getText():
    txt= open("hamlet.txt", "r").read()
    txt= txt. lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        txt= txt. replace(ch, " ")
    return txt
hamletTxt = getText()
words = hamletTxt. split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts. items())
items.sort(key=lambda x:x[1], reverse=True)
n = eval(input())
for i in range(n):
    word, count = items[i]
    print("{0:<10}{1:>5}". format(word, count))

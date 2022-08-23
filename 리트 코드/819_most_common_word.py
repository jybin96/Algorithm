import collections
import re

paragraph = str(input())
banned = list(map(str, input().split()))

words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
         if word not in banned]

counter_words = collections.Counter(words)
print(counter_words.most_common(1)[0][0])
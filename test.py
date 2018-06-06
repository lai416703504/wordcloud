# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

text = open(r'./4578.txt', 'r').read()

cut_text = jieba.cut(text)

result = "/".join(cut_text)

wc = WordCloud(font_path='./msyh.ttf' ,background_color='white', width=1080, height=2160, max_font_size=50, max_words=10000, min_font_size=10,
               mode='RGBA', colormap='pink')

wc.generate(result)
wc.to_file(r"./4578.png")

# plt.figure("词云图")
# plt.imshow(wc)
# plt.axis("off")
# plt.show()

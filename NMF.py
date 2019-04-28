import numpy as np
# from sklearn.feature_extraction.text import TfidfVectorizer
# # 四个词，五个文本
# X = np.array([[1,1,5,2,3], [0,6,2,1,1], [3, 4,0,3,1], [4, 1,5,6,3]])
# from sklearn.decomposition import NMF
# # 预定义三个主题
# model = NMF(n_components=3, alpha=0.01)
# W = model.fit_transform(X)
# H = model.components_
# print(W)
# print(H)
# #Wik 对应第i个词的和第k个主题的概率相关度，而Hkj对应第j个文本和第k个主题的概率相关度。
data = list(open('C:/Users/jing/Desktop/stop_words.txt'))
print([i.replace('\n','') for i in data])
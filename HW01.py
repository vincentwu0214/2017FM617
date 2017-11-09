
# coding: utf-8

# #Q1. 請使用 python 讀入 Nasdaq 公司資訊！

# In[5]:


import pandas


# In[13]:


df = pandas.read_csv('C:/Users/Administrator/Desktop/companylist.CSV')
df


# #Q2. 請使用 python 畫中山大學管理學院周邊地圖！

# In[19]:


import geocoder


# In[27]:


nsysu = geocoder.google('中山大學管理學院,Taiwan')
nsysu.latlng


# In[29]:


import folium


# In[33]:


nsysu = folium.Map(location=[22.627447, 120.265274])
nsysu


# #Q3. 請使用 python 將新聞中可能的關鍵詞萃取出來！ (Bonus)

# In[49]:


import jieba


# In[54]:


import util


# In[55]:


news_text = util.get_news_article('https://news.cnyes.com/news/id/3960008?exp=b')


# In[56]:


news_text


# In[59]:


seg_list = jieba.cut_for_search("權證")  # 搜索引擎模式
print(", ".join(seg_list))


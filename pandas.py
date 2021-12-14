#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
df = pd.read_csv("telecom_users.csv")
df = df.drop (["Unnamed: 0"], axis=1)
df["TotalGasto"] = pd.to_numeric(df["TotalGasto"], errors="coerce")


display(df)
print(df.info())


# In[22]:


#tranformar em númerico a coluna que está com dados em texto
df["TotalGasto"] = pd.to_numeric(df["TotalGasto"], errors = "coerce")
#remover a coluna totalmente vazia
df = df.dropna(how="all", axis = 1)
#remover a linha com itens vazios
df = df.dropna()

display(df["Churn"].value_counts())
display(df["Churn"].value_counts(normalize = True).map("{:.1%}".format))

import plotly.express as px
for coluna in df:
     if coluna != "costumerID":
     #criar a figura 
        fig = px.histogram(df, x = coluna, color = "Churn")
         #exibir a figura
        fig.show()
        #display(df.pivot_table(index = "Churn", columns = coluna, aggfunc="count")["costumerID"])


# In[ ]:





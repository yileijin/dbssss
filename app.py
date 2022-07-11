#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request


# In[2]:


import joblib


# In[3]:


app = Flask(__name__)


# In[5]:


@app.route("/", methods=["GET", "POST"])
def index():
     if request.method =="POST":
        rates= float(request.form.get("rates"))
        print(rates)
        return(render_template("index.html", result ="NIL"))
     else:
        return(render_template("index.html", result ="WAITING"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
import joblib

@app.route("/", methods = ["GET", "POST"])
def index(): 
    if request.method == "POST":
        income = request.form.get("income")
        age = request.form.get("age")
        loan = request.form.get("loan")

      
        model = joblib.load("CreditCardREG")
        pred = model.predict([[float(income),float(age),float(loan)]])
        s1 = "Predicted DBS Share price base on Linear Regression model is : " + str(pred)
        
        model = joblib.load("CreditCardDT")
        pred = model.predict([[float(income),float(age),float(loan)]])
        s2 = "Predicted DBS Share price base on Decision Tree model is : " + str(pred)
        
        
        model = joblib.load("CreditCardNN")
        pred = model.predict([[float(income),float(age),float(loan)]])
        s3 = "Predicted DBS Share price base on Neural Network model is : " + str(pred)
        
        return(render_template("index.html", result1=s1, result2=s2, result3=s3))
    else: 
          return(render_template("index.html", result1="2", result2="2", result3="2"))
        


# In[ ]:


if __name__=="__main__":
    
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





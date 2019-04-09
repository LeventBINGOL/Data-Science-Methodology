#!/usr/bin/env python
# coding: utf-8

# <a href="https://cognitiveclass.ai"><img src = "https://ibm.box.com/shared/static/9gegpsmnsoo25ikkbl4qzlvlyjbgxs5x.png" width = 400> </a>
# 
# <h1 align=center><font size = 5>From Requirements to Collection</font></h1>

# ## Introduction
# 
# In this lab, we will continue learning about the data science methodology, and focus on the **Data Requirements** and the **Data Collection** stages.

# ## Table of Contents
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
# 1. [Data Requirements](#0)<br>
# 2. [Data Collection](#2)<br>
# </div>
# <hr>

# # Data Requirements <a id="0"></a>

#  

# <img src="https://ibm.box.com/shared/static/dv60vn9nq3kb3n7efc5lxtxfgp11stfz.png" width=500>

# In the videos, we learned that the chosen analytic approach determines the data requirements. Specifically, the analytic methods to be used require certain data content, formats and representations, guided by domain knowledge.

# In the **From Problem to Approach Lab**, we determined that automating the process of determining the cuisine of a given recipe or dish is potentially possible using the ingredients of the recipe or the dish. In order to build a model, we need extensive data of different cuisines and recipes.

# Identifying the required data fulfills the data requirements stage of the data science methodology.
# 
# -----------

# # Data Collection <a id="2"></a>

# <img src = "https://ibm.box.com/shared/static/hgocgq6no4d09pbr140hmt3jtjizy2da.png" width=500>

# In the initial data collection stage, data scientists identify and gather the available data resources. These can be in the form of structured, unstructured, and even semi-structured data relevant to the problem domain.

# #### Web Scraping of Online Food Recipes 
# 
# A researcher named Yong-Yeol Ahn scraped tens of thousands of food recipes (cuisines and ingredients) from three different websites, namely:

# <img src = "https://ibm.box.com/shared/static/4fruwan7wmjov3gywiz3swlojw0srv54.png" width=500>
# 
# www.allrecipes.com
# 
# <img src = "https://ibm.box.com/shared/static/cebfdbr22fjxa47lltp0bs533r103g0z.png" width=500>
# 
# www.epicurious.com
# 
# <img src = "https://ibm.box.com/shared/static/epk727njg7xrz49pbkpkzd05cm5ywqmu.png" width=500>
# 
# www.menupan.com

# For more information on Yong-Yeol Ahn and his research, you can read his paper on [Flavor Network and the Principles of Food Pairing](http://yongyeol.com/papers/ahn-flavornet-2011.pdf).

# Luckily, we will not need to carry out any data collection as the data that we need to meet the goal defined in the business understanding stage is readily available.

# #### We have already acquired the data and placed it on an IBM server. Let's download the data and take a look at it.

# <strong>Important note:</strong> Please note that you are not expected to know how to program in Python. The following code is meant to illustrate the stage of data collection, so it is totally fine if you do not understand the individual lines of code. We have a full course on programming in Python, <a href="http://cocl.us/PY0101EN_DS0103EN_LAB2_PYTHON_Coursera"><strong>Python for Data Science</strong></a>, which is also offered on Coursera. So make sure to complete the Python course if you are interested in learning how to program in Python.

# ### Using this notebook:
# 
# To run any of the following cells of code, you can type **Shift + Enter** to excute the code in a cell.

# Get the version of Python installed.

# In[ ]:


# check Python version
get_ipython().system('python -V')


# Read the data from the IBM server into a *pandas* dataframe.

# In[ ]:


import pandas as pd # download library to read data into dataframe
pd.set_option('display.max_columns', None)

recipes = pd.read_csv("https://ibm.box.com/shared/static/5wah9atr5o1akuuavl2z9tkjzdinr1lv.csv")

print("Data read into dataframe!") # takes about 30 seconds


# Show the first few rows.

# In[ ]:


recipes.head()


# Get the dimensions of the dataframe.

# In[ ]:


recipes.shape


# So our dataset consists of 57,691 recipes. Each row represents a recipe, and for each recipe, the corresponding cuisine is documented as well as whether 384 ingredients exist in the recipe or not beginning with almond and ending with zucchini.
# 
# -----------

# Now that the data collection stage is complete, data scientists typically use descriptive statistics and visualization techniques to better understand the data and get acquainted with it. Data scientists, essentially, explore the data to:
# 
# * understand its content,
# * assess its quality,
# * discover any interesting preliminary insights, and,
# * determine whether additional data is necessary to fill any gaps in the data.

# ### Thank you for completing this lab!
# 
# This notebook was created by [Alex Aklson](https://www.linkedin.com/in/aklson/). I hope you found this lab session interesting. Feel free to contact me if you have any questions!

# This notebook is part of a course on **Coursera** called *Data Science Methodology*. If you accessed this notebook outside the course, you can take this course, online by clicking [here](http://cocl.us/DS0103EN_Coursera_LAB2).

# <hr>
# Copyright &copy; 2018 [Cognitive Class](https://cognitiveclass.ai/?utm_source=bducopyrightlink&utm_medium=dswb&utm_campaign=bdu). This notebook and its source code are released under the terms of the [MIT License](https://bigdatauniversity.com/mit-license/).

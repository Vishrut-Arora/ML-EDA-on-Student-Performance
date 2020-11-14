#!/usr/bin/env python
# coding: utf-8

# ## ML MINOR PROJECT
# 
# #### VISHRUT ARORA

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

student_table=pd.read_csv('StudentsPerformance (1).csv')
print("COLUMNS: ")
print(student_table.columns.tolist())
print(student_table.gender.unique())
print(student_table['race/ethnicity'].unique())
print(student_table['parental level of education'].unique())
print(student_table['lunch'].unique())
print(student_table['test preparation course'].unique())
print(student_table.info())
#print(sns.distplot(student_table[['math score','reading score','writing score']]))
#sns.distplot(student_table['math score'],bins=11,hist_kws=dict(edgecolor='yellow',linewidth=3,color='green'))
#sns.distplot(student_table['reading score'],bins=11,hist_kws=dict(edgecolor='yellow',linewidth=3,color='green'))
print(sns.kdeplot(student_table['math score'],shade=True))
print(sns.kdeplot(student_table['reading score'],shade=True))
print(sns.kdeplot(student_table['writing score'],shade=True))


# **OBSERVATIONS**
# 
# * The table has 8 columns and 1000 rows with three int64, five object data types and no null values.
# * There are 3 numerical and 5 categorical data
# * The Sns kdeplot helps to get a view of the three distributions i.e Math score, reading score and writing score.

# In[6]:


print(student_table.describe())
plt.rcParams['figure.figsize']=(30,20)
sns.countplot(student_table['math score'],palette='dark')
plt.title('Math Score',fontsize=25)
plt.show()
plt.rcParams['figure.figsize']=(30,20)
sns.countplot(student_table['reading score'],palette='dark')
plt.title('Reading Score',fontsize=25)
plt.show()
plt.rcParams['figure.figsize']=(30,20)
sns.countplot(student_table['writing score'],palette='dark')
plt.title('Writing Score',fontsize=25)
plt.show()


# **OBSERVATIONS**
# 
# * Displayed mean, std, min-max etc.
# * With this we get to how is the count of each score been distributed and make a good criteria for setting up grades later.

# In[35]:


plt.figure(figsize=(20,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.subplot(141)
plt.title('Math Score')
sns.violinplot(y='math score',data=student_table,color='y',linewidth=2)
plt.subplot(142)
plt.title('Reading Score')
sns.violinplot(y='reading score',data=student_table,color='b',linewidth=2)
plt.subplot(143)
plt.title('Writing Score')
sns.violinplot(y='writing score',data=student_table,color='g',linewidth=2)
plt.show()


# **OBSERVATIONS**
# 
# * Symmetric plot
# * Large number of students scored marks within 60-80 in all three subjects excepth Maths with 50-80 as described above 

# In[8]:


plt.figure(figsize=(20,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.subplot(141)
plt.title('Gender',fontsize=20)
student_table['gender'].value_counts().plot.pie(autopct="%1.1f%%")

plt.subplot(142)
plt.title('Race/Ethinicity',fontsize=20)
student_table['race/ethnicity'].value_counts().plot.pie(autopct="%1.1f%%")

plt.subplot(143)
plt.title('Lunch',fontsize=20)
student_table['lunch'].value_counts().plot.pie(autopct="%1.1f%%")
plt.figure(figsize=(20,10))
plt.subplots_adjust(left=0.125,bottom=0.1,right=0.9,top=0.9,wspace=0.5,hspace=0.2)

plt.subplot(141)
plt.title('Parental level of education',fontsize=20,pad=-30)
student_table['parental level of education'].value_counts().plot.pie(autopct="%1.1f%%")

plt.subplot(142)
plt.title('Test preparation course',fontsize=20)
student_table['test preparation course'].value_counts().plot.pie(autopct="%1.1f%%")


# **OBSERVATIONS**
# 
# * The pie chart for different columns describes how percentage of values are there in each one of them.
# * There are more number of females, more people belonging to Group C, standard lunch preferred, parents are more belonging to some college and associate degree and more students left to complete their test preparation course. 

# 

# In[40]:


plt.figure(figsize=(20,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.subplot(131)
plt.title('Math Score')
sns.barplot(x='gender', y='math score', data=student_table)
plt.subplot(132)
plt.title('Reading Score')
sns.barplot(x='gender', y='reading score', data=student_table)
plt.subplot(133)
plt.title('Writing Score')
sns.barplot(x='gender', y='writing score', data=student_table)
plt.show()


# **OBSERVATIONS**
# 
# * Females outshine in reading and writing score while Males scored better in Maths.

# In[41]:


plt.figure(figsize=(20,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.subplot(131)
plt.title('Math Score')
sns.barplot(x='race/ethnicity', y='math score', data=student_table)
plt.subplot(132)
plt.title('Reading Score')
sns.barplot(x='race/ethnicity', y='reading score', data=student_table)
plt.subplot(133)
plt.title('Writing Score')
sns.barplot(x='race/ethnicity', y='writing score', data=student_table)
plt.show()


# **OBSERVATIONS**
# 
# * Scores followed the order for the Race/Ethnicity as: Group E > Group D > Group C > Group B > Group A

# In[45]:


plt.figure(figsize=(35,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.subplot(131)
plt.title('Math Score')
sns.barplot(x='parental level of education', y='math score', data=student_table)
plt.figure(figsize=(35,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.subplot(131)
plt.title('Reading Score')
sns.barplot(x='parental level of education', y='reading score', data=student_table)
plt.figure(figsize=(35,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)

plt.subplot(131)
plt.title('Writing Score')
sns.barplot(x='parental level of education', y='writing score', data=student_table)
plt.show()


# **OBSERVATIONS**
# 
# * Students whose parents had a master's degree performed better in all three subjects

# In[46]:


plt.figure(figsize=(20,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.subplot(131)
plt.title('Math Score')
sns.barplot(x='lunch', y='math score', data=student_table)
plt.subplot(132)
plt.title('Reading Score')
sns.barplot(x='lunch', y='reading score', data=student_table)
plt.subplot(133)
plt.title('Writing Score')
sns.barplot(x='lunch', y='writing score', data=student_table)
plt.show()


# **OBSERVATIONS**
# 
# * Students with Standard lunch scored higher than those with free/reduced lunch

# In[47]:


plt.figure(figsize=(20,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.subplot(131)
plt.title('Math Score')
sns.barplot(x='test preparation course', y='math score', data=student_table)
plt.subplot(132)
plt.title('Reading Score')
sns.barplot(x='test preparation course', y='reading score', data=student_table)
plt.subplot(133)
plt.title('Writing Score')
sns.barplot(x='test preparation course', y='writing score', data=student_table)
plt.show()


# **OBSERVATIONS**
# 
# * Those who had completed test preparation course performed way better in all three subjects.

# **NOW WE WILL OBSERVE THE PLOTS SEPARATELY**

# In[29]:


plt.figure(figsize=(20,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.subplot(131)
plt.title('GENDER AND RACE')
sns.countplot(x='race/ethnicity', hue='gender', data=student_table)
plt.subplot(132)
plt.title('GENDER AND LUNCH')
sns.countplot(x='lunch', hue='gender', data=student_table)
plt.subplot(133)
plt.title('GENDER AND TEST PREPARATION COURSE')
sns.countplot(x='test preparation course', hue='gender', data=student_table)
plt.figure(figsize=(35,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.subplot(121)
plt.title('GENDER AND PARENTAL LEVEL OF EDUCATION')
sns.countplot(x='parental level of education', hue='gender', data=student_table)


# In[30]:


plt.figure(figsize=(20,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.subplot(131)
plt.title('RACE/ETHNICITY AND GENDER')
sns.countplot(x='gender', hue='race/ethnicity', data=student_table)
plt.subplot(132)
plt.title('RACE/ETHNICITY AND LUNCH')
sns.countplot(x='lunch', hue='race/ethnicity', data=student_table)
plt.subplot(133)
plt.title('RACE/ETHNICITY AND TEST PREPARATION COURSE')
sns.countplot(x='test preparation course', hue='race/ethnicity', data=student_table)
plt.figure(figsize=(35,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.subplot(121)
plt.title('RACE/ETHNICITY AND PARENTAL LEVEL OF EDUCATION')
sns.countplot(x='parental level of education', hue='race/ethnicity', data=student_table)


# In[24]:


plt.figure(figsize=(20,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.subplot(131)
plt.title('LUNCH AND GENDER')
sns.countplot(x='gender', hue='lunch', data=student_table)
plt.subplot(132)
plt.title('LUNCH AND RACE/ETHNICITY')
sns.countplot(x='race/ethnicity', hue='lunch', data=student_table)
plt.subplot(133)
plt.title('LUNCH AND TEST PREPARATION COURSE')
sns.countplot(x='test preparation course', hue='lunch', data=student_table)
plt.figure(figsize=(35,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.subplot(121)
plt.title('LUNCH AND PARENTAL LEVEL OF EDUCATION')
sns.countplot(x='parental level of education', hue='lunch', data=student_table)


# In[25]:


plt.figure(figsize=(20,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.subplot(131)
plt.title('TEST PREPARATION COURSE AND GENDER')
sns.countplot(x='gender', hue='test preparation course', data=student_table)
plt.subplot(132)
plt.title('TEST PREPARATION COURSE AND RACE/ETHNICITY')
sns.countplot(x='race/ethnicity', hue='test preparation course', data=student_table)
plt.subplot(133)
plt.title('TEST PREPARATION COURSE AND LUNCH')
sns.countplot(x='lunch', hue='test preparation course', data=student_table)
plt.figure(figsize=(35,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.subplot(121)
plt.title('TEST PREPARATION COURSE AND PARENTAL LEVEL OF EDUCATION')
sns.countplot(x='parental level of education', hue='test preparation course', data=student_table)


# In[28]:


plt.figure(figsize=(20,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.subplot(131)
plt.title('PARENTAL LEVEL OF EDUCATION AND GENDER')
sns.countplot(x='gender', hue='parental level of education', data=student_table)
plt.subplot(132)
plt.title('PARENTAL LEVEL OF EDUCATION AND RACE/ETHNICITY')
sns.countplot(x='race/ethnicity', hue='parental level of education', data=student_table)
plt.subplot(133)
plt.title('PARENTAL LEVEL OF EDUCATION AND LUNCH')
sns.countplot(x='lunch', hue='parental level of education', data=student_table)
plt.figure(figsize=(35,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.subplot(121)
plt.title('PARENTAL LEVEL OF EDUCATION AND TEST PREPARATION COURSE')
sns.countplot(x='test preparation course', hue='parental level of education', data=student_table)


# ### GPA

# In[14]:


#GPA DEFINED AS FOLLOWS
def determine_final_gpa(percentage):
    if percentage>=85 and percentage<=100:
        return '10 GPA'
    elif percentage>=75:
        return '9 GPA'
    elif percentage>=65:
        return '8 GPA'
    elif percentage>=55:
        return '7 GPA'
    elif percentage>=40:
        return '6 GPA'
    elif percentage>=30:
        return '5 GPA'
    else:
        return 'Repeat'
    
student_table['percentage']=(student_table['math score']+student_table['reading score']+student_table['writing score'])/3
#student_table['gpa']=(determne_final_gpa(student_table.['percentage']))
student_table['gpa']=""
for i in range(1000):
    student_table.at[i,'gpa']=(determine_final_gpa(student_table.iloc[i]['percentage']))
    
plt.figure(figsize=(20,10))
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.7,hspace=0.2)
plt.subplot(121)
plt.title('GPA DISTRIBUTION',fontsize=20)
student_table['gpa'].value_counts().plot.pie(autopct="%1.1f%%")


# In[17]:


plt.figure(figsize=(20,5))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.title('GENDER AND GPA')
sns.countplot(x='gender', hue='gpa', data=student_table)
plt.show()
plt.title('RACE AND GPA')
sns.countplot(x='race/ethnicity', hue='gpa', data=student_table)
plt.show()
plt.title('PARENTAL LEVEL OF EDUCATION AND GPA')
sns.countplot(x='parental level of education', hue='gpa', data=student_table)
plt.show()
plt.title('TEST PREPARATION COURSE AND GPA')
sns.countplot(x='test preparation course', hue='gpa', data=student_table)
plt.show()
plt.title('LUNCH AND GPA')
sns.countplot(x='lunch', hue='gpa', data=student_table)
plt.show()


# **OBSERVATIONS**
# 
# * Analysed data with the help of countplot in GPA(Overall student performance) and showed how other factors played a role in it.

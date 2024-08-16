#pandas-Data analytics tool

import pandas as pd
import numpy as np

#df=pd.read_csv("E:\Programs\Python\Pandas\pokemon_data.csv",delimiter='\t')            #for tab separated files can use other delimiters
df=pd.read_csv(r"E:\Programs\Python\Pandas\pokemon_data.csv")                            #files of different formats can also be read
#df=pd.read_csv("E:\Programs\Python\Pandas\pokemon_data.csv",header=None)               for files that does not have any header/column name else fisrt column is used as header
#df=pd.read_csv("E:\Programs\Python\Pandas\pokemon_data.csv",names=[],index_cols="")    #names -user defined column name, index_cols=user defined index name
#df=pd.read_csv("E:\Programs\Python\Pandas\pokemon_data.csv",skiprows=[])               #to skip some particular rows while reading file

pd.set_option('display.max_rows',5)                             #to define maximum number of rows to be displayed same can be done for columns

#Basic operations on Data Frame

#print(df)                                                      #print whole data set
#print(df.info())                                               #gives number of rows and columns along with datatype of each column
#for index,rows in df.iterrows():                               #iterate through rows
#    print(index,rows) 
#    print(index,rows["Name"])                                  #iterate through specific data row wise
#    print()

a=df.head(4)                                                    #to load some of the starting data if no argument is passed first 5 rows are shown
a=df.tail(3)                                                    #to load some of the ending data
a=df.shape                                                      #gives a tuple of number of rows and columns
a=df.columns                                                    #for headers of files
a=df["Name"]                                                    #print a column can use df.Name also
a=df["Name"][0:5]                                               #print a column till a specific range
a=df[:2]                                                        #print data frame upto range
a=df[["Name","Type 1","HP"]]                                    #print multiple columns
a=df.iloc[1]                                                    #iloc-integer location-gives every detail in the row
a=df.iloc[1:4]                                                  #multiple rows
a=df.iloc[2,1]                                                  #read a specific column of specific row(row first)
a=df.T                                                          #transpose a data frame
a=df.loc[(df["Type 1"]=="Fire")&(df["Type 2"]=="Flying")]       #get data following specific conditions
a=df.describe()                                                 #gives advanced details like mean, standard deviation etc
a=df.sort_values("Name")                                        #sort data according by some column
a=df.sort_values("Name",ascending=False)                        #sort data according by some column in reverse order
a=df.sort_values(["Name","Attack"],ascending=[0,1])             #sort data according multiple columns 1-True 0-False
a=df['Type 1'].unique()                                         #storing unique values
a=df.value_counts()                                             #counts unique values

#changing data
df['Owner']='Ash'                                               #Add new column with fixed value for every row
df=pd.DataFrame(df,columns=['#','Name','Type 1','Type 2','HP','Attack','Defense',
                            'Sp. Atk','Sp. Def','Speed','Generation','Legendary','Owner'])   #add new column with Nill entry
#df["Total"]=df["HP"]+df["Attack"]+df["Defense"]+df["Sp. Atk"]+df["Sp. Def"]+df["Speed"]     #add column with specific condition
#another way of adding/creating 
df["Total"]=df.iloc[:,4:10].sum(axis=1)                         #axis=1 row wise
df.index.name='Index'                                           #give title/name to index
df.columns.name='Columns'                                       #give title/name to column list

#shift a column
cols=list(df.columns)
df=df[cols[0:10]+[cols[-1]]+cols[10:12]]                        

#drop is used to remove row and columns
data=df.drop(columns=["Speed"])                                 #to drop a column,for multiple columns use list ofcolumns name                      
#using drop with help of axis
data=df.drop('#',axis=1)                                        #droping column
data=data.drop(0,axis=0)                                        #to drop a row use indexing,for multiple rows use list of indexes


#saving data
df.to_csv(r"E:\Programs\Python\Pandas\Modified.csv",index=False)                           #copies the data frame df to a file and removes indexing(optional)
df.loc[(df["Type 1"]=="Fire")&(df["Type 2"]=="Flying")]         #get data following specific conditions
#a=a.reset_index()                                              #to reset index.This will create a new column holding old index
#a=a.reset_index(drop=True)                                     #removes the old indexing
a.reset_index(drop=True,inplace=True)                           #if don't want to reset in new data frame
df.loc[df["Name"].str.contains("Mega")]                         #to look for specific data within a column
df.loc[~df["Name"].str.contains("Mega")]                        #to look for specific data within a column(not included/reverse)
#all RegEx expressions can be used inside conatins method


#conditional changes
df.loc[df["Type 1"]=="Fire","Type 1"]="Flame"                   #changes fire in type 1 to flames
df.loc[df["Type 1"]=="Flame","Legendary"]=True                  #use one condition to set the parameter for another column
df=pd.read_csv(r"E:\Programs\Python\Pandas\Modified.csv")

#df.loc[df["Total"] > 600,["Generation","Legendary"]]=["12",True]
#multiple conditions can be modified in a single time


#Groupby for aggregate statistics- has majorly three functions sum,mean and count.Multiple values can be passed
datas=df.groupby(["Type 1"]).mean(numeric_only=True).sort_values("Attack",ascending=False)
#groups data according to column and find mean and sort them descendingly of attack parameter

df.groupby(["Type 1"]).sum()                                    #groups data according to column and find sum of all values of row parameters
df["count"]=1
df.groupby(["Type 1","Type 2"]).count()["count"]                #counts data having same column 

#Creating new Data Frame
new_df=pd.DataFrame(columns=df.columns)                         #creates new empty data frame with same columns as given data frame
#can read large files in small chunks
# for df in pd.read_csv("D:\Programs\Python\Pandas\Modified.csv",chunksize=5):              #here df represents 5 rows of the file 
#     print("Chunk")
#     print(df)

#User defined Data frame
data={"states":["Ohio","Ohio","Ohio","Nevada","Nevada","Nevada"],
     "year":[2000,2001,2002,2001,2002,2003],
     "pop":[1.5,1.7,3.6,2.4,2.9,3.2]}
frame2=pd.DataFrame(data)                                       #make our data into frames
frame2["pass"]=np.arange(6.)                                    #range should be equal to number of columns range should be equal to number of rows



data=pd.DataFrame(np.arange(16).reshape((4,4)),index=["ohio","colorado","Utah","New York"],columns=["one","two","three","four"])
data[data<5]=0                                                  #setting a specific value to whole data frame satisfying condition can be applied on numeric data only
change=data.rename(index=str.title,columns=str.upper)
#title- returns a string where first character of every string is in upper case
#upper-converts whole string in uppercase

change=data.rename(index={'ohio':"Indiana"},columns={'three':'Count'})     #renaming index and columns


#Series Data
obj=pd.Series([3,5,1,9])                                        #Series is a one-dimensional array like object containing a sequence of value
#print(obj)                                                     #prints values along with respective index
obj=pd.Series([3,5,1,9],index=['a','b','c','d'])                #provide user defined indexing
obj=obj.reindex(['b','a','d','c'])                              #change previous indexing
change=obj['b']                                                 #Access single element of Series by index
change=obj[['b','c']]                                           #Access multiple elements of Series by index
change=obj[2:4]                                                 #Access element through slicing
change=obj[obj<3]                                               #Apply condition to Series data
change=obj.replace(9,np.nan)                                    #replace a value for multiple values use list of values
change=obj.replace({9:23,5:47})                                 #replace multiple values with other particular values
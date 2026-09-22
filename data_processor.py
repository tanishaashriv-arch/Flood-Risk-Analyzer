import pandas as pd#importing panda library 

def data(file_path):#defining a new function called data with my csv file address as argument
    df = pd.read_csv(file_path)#loads my csv file and converts to dataframe
    
    #clean the data by dropping missing values 
    simpledf = df.dropna()
    
    #for this project, we will focus on the 'ANNUAL' total rainfall
    # We only keep the Region, the Year, and the Annual total to keep it simple
    finaldata = simpledf[['SUBDIVISION', 'YEAR', 'ANNUAL']].copy()#clone dataset containing only the specified details
    
    return finaldata
import numpy as np

def findanomalies(df):
    mean_rainfall = np.mean(df['ANNUAL'])#calculates mean rainfall over the year
    sd_rainfall = np.std(df['ANNUAL'])#calculates standard deviation of rainfall over the year
    df['Z_SCORE'] = (df['ANNUAL'] - mean_rainfall) / sd_rainfall# Z-score formula: (Value - Mean) / Standard Deviation
    extreme_events = df[df['Z_SCORE'] >= 3.0].copy()# flag an extreme event if the Z-score is 3 or higher,this means the rainfall was exceptionally heavier than normal
    
    return extreme_events
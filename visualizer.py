import matplotlib.pyplot as plt
import numpy as np

def plot_trends(extreme_rain):
    x = extreme_rain['YEAR'].values#x is the years extreme rainfall took place
    y = extreme_rain['ANNUAL'].values#y is the amount of rainfall in those years
    
    # use NumPy to calculate a linear regression (line of best fit)
    # the '1' means we want a straight line
    slope, intercept = np.polyfit(x, y, 1)
    trendline = (slope * x) + intercept#y=mx+b
    plt.figure(figsize=(10, 6))#blank cavas that is 10 inches on x axis and 6 inches on y axis
    plt.scatter(x, y, color='red', label='Extreme Rainfall Events')#stamps a red dot for extreme outlier years
    plt.plot(x, trendline, color='blue', linestyle='--', label=f'Trendline (Slope: {slope:.2f})')#draw the trendline to see if extremes are increasing over time
    
    #add labels and a title to make it readable
    plt.title('Extreme Rainfall Events in India (1901-2015)')
    plt.xlabel('Year')
    plt.ylabel('Annual Rainfall (mm)')
    plt.legend()
    plt.grid(True)
    
    if slope > 0:
        plt.figtext(0.15, 0.15, f"CONCLUSION: Increasing intensity (Slope: {slope:.2f})", fontsize=10, bbox=dict(facecolor='white', alpha=0.8))
    else:
        plt.figtext(0.15, 0.15, f"CONCLUSION: Decreasing intensity (Slope: {slope:.2f})", fontsize=10, bbox=dict(facecolor='white', alpha=0.8))
    
    # 6. Show the final graph
    plt.show()
    
    return slope
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x='Year',y='CSIRO Adjusted Sea Level', data=df, color = 'r', marker='.')

    # Create first line of best fit

    first_fit = linregress(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])
    years1 = [df['Year'].min() + i for i in range(2051 - df['Year'].min())]
    y_pred1 = [first_fit.intercept + first_fit.slope * year for year in years1]
    ax.plot(years1, y_pred1)
    # Create second line of best fit

    df_above2000 = df[df['Year']>=2000]
    second_fit = linregress(x=df_above2000['Year'],y=df_above2000['CSIRO Adjusted Sea Level'])
    years2 = [df_above2000['Year'].min() + i for i in range(2051 - df_above2000['Year'].min())]
    y_pred2 = [second_fit.intercept + second_fit.slope * year for year in years2]
    ax.plot(years2, y_pred2)

    # Add labels and title

    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    x_ticks = [1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075]
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_ticks)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
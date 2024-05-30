import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
     (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():

    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot(ax=ax, color='r')

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    plt.savefig("line_plot.png")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    
    df_bar=df.copy()
    df_bar['year'] = df.index.year
    df_bar['month'] = df.index.month
    df_grouped = df_bar.groupby(['year', 'month'])['value'].sum().unstack()

    fig, ax = plt.subplots(figsize=(14, 8))

    df_grouped.plot(kind='bar', ax=ax)

    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    ax.legend(title='Month', labels= ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December'])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    fig, axs = plt.subplots(2, 1, figsize=(14, 16))

    # Plot year-wise box plot
    sns.boxplot(x='year', y='value', data=df_box, ax=axs[0], palette='pastel')
    axs[0].set_title("Year-wise Box Plot (Trend)")
    axs[0].set_xlabel("Year")
    axs[0].set_ylabel("Page Views")

    # Plot month-wise box plot
    sns.boxplot(x='month', y='value', data=df_box, order=month_order, ax=axs[1], palette='pastel')
    axs[1].set_title("Month-wise Box Plot (Seasonality)")
    axs[1].set_xlabel("Month")
    axs[1].set_ylabel("Page Views")


    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

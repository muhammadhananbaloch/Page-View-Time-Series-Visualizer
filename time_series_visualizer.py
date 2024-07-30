import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=[0], index_col='date')

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025))  & (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(18,6))
    plt.plot(df.index, df['value'], color='firebrick')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df.index.year
    df_bar['month'] = df.index.month_name()
    months = ["January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December"]
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=months)
    df_bar_agg = df_bar.groupby(['year', 'month'], observed=True)['value'].mean().unstack()

    # Draw bar plot
    fig = df_bar_agg.plot(kind='bar').get_figure()
    plt.ylabel('Average Page Views')
    plt.xlabel('Years')
    plt.legend(title='Months')
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
              "Sep", "Oct", "Nov", "Dec"]
    df_box['month'] = pd.Categorical(df_box['month'], categories=months)

    fig = plt.figure(figsize=(18,6))
    plt.subplot(121)
    sns.boxplot(data=df_box, x=df_box['year'], y=df_box['value'])
    plt.xlabel("Year")
    plt.ylabel('Page Views')
    plt.title('Year-wise Box Plot (Trend)')
 
    plt.subplot(122)
    sns.boxplot(data=df_box, x=df_box['month'], y=df_box['value'])
    plt.xlabel("Month")
    plt.ylabel('Page Views')
    plt.title('Month-wise Box Plot (Seasonality)')
    
    plt.show()


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2

df = df.assign(overweight=lambda x: (x['weight'] / (x['height'] * 0.01) ** 2 > 25).astype('bool'))

# 3

df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1

df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1


# 4


def draw_cat_plot():
    df_cat = df[['cardio', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']]

    df_cat = pd.melt(df_cat, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name='feature', value_name='value')

    df_cat = df_cat.groupby(['cardio', 'feature', 'value']).size().reset_index(name='count')

    g = sns.catplot(data=df_cat,
                    x='feature',
                    y='count',
                    hue='value',
                    col='cardio',
                    kind='bar',
                    height=4,
                    aspect=1.2)

    g.set_axis_labels("variable", "total")  # Adjust the y-axis label to 'total'
    g.set_titles("cardio = {col_name}")

    g.savefig('catplot.png')
    
    return g.fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
            (df['height'] >= df['height'].quantile(0.025)) & 
            (df['height'] <= df['height'].quantile(0.975)) & 
            (df['weight'] >= df['weight'].quantile(0.025)) & 
            (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr().round(1)

    # 13
    mask = np.triu(np.ones_like(corr, dtype= bool))

    # 14
    fig, ax = plt.subplots(figsize=(10, 8))

    # 15
    sns.heatmap(corr, mask=mask, vmin=corr.min().min(), vmax=corr.max().max(), fmt=".1f", annot=True, cmap='BrBG', ax=ax)

    # 16
    fig.savefig('heatmap.png')
    return fig

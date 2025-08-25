import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

df = pd.read_csv('for Ethan(Vol Graph).csv')
df['datetime'] = pd.to_datetime(df['Timestamp'], format='%m/%d/%y %I:%M %p')
df['warrant_price'] = df['option price']
df['implied_vol'] = df['Implied Vol'] * 100

plt.style.use('default')
fig = plt.figure(figsize=(15, 12))

def plot_iv_over_time(ax):
    percentiles = df['implied_vol'].quantile([0.05, 0.25, 0.5, 0.75, 0.95])
    ax.plot(df['datetime'], df['implied_vol'], 'b-', linewidth=1)
    colors = ['red', 'orange', 'green', 'orange', 'red']
    for (p, v), c in zip(percentiles.items(), colors):
        ax.axhline(y=v, color=c, linestyle='--', alpha=0.5)
    ax.set_title('Warrant Implied Volatility Analysis\nImplied Volatility Over Time')
    ax.set_ylabel('Implied Volatility (%)')
    ax.grid(True, alpha=0.3)

def plot_iv_distribution(ax):
    ax.hist(df['implied_vol'], bins=30, density=True, alpha=0.7, color='skyblue')
    colors = ['red', 'orange', 'green', 'orange', 'red']
    for p, c in zip([0.05, 0.25, 0.5, 0.75, 0.95], colors):
        val = df['implied_vol'].quantile(p)
        ax.axvline(val, color=c, linestyle='--', alpha=0.5)
    ax.set_title('IV Distribution')
    ax.set_xlabel('Implied Volatility (%)')
    ax.set_ylabel('Density')
    ax.grid(True, alpha=0.3)

def plot_intraday_pattern(ax):
    df['hour'] = df['datetime'].dt.hour
    hourly = df.groupby('hour')['implied_vol'].agg(['mean', 'std']).reset_index()
    ax.plot(hourly['hour'], hourly['mean'], color='purple', marker='o')
    ax.fill_between(hourly['hour'], 
                   hourly['mean'] - hourly['std'],
                   hourly['mean'] + hourly['std'],
                   alpha=0.3, color='purple')
    ax.set_title('Intraday IV Patterns')
    ax.set_xlabel('Hour of Day')
    ax.set_ylabel('Average IV (%)')
    ax.grid(True, alpha=0.3)

def plot_iv_vs_price(ax):
    ax.scatter(df['warrant_price'], df['implied_vol'], alpha=0.5, color='blue', s=20)
    ax.set_title('IV vs Warrant Price')
    ax.set_xlabel('Warrant Price')
    ax.set_ylabel('Implied Volatility (%)')
    ax.grid(True, alpha=0.3)

ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)

plot_iv_over_time(ax1)
plot_iv_distribution(ax2)
plot_intraday_pattern(ax3)
plot_iv_vs_price(ax4)

plt.tight_layout()
plt.savefig('warrant_iv_analysis.png', dpi=300, bbox_inches='tight')
plt.close()
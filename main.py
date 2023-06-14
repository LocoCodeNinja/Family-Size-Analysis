import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 20, 10

df = pd.read_csv('data/stcfamilysizecsvv2.02012-09-19.csv')

# Print first five datasets
print(df.head(5))

# Subsetting/Retrieve only Family Size and Proportion (%)
df = df[['Family Size', 'Proportion (%)']]
print(df.head(20))

# Filter the data for a specific geography or family size
filtered_data = df[df['Geography'] == 'Canada']

# Group the filtered data by year and calculate the mean proportion
grouped_data = filtered_data.groupby('Year')['Proportion (%)'].mean()

# Plotting the line chart
plt.plot(grouped_data.index, grouped_data.values)
plt.xlabel('Year')
plt.ylabel('Proportion (%)')
plt.title('Proportion of Family Size over Years')
plt.show()

# Group the data by family size and calculate the mean proportion
grouped_data = df.groupby('Family Size')['Proportion (%)'].mean()

# Plotting the bar chart
plt.bar(grouped_data.index, grouped_data.values)
plt.xlabel('Family Size')
plt.ylabel('Proportion (%)')
plt.title('Average Proportion of Family Size')
plt.xticks(rotation=45)
plt.show()

# Filter the data for specific geographies
filtered_data = df[df['Geography'].isin(['Canada', 'Newfoundland and Labrador', 'Ontario'])]

# Group the filtered data by year and geography and calculate the mean proportion
grouped_data = filtered_data.groupby(['Year', 'Geography'])['Proportion (%)'].mean().unstack()

# Plotting the multiple line plots
grouped_data.plot(marker='o')
plt.xlabel('Year')
plt.ylabel('Proportion (%)')
plt.title('Proportion of Family Size in Different Geographies')
plt.legend(title='Geography')
plt.show()

# Calculate the average data for each year
df['Data'] = np.random.rand(len(df))
average_data = df.groupby('Year')['Data'].mean()

# Display the average data
print(average_data)
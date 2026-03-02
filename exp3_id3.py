# EXPERIMENT 3
# ID3 Algorithm - Play Tennis Dataset

import math
import pandas as pd

# Dataset
data = {
    'Outlook': ['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast',
                'Sunny','Sunny','Rain','Sunny','Overcast','Overcast','Rain'],
    'Temperature': ['Hot','Hot','Hot','Mild','Cool','Cool','Cool',
                    'Mild','Cool','Mild','Mild','Mild','Hot','Mild'],
    'Humidity': ['High','High','High','High','Normal','Normal','Normal',
                 'High','Normal','Normal','Normal','High','Normal','High'],
    'Wind': ['Weak','Strong','Weak','Weak','Weak','Strong','Strong',
             'Weak','Weak','Weak','Strong','Strong','Weak','Strong'],
    'PlayTennis': ['No','No','Yes','Yes','Yes','No','Yes',
                   'No','Yes','Yes','Yes','Yes','Yes','No']
}

df = pd.DataFrame(data)

# Entropy function
def entropy(target_col):
    elements, counts = target_col.value_counts().index, target_col.value_counts().values
    entropy = 0
    for i in range(len(elements)):
        p = counts[i]/sum(counts)
        entropy += -p * math.log2(p)
    return entropy

# Information Gain
def information_gain(data, split_attribute, target="PlayTennis"):
    total_entropy = entropy(data[target])
    vals, counts = data[split_attribute].value_counts().index, data[split_attribute].value_counts().values
    
    weighted_entropy = 0
    for i in range(len(vals)):
        subset = data[data[split_attribute] == vals[i]]
        weighted_entropy += (counts[i]/sum(counts)) * entropy(subset[target])
        
    return total_entropy - weighted_entropy

# Calculate Information Gain for all attributes
attributes = ['Outlook', 'Temperature', 'Humidity', 'Wind']

print("Information Gain Values:\n")
for attr in attributes:
    print(attr, ":", round(information_gain(df, attr), 3))

# Classification of new sample
print("\nNew Sample: Outlook=Sunny, Humidity=High")
print("Prediction: PlayTennis = No")

import csv

# Load CSV file
with open('training_data.csv') as file:
    reader = list(csv.reader(file))
    data = reader[1:]  # Remove header

num_attributes = len(data[0]) - 1

# Initialize S and G
S = data[0][:-1]
G = [["?" for _ in range(num_attributes)]]

print("\nInitial S:", S)
print("Initial G:", G)

for row in data:
    if row[-1] == "Yes":  # Positive Example
        for i in range(num_attributes):
            if S[i] != row[i]:
                S[i] = "?"
                
    else:  # Negative Example
        for i in range(num_attributes):
            if S[i] != row[i]:
                G.append(["?" if j != i else S[i] for j in range(num_attributes)])

print("\nFinal Specific Boundary S:", S)
print("Final General Boundary G:")
for g in G:
    print(g)

import pandas as pd

df = pd.read_excel('homework.xlsx')

print("Rows where score is NaN")
print(df[df['score'].isnull()])

print("Rows where score is between a and b")
a = float(input("Enter minimum score: "))
b = float(input("Enter maximum score: "))
print(df[(df['score'] >= a) & (df['score'] <= b)])

print("Sort by score")
print(df.sort_values('score'))

print("Sort by name")
print(df.sort_values('name'))

print("Add new row")
new_row = {'name': input("Enter name: "),
           'score': float(input("Enter score: ")),
           'attempts': int(input("Enter attempts: ")),
           'qualify': 'yes'}

new_df = pd.DataFrame([new_row])

df = pd.concat([df, new_df], ignore_index=True)

print("Remove row by index")
index = int(input("Enter index to remove: "))
df.drop(index, inplace=True)

print("Save qualified students")
qualified = df[df['qualify'] == 'yes'][['name', 'score']]
qualified.to_excel('qualified_students_2.xlsx', index=False)

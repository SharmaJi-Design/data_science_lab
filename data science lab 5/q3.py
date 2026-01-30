# 3. Select rows where Marks > 60. 
import pandas as pd

df = pd.read_csv('data.csv')

high_marks = df[df['Marks'] > 60] 

high_marks_selected = high_marks[['Name', 'Marks']]

print(high_marks_selected)


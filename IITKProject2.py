import matplotlib.pyplot as plt
import pandas as pd

# Load the datasets
animal_data = pd.read_csv( "../IITPRACTICALSQL/DataSet_Animal_Center_Intakes.csv" )
outcome_data = pd.read_csv( "../IITPRACTICALSQL/DataSet_Animal_Center_Outcomes.csv" )

# Project Task-01: Print the shape of the dataset
print("Shape of the dataset:", animal_data.shape)

# Project Task-02: Which column has null values?
print("Columns with null values:\n", animal_data.isnull().sum())

# Project Task-03: Remove the duplicate rows from intake dataset.
animal_data.drop_duplicates(inplace=True)

# Project Task-04: Rename column names
new_column_names = {
    'Animal ID': 'id',
    'DateTime': 'date_time',
    'MonthYear': 'month_year',
    'Found Location': 'found_location',
    'Intake Type': 'intake_type',
    'Intake Condition': 'intake_condition',
    'Animal Type': 'animal_type',
    'Sex upon Intake': 'sex_upon_intake',
    'Age upon Intake': 'age_upon_intake',
    'Breed': 'breed'
}
animal_data.rename(columns=new_column_names, inplace=True)

# Project Task-05: Remove Monthyear column because it is similar to Datetime column.
animal_data.drop('month_year', axis=1, inplace=True)

# Project Task-06: Extracting month and year from Datetime column
animal_data['year'] = pd.to_datetime(animal_data['date_time']).dt.year
animal_data['month'] = pd.to_datetime(animal_data['date_time']).dt.month

# Project Task-07: Which month, year has the most animal intakes?
yearly_intake_counts = animal_data['year'].value_counts()
plt.pie(yearly_intake_counts, labels=yearly_intake_counts.index, autopct='%1.1f%%')
plt.title("Year-wise Animal Intake from 2014 to 2021")
plt.show()

# Project Task-08: Create a bar chart to represent month-wise animal intake.
monthly_intake_counts = animal_data['month'].value_counts()
plt.bar(monthly_intake_counts.index, monthly_intake_counts.values)
plt.xlabel('Month')
plt.ylabel('Animal Intake Count')
plt.title("Month-wise Animal Intake")
plt.show()

# Project Task-09: Create a bar chart to represent animal intake methods wise counting.
animal_intake_methods = animal_data['intake_type'].unique()
animal_intake_counts = animal_data['intake_type'].value_counts()
plt.bar(animal_intake_methods, animal_intake_counts)
plt.xlabel('Intake Type')
plt.ylabel('Count')
plt.title("Animal Intake Methods")
plt.show()

# Project Task-10: What are the conditions of animals which are taken into the shelter?
animal_conditions = animal_data['intake_condition'].unique()
print("Conditions of animals taken into the shelter:", animal_conditions)

# Project Task-11: How many types of animals are taken into shelter and what is their total count?
animal_types_count = animal_data['animal_type'].value_counts()
print("Types of animals taken into the shelter:")
print(animal_types_count)

# Project Task-12: What are the top 10 breeds in the animal shelter?
top_10_breeds = animal_data['breed'].value_counts().head(10)
plt.bar(top_10_breeds.index, top_10_breeds.values)
plt.xlabel('Breed')
plt.ylabel('Count')
plt.title("Top 10 Breeds in the Animal Shelter")
plt.xticks(rotation=90)
plt.show()

# Project Task-13: What are the top 20 common names of animals in the animal shelter?
top_20_names = animal_data['Name'].value_counts().head(20)
plt.bar(top_20_names.index, top_20_names.values)
plt.xlabel('Name')
plt.ylabel('Count')
plt.title("Top 20 Common Names of Animals in the Animal Shelter")
plt.xticks(rotation=90)
plt.show()

# Project Task-14: Draw a bar chart representing the "Outcome Type" wise count of animals
outcome_counts = outcome_data['Outcome Type'].value_counts()
plt.bar(outcome_counts.index, outcome_counts.values)
plt.xlabel('Outcome Type')
plt.ylabel('Count')
plt.title("Outcome Type Wise Count of Animals")
plt.xticks(rotation=90)
plt.show()

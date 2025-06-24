import csv
import pandas as pd


#with open('aac_shelter_outcomes.csv', 'r') as file:
 #   reader = csv.DictReader(file)
  #  for row in reader:
   #     print(row['age_upon_outcome'], row['animal_id'],row['breed'], row['color'], row['date_of_birth'], row['datetime'], row['monthyear'],
     #         row['name'], row['outcome_subtype'], row['outcome_type'], row['sex_upon_outcome'], row['location_lat'], row['location_long'],
      #        row['age_upon_outcome_in_weeks'])

df = pd.read_csv('aac_shelter_outcomes.csv')

df.to_html('aac.html')
import random
import numpy as np
import pandas as pd

# Read the Excel file with workouts listed.
df = pd.read_excel('/Users/omarbailey/Documents/Gym/Omar Random Workout Generator.xlsx')

# Fill null values with Don't Use
df= df.fillna('Dont Use')

# Create a function that reads type of workout someone wants and the number of exercises they want to do.
def workout_generator(type_of_workout, num_exercises):
    type_of_workout = str(type_of_workout).lower()
    num_exercises = int(num_exercises)
    try:
        if type_of_workout == 'legs':
            type_of_workout = 'Leg Workouts'
        if type_of_workout == 'pull' or type_of_workout == 'back' or type_of_workout =='arms':
            type_of_workout = 'Upper Body Pull Workout'
        if type_of_workout == 'push' or type_of_workout == 'chest' or type_of_workout == 'shoulders':
            type_of_workout = 'Upper Body Push Workout'

        # Convert Specified Workout Column and workout_type into List
        workout_list = df[type_of_workout].to_list()
        workout_type = df['Types of Workout'].tolist()

        # Convert workout_list and workout_type into Set to eliminate repeating values), remove single 'Don't Use' value, and revert back to list
        workout_list = set(workout_list)
        if 'Dont Use' in workout_list:
            workout_list.remove('Dont Use')
        workout_list = list(workout_list)

        workout_type = set(workout_type)
        workout_type.remove('Dont Use')
        workout_type = list(workout_type)

        # Returns randomized workout of exercises for specified body part + the type of workout to be done.
        rand_workout = ', '.join(map(str,random.sample(workout_list, num_exercises)))
        rand_workout_type = ''.join(map(str,random.sample(workout_type, 1)))

        return rand_workout + '\n'*2 + rand_workout_type

    #  If user inputs wrong information.
    except:
        return 'Invalid Input. Please Try Again.'

# Allows user to insert body part to work out and number of exercises
print(workout_generator(input('What body part do you want to workout? '), input('How many exercises do you want to do? ')))
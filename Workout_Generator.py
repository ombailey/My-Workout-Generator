import random
import pandas as pd

# Read the Excel file with workouts listed.
df = pd.read_excel('/Users/omarbailey/Documents/Gym/Omar Random Workout Generator.xlsx')

# Fill null values with Don't Use
df= df.fillna('Dont Use')

# Asks the user what body part(s) they want to workout and how many exercises than generates a workout for them.
def workout_generator(body_part_to_workout, num_exercises):
    final_workout = ''
    num = 0
    # Create different steps for if one body part is specified or multiple.
    if 'and' in body_part_to_workout:
        list_body_parts = body_part_to_workout.split('and')
        for body_part in list_body_parts:
            list_body_parts[num] = str(body_part).lower().strip()
            num +=1
    else:
        list_body_parts = [str(body_part_to_workout).lower()]
    num_exercises = int(num_exercises)
    # Convert body parts specified to exercise to their corresponding list of exercises
    try:
        for body_part in list_body_parts:
            if body_part == 'legs' or body_part_to_workout == 'lower body':
                body_part_to_workout = 'Leg Workouts'
            elif body_part == 'pull':
                body_part_to_workout = 'Upper Body Pull Workout'        
            elif body_part == 'back':
                body_part_to_workout = 'Back Workouts'
            elif body_part == 'push':
                body_part_to_workout = 'Upper Body Push Workout'
            elif body_part == 'chest':
                body_part_to_workout = 'Chest Workouts'
            elif body_part == 'abs':
                body_part_to_workout = 'Ab Workouts'
            elif body_part == 'shoulders' or body_part == 'shoulder':
                body_part_to_workout = 'Shoulder Workouts'
            elif body_part == 'biceps' or body_part == 'bicep':
                body_part_to_workout = 'Bicep Workouts'
            elif body_part == 'triceps' or body_part == 'tricep':
                body_part_to_workout = 'Tricep Workouts'
            elif body_part == 'arms':
                body_part = input('Biceps or Triceps or Both? ')
                body_part = str(body_part).lower()
                if body_part == 'biceps' or body_part == 'bicep':
                    body_part_to_workout = 'Bicep Workouts'
                elif body_part == 'triceps' or body_part == 'tricep':
                    body_part_to_workout = 'Tricep Workouts'
                elif body_part == 'both':
                    list_body_parts.extend(['triceps', 'biceps'])
                    continue
                else:
                    return 'Invalid Input. Please Try Again.' 
            elif body_part == 'upper body':
                body_part = input('Push or Pull for Upper Body? ')
                body_part = str(body_part).lower()
                if body_part == 'push':
                    body_part_to_workout = 'Upper Body Push Workout'
                elif body_part == 'pull':
                    body_part_to_workout = 'Upper Body Pull Workout'
                else:
                    return 'Invalid Input. Please Try Again.'

        # Convert Specified Body Part Workout Column and workout_type into List
            workout_list = df[body_part_to_workout].to_list()
            if body_part_to_workout == 'Ab Workouts':
                workout_type = df['Ab Sets'].tolist()
            else:
                workout_type = df['Types of Workout'].tolist()

        # Convert workout_list and workout_type into Set to eliminate repeating values, remove single 'Don't Use' value, and revert back to list
            workout_list = set(workout_list)
            if 'Dont Use' in workout_list:
                workout_list.remove('Dont Use')
            workout_list = list(workout_list)

            workout_type = set(workout_type)
            if 'Dont Use' in workout_type:
                workout_type.remove('Dont Use')
            workout_type = list(workout_type)

        # Returns randomized workout of exercises for specified body part + the type of workout to be done.
            rand_workout = '\n'.join(map(str,random.sample(workout_list, num_exercises)))
            rand_workout_type = ''.join(map(str,random.sample(workout_type, 1)))

            final_workout = final_workout + '\n'*2 + rand_workout + '\n'*2 + rand_workout_type 

    # return 'Workout For Today' + '\n'*2 + rand_workout + '\n'*2 + rand_workout_type
        return '\n' + 'Workout for Today' + final_workout
    #  If user inputs wrong information.
    except:
        return 'Invalid Input. Please Try Again.'

# Allows user to insert body part to work out and number of exercises
print(workout_generator(input('What body part(s) do you want to workout? '), input('Number of Exercises(Per Body Part if Multiple)? ')))
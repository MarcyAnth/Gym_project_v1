from itertools import zip_longest
import math
from muscle_def import programs
from itertools import chain, zip_longest



lifts = ["Bench" ,"Squat" ,"Deadlift"]
one_rep_maxes_list = []
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
num_of_days = []
times_week_training = 0
final_week_program = []



def orp_calc(weight):
    return math.ceil(float(weight*(36/(37-10))))


def eighty_percent(weight):
    return math.ceil(float(weight*0.8))


def one_rep_max(one_rep_maxes_list):
 for item in lifts:
    rpe_10 = int(input(f"Please input a weight you can do 10 reps for {item}: "))
    one_rep_maxes_list.append(orp_calc(rpe_10))
    print(f"Your 1RM is {(orp_calc(rpe_10))}")
 return one_rep_maxes_list


print("Welcome to the Beginner Powerlifitng Program!")
welcome = input("A key thing before we start is figuring out your one rep maxes. Type 'go' to proceed: ")
if welcome == "go":
    one_rep_max(one_rep_maxes_list)


bench = one_rep_maxes_list[0]
squat = one_rep_maxes_list[1]
deadlift = one_rep_maxes_list[2]


def workout_chooser():
    print(f"We have now established your max for bench is {bench}kg, squat is {squat}kg and deadlift is {deadlift}kg. "
          f'Theres a few programs that can work, which are {programs}.')
    program_choice = input("Please choose your option by referring to it's full name: ")
    if program_choice in programs:
        print(f"{programs[program_choice]}")




def workout():
    print(f"We have now established your max for bench is {bench}kg, squat is {squat}kg and deadlift is {deadlift}kg. "
          f'A standard powerlifitng program is {programs["5by5"]}'
          f". Based on your current 1RM the results will be: \nBench = {eighty_percent(bench)}kg. "
          f"\nSquat = {eighty_percent(squat)}kg \n"
          f"Deadlift = {eighty_percent(deadlift)}kg ")


def days_training(num_of_days):
    num_of_days_training = int(input("How many days a week would you like to train?"))
    final_days = num_of_days_training + times_week_training

    for day in range(final_days):
        days = input(f"{days_of_week}")
        num_of_days.append(days)
        if days in days_of_week:
            days_of_week.remove(days)
    return


def merge():
    final_week_program = [*zip_longest(num_of_days, lifts, fillvalue="Accessory work/Cardio")]
    print(final_week_program)
    return final_week_program


workout_chooser()
days_training(num_of_days)
merge()

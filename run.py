from main import one_rep_max, eighty_percent, orp_calc, workout, days_training,merge


lifts = ["Bench" ,"Squat" ,"Deadlift"]
one_rep_maxes_list = []
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
num_of_days = []
times_week_training = 0
final_week_program = []


orp_calc()
eighty_percent()
one_rep_max(one_rep_maxes_list)


print("Welcome to the Beginner Powerlifitng Program!")
welcome = input("A key thing before we start is figuring out your one rep maxes. Type 'go' to proceed: ")
if welcome == "go":
    one_rep_max(one_rep_maxes_list)


bench = one_rep_maxes_list[0]
squat = one_rep_maxes_list[1]
deadlift = one_rep_maxes_list[2]

workout()
days_training(num_of_days)
merge()
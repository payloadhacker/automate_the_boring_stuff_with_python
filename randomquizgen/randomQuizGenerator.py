import random

Capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 
'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 
'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 
'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 
'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 
'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 
'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 
'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 
'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 
'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia','West Virginia':'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

#generating 35 quiz files and answers(files will be saved in a quiz 
#folder on the desktop)
 
for quiz_num in range(35):
    quiz_file = open(rf'C:\Users\USER\Desktop\automate_the_boring_stuff_with_python\randomquizgen\capitalsquiz{quiz_num + 1}.txt', 'w', encoding='utf-8')
    quiz_answers = open(rf'C:\Users\USER\Desktop\automate_the_boring_stuff_with_python\randomquizgen\capitalsquiz_answers{quiz_num +1}.txt', 'w', encoding='utf-8' )

    #quiz header
    quiz_file.write('Name:\nDate:\nPeriod:\n\n')
    quiz_file.write(' '*20 + f'State Capitals Quiz {quiz_num + 1}')
    quiz_file.write('\n\n')

    #shuffling the states
    states = list(Capitals.keys())
    random.shuffle(states)

    #getting the correct and wrong then randomizing the answers
    for num in range(len(states)):
        correct_answer = Capitals[states[num]]
        wrong_answers = list(Capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer] 
        random.shuffle(answer_options)

    for num in range(50):
        quiz_file.write(f"{num + 1}. Capital of {states[num]}: \n")
        for i in range(4):
            quiz_file.write(f"   {'ABCD'[i]}. {answer_options[i]}\n")
        quiz_file.write('\n')

        #writing the answers to the answer file
        quiz_answers.write(f"{num + 1}.{'ABCD'[answer_options.index(correct_answer)]}\n")

quiz_file.close()
quiz_answers.close()
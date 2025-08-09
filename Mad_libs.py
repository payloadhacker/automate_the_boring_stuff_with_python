with open(f'mad_lib.txt', 'w') as file:
    file.write(f'''The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was 
unaffected by these events.''')

with open('mad_lib.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = text.split()

for i in range(len(words)):
    if  'ADJECTIVE'in words[i]:
        words[i] = input("Enter an adjective: ")
        words[i].replace('ADJECTIVE', words[i])
    elif words[i] == 'NOUN':
        words[i] = input("Enter a noun: ")
        words[i].replace('NOUN', words[i])
    elif words[i] == 'VERB':
        words[i] = input("Enter a verb: ")
        words[i].replace('VERB', words[i])

final_text= (' '.join(words))

with open('mad_lib_completed.txt', 'w', encoding='utf-8') as file:
    file.write(final_text)
print("\nYour completed Mad Libs story:")
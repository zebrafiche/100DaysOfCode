#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Letters/starting_letter.txt') as file:
    mail_text = file.read()
    # print(mail_text)

with open('./Input/Names/invited_names.txt') as file:
    names_list = file.readlines()
    # print(names_list)

for i in names_list:
    name = i.strip('\n')
    new_mail_text = mail_text.replace('[name]', name)
    # print(new_mail_text)
    with open(f"./Output/ReadyToSend/Letter for {name}.txt", 'w') as output_file:
        output_file.write(new_mail_text)

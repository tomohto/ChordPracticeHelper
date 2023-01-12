import random
notes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
intro = r"""
 _______           _______  _______  ______     _______  _______  _______  _______ __________________ _______  _______ 
(  ____ \|\     /|(  ___  )(  ____ )(  __  \   (  ____ )(  ____ )(  ___  )(  ____ \\__   __/\__   __/(  ____ \(  ____ \
| (    \/| )   ( || (   ) || (    )|| (  \  )  | (    )|| (    )|| (   ) || (    \/   ) (      ) (   | (    \/| (    \/
| |      | (___) || |   | || (____)|| |   ) |  | (____)|| (____)|| (___) || |         | |      | |   | |      | (__    
| |      |  ___  || |   | ||     __)| |   | |  |  _____)|     __)|  ___  || |         | |      | |   | |      |  __)   
| |      | (   ) || |   | || (\ (   | |   ) |  | (      | (\ (   | (   ) || |         | |      | |   | |      | (      
| (____/\| )   ( || (___) || ) \ \__| (__/  )  | )      | ) \ \__| )   ( || (____/\   | |   ___) (___| (____/\| (____/\
(_______/|/     \|(_______)|/   \__/(______/   |/       |/   \__/|/     \|(_______/   )_(   \_______/(_______/(_______/
                                                                                                                       
"""

print(intro)
print('Would you like to begin practice?')

def startQuestion():
    easymoney = 0
    youfuckingsuck = 0
    keepGoing = True
    MajorMinor = ''
    typeChooser = 0
    while keepGoing == True:
        answer = ''
        typeChooser = random.choice([0,1])
        noteChooser = random.randint(0,11)
        if(typeChooser == 0):
            MajorMinor = 'Major Interval'
            if(noteChooser+4 >= 11):
                answer = notes[((noteChooser+4) %11)-1]
            else:
                answer = notes[(noteChooser+4) %11]
        else:
            MajorMinor = 'Minor Interval'
            if(noteChooser+3 >= 11):
                answer = notes[((noteChooser+3) %11)-1]
            else:
                answer = notes[(noteChooser+3) %11]
        
        line = 'What is a '+ MajorMinor + ' above ' + notes[noteChooser] + '?'
        print(line)
        myAnswer = input().upper()
        if(myAnswer == answer):
            print('nice job')
            easymoney = easymoney +1
        else:
            print('L')
            youfuckingsuck = youfuckingsuck +1
        runitbackturbo = input().lower()
        if(runitbackturbo == 'exit'):
            keepGoing = False
            print('You got '+ str(easymoney) + ' out of ' + str((easymoney + youfuckingsuck)) + ' questions correct.')


startAnswer = input().lower()
if(startAnswer == 'yes'):
    startQuestion()
else:
    exit()



        



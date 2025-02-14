from flask import Flask, render_template, request
import random
import time



charFcts1 = {
    'name':'malachi',
    'gender':'male',
    'hair color':'black hair',
    'height':"5'11",
    'race':'black',
}

charFcts2 = {
    'name':'nate',
    'gender':'male',
    'hair color':'brown hair',
    'height':"5'10",
    'race':'hispanic',
}

charFcts3 = {
    'name':'carlajah',
    'gender':'female',
    'hair color':'black hair',
    'height':"5'6",
    'race':'white',
}

charFcts4 = {
    'name':'micah',
    'gender':'male',
    'hair color':'dark brown hair',
    'height':"6'3",
    'race':'white',
}

charFcts5 = {
    'name':'emily',
    'gender':'female',
    'hair color':'dark brown hair',
    'height':"5'2",
    'race':'hispanic',
}

charFcts5 = {
    'name':'ms alexander',
    'gender':'female',
    'hair color':'brown hair',
    'height':"5'7",
    'race':'white',
}

charFcts6 = {
    'name':'sofija',
    'gender':'female',
    'hair color':'light brown hair',
    'height':"5'7",
    'race':'white',
}

charFcts7 = {
    'name':'josh',
    'gender':'male',
    'hair color':'dirty blonde hair',
    'height':"6'",
    'race':'white',
}

charFcts8 = {
    'name':'jude',
    'gender':'male',
    'hair color':'brown hair',
    'height':"5'9",
    'race':'white',
}

charFcts9 = {
    'name':'rhys',
    'gender':'male',
    'hair color':'brown hair',
    'height':"5'10",
    'race':'white',
}

charFcts10 = {
    'name':'aleksander',
    'gender':'male',
    'hair color':'dirty blonde hair',
    'height':"5'8",
    'race':'white',
}

charFcts11 = {
    'name':'paloma',
    'gender':'female',
    'hair color':'brown hair',
    'height':"5'4",
    'race':'hispanic',
}

charFcts12 = {
    'name':'geselle',
    'gender':'female',
    'hair color':'black hair',
    'height':"5'",
    'race':'hispanic',
}

charFcts13 = {
    'name':'ellery',
    'gender':'female',
    'hair color':'brown hair',
    'height':"5'4",
    'race':'white',
}

charFcts14 = {
    'name':'nicole',
    'gender':'female',
    'hair color':'black hair',
    'height':"4'11",
    'race':'black',
}

charFcts15 = {
    'name':'ryahna',
    'gender':'female',
    'hair color':'black hair',
    'height':"5'1",
    'race':'black',
}

charFcts16 = {
    'name':'bela',
    'gender':'female',
    'hair color':'brown hair',
    'height':"5'4",
    'race':'white',
}

charFcts17 = {
    'name':'avery',
    'gender':'female',
    'hair color':'dirty blonde hair',
    'height':"5'10",
    'race':'white',
}

charList = [charFcts1, charFcts2, charFcts3,charFcts4, charFcts5, charFcts6,charFcts7, charFcts8, charFcts9,charFcts10, charFcts11, charFcts12,charFcts13, charFcts14, charFcts15,charFcts16,charFcts17]
gameChosenChar = charList[random.randint(0,16)]

userCommand = ''
gameStatus = ''
userGuessCount = 0
hintNumb = 4
hint = ''

app = Flask(__name__)






@app.route('/')
def my_form():

    return render_template('pphtml1.html')

@app.route('/new', methods=['POST'])
def my_post():
    global num
    global gameChosenChar
    global gameChosenChar1
    global charList, userCommand, gameStatus, userGuessCount, hintNumb, hint
   
    hintNumb1 = ''
    msg = ''
    hint = ''
   

    if userGuessCount <4:
        
        userCommand = request.form['text1']
        

        if userCommand == gameChosenChar['name']:
            gameChosenChar1 = str(gameChosenChar['name'])
            num = 'Correct, awnser was ' + gameChosenChar1
            gameChosenChar = charList[random.randint(0,16)]
            msg = ''
            hintNumb = 4
            userGuessCount = 0
            print("correct")
            return render_template("pphtml1.html", num=num, msg=msg)
        
        elif userCommand != gameChosenChar['name']:
            userGuessCount +=1
            hintNumb = hintNumb - 1

            if hintNumb == 3:
                hint = ("hint: "+ gameChosenChar['gender'])
            elif hintNumb == 2:
                hint = ("hint: " + gameChosenChar['height'])
            elif hintNumb == 1:
                hint = ("hint: " + gameChosenChar['hair color'])
            elif hintNumb == 0:
                hint = ("hint: " + gameChosenChar['race'])
            
            hintNumb1 = str(hintNumb)
            msg = 'Incorrect. Hints left: ' + hintNumb1
            return render_template("pphtml1.html", msg=msg, hint=hint)
    else:
        
        if userCommand == gameChosenChar['name']:
            gameChosenChar1 = str(gameChosenChar['name'])
            num = 'Correct, Answer was ' + gameChosenChar1
            gameChosenChar = charList[random.randint(0,16)]
            msg = ''
            hintNumb = 4
            hintNumb1 = ''
            userGuessCount = 0
            print("correct")
            return render_template("pphtml1.html", num=num, msg=msg)
        
        else:
            gameChosenChar1 = str(gameChosenChar['name'])
            num = "Incorrect, answer was " + gameChosenChar1
            gameChosenChar = charList[random.randint(0,16)]
            msg = ''
            hintNumb = 4
            hintNumb1 = ''
            userGuessCount = 0
            return render_template("pphtml1.html", num=num, msg=msg)

if __name__== '__main__':
    app.run(debug=True)

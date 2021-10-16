
import random

class Words:
    def __init__(self):
#words list
        self.wordlist = ["bacon", "eternal", "drill", "solar", "house",
"desk", "television", "sidewalk", "branch", "leaf"]
        #total words in the list
        self.wordCount = 10

    #get random a word from word list
    def getRandomWord(self):
        #generate random index 
        i = random.randint(0, self.wordCount - 1)
        #return the word 
        return self.wordlist[i]

#class 2 for jumper 
class Jumper:
    def __init__(self):
        #jumper img 
        self.jumper = [" ___ ",
                      "/___\ ",
                       "\   / ",
                       " \ / ",
                        "  0 ",
                       " /|\ ",
                       " / \ ",
                         "  ",
                      ""]

    def draw(self):
        for line in self.jumper:
            print(line)

    #incorrect guesses
    def reduce(self):
        self.jumper = self.jumper[1:] 
        if len(self.jumper) == 5:
            self.jumper[0] = "  XX ";

#if uses all the guesses
    def finished(self):
        if len(self.jumper) == 5: 
            #game will be over
            return True 
        else: #stll in the game
            return False 

#user inputs
class Console:
    #guesses from user
    def getUserGuess(self):
        letter = input("GUESS A LETTER: ") 
        return letter 

#the game
class Game:
    def __init__(self):
        #create word object
        self.words = Words() 
        #Jumper guy
        self.jumper = Jumper()
        #console object
        self.console = Console() 
        #random word
        self.word = self.words.getRandomWord() 
        self.guess = "" 

        for i in range(len(self.word)):
            self.guess += "-" #filler 
        self.finished = False #game not over

    #user guess
    def play(self):
        #print guessed word
        print("\n" + self.guess) 
        #jumper pic
        self.jumper.draw() 
        #not finished
        if not self.finished: 
            guessLetter = self.console.getUserGuess() 
            changed = self.updateGuess(guessLetter) #correct??
            if not changed: #incorrect guess
                self.jumper.reduce() #update jumper guy

    #are guesses correct
    def updateGuess(self, guessLetter):
        #if wrong guess
        changed = False 
        for i in range(len(self.word)): 
            if self.word[i] == guessLetter and self.guess[i] == "-":
            #is a character match
                self.guess = self.guess[0:i] + guessLetter + self.guess[i + 1:]
                changed = True 
        return changed #return 

    #game over
    def isFinished(self):
        #if the game is over
        self.finished = True 
        #check if all letters guessed
        for i in range(len(self.guess)): 
            #verify one letter not guessed
            if self.guess[i] == '-': 
                self.finished = False 
        if self.finished or self.jumper.finished():
        
            self.finished = True 
            return True 
        else:
            return False 

    #correct word 
    def show(self):
        print("CORRECT WORD IS: " + self.word)
        print()

#game object
game = Game() 

while not game.isFinished(): #loop 
    game.play() 

game.play() 
game.show() 
## This file contents the test for the logic in the script probabilistic dynamic programing
## author: Daniel Fernando Santos Bustos


from __future__ import print_function
from PDP.Game2Player import  Game2Player  
from PDP.GameNPlayers import  GameNPlayers
from PDP.Player import  Player


def testProgram(game, numStages, probabilities ,apuesta):
    
    stages = {} ##This var store the tables in the game 
    ##Here I initialize the stages 
    for x in range (1, numStages+1):
        stages[x] = []

    ##Instantiate the class Game1Player
	game.setStages(stages)
    game.createTables()
    stages = game.getStages()

    ##This is the first decision that the program recomend to take
    ##calEntropy(1) refers to calc the probabiliti to win more money if won in the next stage
    print ("Entropy win next stage"+str(game.calcEntropy(1))+ "\n\nStage#1")
    if apuesta>game.calcEntropy(1):
        print ("We recomend do not play, but if you want to play we suggest that you follow this instructions \n")
    else:
        print ("We recomend that you play, We suggest that you follow this instructions \n")

    ##These are the next stages (2 to num of stages) in the game
    ##Here we show the piece of advices that our game give
    for i in range (2, numStages+1):
        
        print ("Stage #"+str(i)) 
        table= stages[i]
        for row in table:
            print ("If your state is "+ row[0]+ ", We recomend that you "+ row[4] +" the game")



def test1Player():
    numStages = 10 ##This is the number of stages
    probabilities = {} ##This dictionary store the probabilities in the game
    apuesta = 0 ##This is the initial bet of the game

    ##Define  the probabilities of this case
    probabilities["1"] = 0.3
    probabilities["2"] = 0.25
    probabilities["3"] = 0.2
    probabilities["4"] = 0.15
    probabilities["5"] = 0.1
	#			state    probability of this state  	

    states=probabilities.keys()
    game = GameNPlayers(probabilities,states)
    testProgram(game, numStages, probabilities, apuesta)
    


def test2Players():

    numStages = 5 ##This is the number of stages
    probabilities = {} ##This dictionary store the probabilities in the game
    apuesta = 50 ##This is the initial bet of the game
    features = {}
    features1 = {}
    ##Define  the probabilities of this case
	 
    features1 = {
        "speed" : 70.0,
        "strength" : 80.0,
        "intelligent" : 45.0,
        "shield" : 0.0,
        "skill" : 90.0,
        "espirit" : 40.0,
        "confidence" : 45.0,
		"health":78.0
    }
    features = {
        "speed" : 50.0,
        "strength" : 70.0,
        "intelligent" : 80.0,
        "shield" : 90.0,
        "skill" : 80.0,
        "espirit" : 70.0,
        "confidence" : 50.0,
		"health": 70.0
    }

    player1 = Player("Daniel",features)
    player2 = Player("Julian",features1)

    game = Game2Player()
    probabilities = game.calcProbabilities(player1, player2)
    print(probabilities)
    states=probabilities.keys()
    game.setProbabilities(probabilities)
    game.setStates(states)
    testProgram(game, numStages, probabilities, apuesta)
	

    #player1.show()
    #player2.show()
	

	#testProgram(numStages, probabilities, apuesta)

test2Players()

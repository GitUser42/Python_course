import numpy.random as random

class RockPaperScissors:
   
        
    def __init__(self):
        scissors = {"rock" : False, "paper" : True }
        rock = {"scissors" : True, "paper" : False}
        paper = {"rock" : True, "scissors" : False}
        
        self.choices = {"scissors" : scissors, "rock" : rock, "paper" : paper}
        self.answer = "rock"
        self.computer_answer = random.choice(["scissors", "rock", "paper"])
        
    def play(self, answer):
        while self.answer not in self.choices:
            self.answer = input("rock, paper or scissors?")

        
    def outcome(self):     
        if self.answer == self.computer_answer:
            print("Computer has", self.answer, "as well!")
            print("TIED GAME")
        else: 
            if self.choices[self.answer][self.computer_answer]:
                print("Computer has", self.computer_answer)
                print("YOU WON")
            else:
                print("Computer has", self.computer_answer)
                print("YOU LOSE")
                
        new_game = input("Another round? (y/n)")
        if new_game in ["y","Y","yes","Yes"]:
            RockPaperScissors
            
if __name__ == "__main__":
        rock_paper_scissors = RockPaperScissors  # mit () ?
        rock_paper_scissors.play("self", "answer")
        rock_paper_scissors.outcome("self")
    
    
            



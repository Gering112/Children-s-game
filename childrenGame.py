import turtle
import random

def game():
        
    playerx=turtle.Turtle()
    playery=turtle.Turtle()
    playerz=turtle.Turtle()
    ref=turtle.Turtle()

    playerx.shape("square")
    playery.shape("turtle")
    playerz.shape("triangle")
    ref.shape("circle")

    playerx.color("red")
    playery.color("blue")
    playerz.color("green")
    ref.color("black")


    playerx.penup()
    playerx.goto(-250,250)
    playery.penup()
    playery.goto(-250,0)
    playerz.penup()
    playerz.goto(-250,-250)
    ref.penup()
    ref.setposition(300,300)
    ref.pendown()
    ref.goto(300,-300)
    

    firstplayer=random.randint(1,10)
    firstplayer=(firstplayer%3)+1
    if (firstplayer==1):
        player1=("1")
        player2=("2")
        player3=("3")
    if (firstplayer==2):
        player1=("2")
        player2=("3")
        player3=("1")
    if (firstplayer==3):
        player1=("3")
        player2=("1")
        player3=("2")
            
        

    





    print("player's %c turn" %player1)
    q1= userinput=input("What is the world's largest ocean?")
    answer=("pacific")
    if q1== ("pacific ocean"):print(" Correct Answer!!")
    if q1== ("pacific"):playerx.forward(100)
    else:print(" Incorrect!""The right answer is ",answer)
    

    print("player's %c turn"%player2)
    q2=userinput=input("which of the following item is attracted to magnets? A) wood, B)Aluminum, C)Copper, D)iron ")
    answer=("iron")
    if q2==("D") or q2==("d"): print(" Correct Answer!!")
    if q2==("D") or q2==("d"): playery.forward(100)
    else: print("Incorrect!""The right answer is ",answer)

    print("player's %c turn"%player3)
    q3= userinput=input("Which form of electricity is created when your hair stands up after rubbing a balloon on your head?")
    answer=("static")
    if q3==("static"):print("Correct Answer!!")
    if q3==("static"): playerz.forward(100)
    else: print("Incorrect!""The right answer is ",answer)

    print("player's %c turn"%player1)
    q4=userinput=input("Which of the following is true about the sun? A)It is the largest star in the universe, B)It is the brightest star in the universe,C)It is the closest star to Earth, D)It is the closest to to you")
    answer= ("It is the closest star to Earth")
    if q4==("C") or q4==("c"):print("Correct Answer!!")
    if q4==("C") or q4==("c"): playerx.forward(100)
    else:print("Incorrect!""The right answer is ",answer)


    print("player's %c turn"%player2)
    q5= userinput=input(" In what war did the United States fight itself?")
    answer=("Civil War")
    if q5== ("Civil War") or q5==("civil war"):print("Great Job")
    if q5== ("Civil War") or q5==("civil war"): playery.forward(100)
    else:print("Incorrect!""The right answer is ",answer)

    print("player's %c turn"%player3)
    q6= userinput=input("How many terms can a president be selected to?")
    answer=("2 terms")
    if q6==("2")or q6==("two"):print("Correct Answer!!")
    if q6==("2")or q6==("two"): playerz.forward(100)
    else:print("Incorrect!""The right answer is ",answer)

    print("player's %c turn"%player1)
    q7= userinput=input(" Name the thirteen original colonies in order from north to south. Remember to captizal the first letter of the state since its a name")
    answer=("Maine, New Hampshire, Massachusetts, New York, Connecticut, Pennsylvania, New Jersey, Maryland, Delaware, Virginia, North Carolina, South Carolina, Georgia")
    if q7==("Maine, New Hampshire, Massachusetts, New York, Connecticut, Pennsylvania, New Jersey, Maryland, Delaware, Virginia, North Carolina, South Carolina, Georgia"):
        print("Correct Answer!!")
    if q7==("Maine, New Hampshire, Massachusetts, New York, Connecticut, Pennsylvania, New Jersey, Maryland, Delaware, Virginia, North Carolina, South Carolina, Georgia"):
        playerx.forward(20)
    else:print("Incorrect!""The right answer is ",answer)

    print("player's %c turn"%player2)
    q8=userinput=input("True or False. The head of the Department of Homeland Security is a member of the president’s cabinet?")
    answer=("True")
    if q8==("True") or q8==("true"): print("Correct Answer")
    if q8==("True") or q8==("true"):playery.forward(100)
    else:print("Incorrect!""The right answer is ",answer)

    print("player's %c turn"%player3)
    q9=userinput=input("Is the U.S. Census, which counts the population and gathers other information about residents? 1) every 5 yeas, 2) every 10 years, 3) every 15 years ")
    answer=("Every 5 years")
    if q9==("1"):print("Good Job")
    if q9==("1"): playerz.forward(100)
    else:print("Incorrect!""The right answer is ",answer)

    print("player's %c turn"%player1)
    q10=userinput=input(" How many states are in the United States?")
    answer=("50 states")
    if q10==("50"):print("Correct Answer!!")
    if q10==("50"): playerx.forward(100)
    else:print("Incorrect!""The right answer is ",answer)


    print("player's %c turn"%player2)
    q11=userinput=input("There are 123 boxes of sweets in a store. There are 25 sweets in each box. How many sweets are in the store?")
    answer=("3,075")
    if q11==("3,075"):print("Nice job")
    if q11==("3,075"): playery.forward(100)
    else:print("Incorrect!""The right answer is ",answer)

    print("player's %c turn"%player3)
    q12=userinput=input("Tom, Julia, Mike and Fran have 175 cards to use in a certain game. They decided to share them equally. How many cards should each one take and how many cards are left?")
    answer=("1")
    if q12==("1"):print("Correct Answer!!")
    if q12==("1"):playerz.forward(100)
    else:print("Incorrect!""The right answer is ",answer)

    print("player's %c turn"%player1)
    q13=userinput=input("Mr Joshua runs 6 kilometers everyday from Monday to Friday. He also runs 12 kilometers a day on Saturday and Sunday. How many kilometers does Joshua run in a week?")
    answer=("54 Kilometer")
    if q13==("54 kilometer"):print("Correct Answer!!")
    if q13==("54 kilometers"): playerx.forward(100)
    else:print("Incorrect!""The right answer is ",answer)

    print("player's %c turn"%player2)
    q14=userinput=input("Tom and Bob are brothers and they each had the same amount of money which they put together to buy a toy. The cost of the toy was $22. If the cashier gave them a change of 6$, how much money did each have?")
    answer=("$14")
    if q14==("$14") or q14==("14"): print("Correct Answer!!")
    if q14==("$14") or q14==("14"):playery.forward(100)
    else:print("Incorrect!""The right answer is ",answer)

    print("player's %c turn"%player3)        
    q15=userinput=input("There are 365 days in one year, and 100 years in one century. How many days are in one century?")
    answer=("35,600")
    if q15==("35,600 days") or q15==("35,600"):print("Correct Answer!!")
    if q15==("35,600 days") or q15==("35,600"):playerz.forward(100)
    else:print("Incorrect!""The right answer is ",answer)

    print("player's %c turn"%player1)
    q16=userinput=input("what is the earth's most common gas in the atmospere? 1)Oxygen, 2)Nitrogen, 3)Carbon, 4)Hydrogen ")
    answer=("2) Nitrogen")
    if q16==("2"): print("Correct Answer!!")
    if q16==("2"):playerx.forward(100)
    else:print("Incorrect!""The right answer is ",answer)

    print("player's %c turn"%player2)
    q17=userinput=input("Which is smaller Atoms or Electrons?")
    answer=("Eletrons")
    if q17==("Electron") or q17==("electrons"):print("Correct Answer!!")
    if q17==("Electron") or q17==("electrons"):playery.forward(100)
    else:print("Incorrect!""The right answer is ",answer)

    print("player's %c turn"%player3)
    q18=userinput=input("where does sound travel the fastest? 1)water 2)air 3)space")
    answer=("water")
    if q18==("1"):print("Correct Answer!!")
    if q18==("1"):playerz.forward(100)
    else: print("Incorrect!""The right answer is ",answer)

    print("player's %c turn"%player1)
    q19=userinput=input("Approximately how long does it take light from the sun to reach Earth? 1)Eight minutes, 2)Eight seconds, 3)Eight hours, 4)Instantly")
    answer=("Eight minutes")
    if q19==("1"): print("Correct Answer!!")
    if q19==("1"):playerx.forward(100)
    else:print("Incorrect!""The right answer is ",answer)

    print("player's %c turn"%player2)
    q20=userinput=input("What is 9+10")
    answer=("19")
    if q20==("19"): print("Correct Answer!!")
    if q20==("19"):playery.forward(100)
    else:("Incorrect!""The right answer is ",answer)



print(" Are you smarter than a fourth grader game")
Start = input( "would you like to start?")
while (Start=="yes"):

    game()
    again=input("Do you want to play again?")
    if (again=="yes"):
        Start=again

    else:
        Start="no"
        print("Thank you for playing")

    turtle.clearscreen()


print( "guess you're not smarter than a fourth grader, have a nice day")
        
    



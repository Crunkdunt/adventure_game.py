# adventure_game.py
OBJECTIVES
Build a terminal program using Python
Add at least one interactive feature using input()
Use Git version control
Use the command line and file navigation
Write a technical blog post on the project

Make a timeline for yourself and avoid the temptation to build things that aren’t required. Setting firm boundaries and deadlines will keep you on track and prevent scope creep.
    I want to have this game complete by the end of the week latest (Friday 31st March). Ideally, wednesday 29th March. I have been agonising over this damn game for too long and delaying. A git repo has already been set up, but the adventure.py will now me the main script to be version controlled.

    Initially, I want to create the locations and logic for traveling between locations. Once this has been done, the locations can be fleshed out with descriptions and items.
    Once the items have been designed/created the logic will be created to allow for rudimentary interraction between the player, world and items. 

    Initially this will be VERY SIMPLE!

Game Premise:   
    The game will take place in a modern day home. Our hero (the player) must start their day by waking up in the bedroom. From there, they must head to the bathroom to use the toilet, wash their hands, then head to the kitchen,
    make a cup of coffee and some toast. Once made, the player should take their food and drink, head to the lounge, turn on the TV sit down and eat.
    After this is done, they should head to the bathroom, shower, dry off, brush teeth and then head to the bedroom to get dressed and ready for work. 
    Once they are dressed and ready for work, they should head out of the bedroom, down the hall and through the lounge to the exit.

What does your program do?
    This is a very simple beginning of a terminal, text based adventure game written in Python
    The player is provided with choices based upon their location and will be prompted to enter an input dependant on what they want to do

How will it work in a terminal?
    The game will prompt the user for input and provide the user with descriptions showing what is in the immediate area, what exits exist and what items they can interract with

Is it one player or two players?
    It is a single player game

Rooms - There will be 5 rooms, Bedroom, Hall, Bathroom, Kitchen and Lounge. The lounge will lead on to the exit.

From the Bedroom, the player can move EAST to the Hall. 
From the Hall, the player can go NORTH to the Bathroom, EAST to the Lounge, South to the Kitchen or West to the Bedroom.
From the Kitchen, the player can go NORTH to the Hall.
From the Batrhoom the player can go SOUTH to the Hall
From the Lounge the player can go WEST to the Hall or East to the Exit

The Game - 
    Start - Player is dreaming of something wonderful, some sort of high adventure involving dragonslaying. During this part, an input will request the players name. Following this will be a series of print statements leading to a *beep**beep**beep* signifyig the alarm clock.
    The player will wake in the BEDROOM and the ALARM CLOCK will show 07:01 - time to get up. - USE ALARM CLOCK
    The player will see a small room, with a single bed in which they are lying, a bedside table with a TOWEL, mirror and chair with CLOTHING draped over it. At the foot of the bed is a DRESSING GOWN. USE DRESSING GOWN
    The player will be prompted that they need to get ready for work. They feel the urge to go to the TOILET and are currently wearing nothing, so a DRESSING GOWN would be appropriate.
    At this point the player should TAKE TOWEL.
    The player can use the BED but will lose the game. 

    The player should head EAST to the Hall - Once in the Hall, they can see a table with a Telephone, Shoes which the player must use before leaving, a Coat Rack with a Coat and a Key Tray containing door and car keys. From here they can head NORTH to the Bathroom, EAST to the Lounge, SOUTH to the Kitchen or WEST to the Bedroom. They should head NORTH to the bathroom

    The player heads NORTH to the bathroom. They see a room with a medicine cabinet, a SHOWER, TOILET, SINK, TOOTHBRUSH, TOOTHPASTE. A light source could be added and a dark room could be used?
    The player should first USE TOILET. They should then USE SINK to wash their hands. they should then TAKE TOOTHBRUSH, USE TOOTH PASTE on TOOTH BRUSH and finally USE TOOTH BRUSH to brush teeth. 
    Once teeth have been brushed, player should PUT TOOTHBRUSH in SINK because im too lazy to add more logic for now. 
    The player will then USE SHOWER. The player will be prompted that they are wet. If after using the shower the player has TOWEL in inventory, they can USE TOWEL to dry off. Else, the player will be told they need a towel to dry off and a towel can be found somewhere. Logic should be added sometime to allow for wet spot in HALL and slip/fall/game over. for now, player can just head to BEDROOM to get Towel.
    Once showered, the game will prompt that the user needs to get dressed and should head to the BEDROOM to put on some clothes. 

    Regarless (for now) whether player had TOWEL, they will need to head to the BEDROOM via the HALL 
    Once in the Bedroom, the player should USE CLOTHES to get dressed.
    
    Once dressed, the player will be prompted that they could do with some toast and a coffee to start the day. From there they should head to the Kitchen, they should head SOUTH to HALL and SOUTH to KITCHEN

    KITCHEN - The player will see a simple kitchen with counters, SINK, fridge, KETTLE, COFFEE, BREAD, TOASTER. For now, the fridge will not be used, but eventually the FRIDGE will contain MILK and BUTTER, these should be TAKEn to help with the creation of COFFEE and TOAST. 
    The player will be prompted to find a MUG and PLATE for the COFFEE and TOAST. They will recieve a suggestion that they are located in the LOUNGE.
    The player will then head NORTH to the HALL

    Once in the HALL the player should head EAST to the LOUNGE
    The Lounge will be a bright room with a front door(EXIT), window, SOFA, TV, coffee table containing a DIRTY PLATE and a DIRTY MUG
    The player should TAKE DIRTY MUG and TAKE DIRTY PLATE and head WEST back to the HALL

    From the HALL the player should head SOUTH to the KITCHEN once more.
    Once in the Kitchen they should USE DIRTY MUG on SINK and USE DIRTY PLATE on SINK to create MUG and PLATE (clean).
    They should then use BREAD on TOASTER to create Toast, KETTLE on SINK to fill and boil kettle, TOAST on PLATE to plate toast and COFFEE on MUG and KETTLE on MUG to make coffee. 
    The player will be prompted to sit down and catch the news while having their food and drink, so they should TAKE PLATE TOAST and TAKE MUG COFFEE and head back to the LOUNGE via the HALL

    Once in the Lounge, they should USE SOFA, USE TV, USE PLATE TOAST to eat toast and USE MUG COFFEE to drink coffee. Each of these actions will add points. mug will become DIRTY MUG and plate will become DIRTY PLATE
    Once breakfast done the player should USE TV to turn it off then head WEST to the Hall (Player has an option of taking DIRTY MUG/PLATE to Kitchen for extra points )

    Once in the hall the player should TAKE KEYS and TAKE CAR KEYS and USE SHOES and USE COAT then head EAST to LOUNGE and finally EAST to EXIT - Thus ending the game and printing total points x/y 
    The player could then be provided with a breakdown of what they scored for.


I will start by creating this logic

Items - There will be items which can be picked up or manipulated. These items will include:
*These items can either constitute a game loss or a reduction in points/completion. 
Bedroom - 
    An alarm clock - This will be the first thing the player will interract with. When the game starts the player will be featured in a dream sequence which will be interrupted by the alarm. The player will need to turn off the alarm.
    Dressing Gown - The player should wear this before showering and getting dressed
    Clothing - The player will need to put on or use clothes once showered to be able to get dressed - Failure to do this will result in a loss of points and a comedic naked moment if the player leaves without getting dressed*
    Towel - This will need to be picked up to be able to dry off after getting in the shower* If the player fails to pick up the towel before showering, they will end up slipping in the hall and breaking their neck, or something.
    Bed - If the player uses bed, they will go back to sleep, miss work and lose the game.

Hall - 
    A phone - This will be an old school wired phone. This can be used in future updates maybe but is just filler for now
    Key Tray - 
        Door Keys - Extra points for grabbing, allows them to re enter home in the future. Forgetting this will result in some sort of snarky message
        Car Keys - Extra points but not essential - May add logic for car journey?
    Coat/Coat rack - This can be used to pick up or hang up coat which will be needed to exit. Failure to do this will end in some sort of game loss scenario *
    Shoes - This will need to be put on in order to exit the house - Failure to do this could result in some sort of game loss scenario *

Bathroom - 
    Toilet - The player will be prompted upon awakening stating they are busting for their morning business. The player must use the toilet before they leave to improve score and remove the 'soiled' ending
    Sink - This will be interracted with by the player for the purpose of cleanliness after having a shit, also will be required for brushing their teeth.
    Tooth brush - Player must use this to maintain good oral hygeine. Must be used along with toothpaste to improve score.
    Toothpaste - This should be used with tooth brush.
    Shower - the player should use the shower to get clean. Simple in and out.

Kitchen - 
    Fridge - This will contain butter and milk - butter for toast and milk for tea/coffee
    Bread - The player will take bread to put in the toaster for toast
    Toaster - The player should use bread with toaster to make toast.
    Kettle - The player will find an empty kettle which needs to be filled with water at the sink.
    Sink - This will EVENTUALLY be full of dirty dishes as the player is a lazy turd who doesnt clean. The sink is needed to fill the kettle with water. - Also add Dish Soap and ability to wash up for extra points. For now, player can use Plate or Mug with sink to clean to gain bonus points.
    Coffee - This should be used with the mug and kettle in order to make a cup of tea/coffee
    ***Player should clean mug and plate from lounge before use. 
    ***Once the player has made toast, they should take toast and use toast with plate to reduce crumbs. Failure to use plate will reduce points and cause mess.
    ***Once player has taken Mug from lounge, they should use coffee with mug, milk with mug then kettle with mug to make mug of coffee
    ***Once the player have made coffee and toast, they should go to the lounge.

Lounge - 
    TV - can be turned on to watch random shit while eating/drinking. Not turning on does not lose points, however, turning on and then off before leaving will gain bonus points, whereas leaving on will result in point penalty.
    Sofa - Can be used to sit down while eating/drinking/watching TV
    DIRTY Mug - Is dirty, needs to be cleaned before use, not cleaning will result in penalty.
    DIRTY Plate - Is dirty, needs to be cleaned before use, not cleaning will result in penalty.



General requirements for the game:
    I will require the following classes:
    Location class - This will contain logic for
Currently, i have added simple logic and a test class of player which creates a player bio based upon user input. The class representation is a string presenting the user input.

I will add classes for each area that the user enters. An item class will also need to be created, consisting of a name, type(as in sword, candle whatever) weight, damage, defense, any other item elements to be added. Will likely start simple with just attack and defence items along with potions. Should magic items have a magic bool? 

Consumables such as potions, food, drink will be added.
Project Brainstorming
Now that you have an idea, visualize the end result:








The following tasks will help you identify natural breakpoints.

Each location class will require the following: 
A Description - describing the current location, what is within reach and exit points.
Directions - valid areas of exits to continue the adventure
Items - a list of items within the current room which can be added to or removed from.


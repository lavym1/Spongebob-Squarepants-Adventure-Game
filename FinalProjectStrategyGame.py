#Final Project CST-205 Vasile Danciu, Josh Jones, Lavinia Uruc
#Spongebob SquarePants strategy text based game
import time
setMediaPath()

def pyCopy(source, target, targetX, targetY):
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      color = getColor(getPixel(source,x,y))
      setColor(getPixel(target, x + targetX, y + targetY), color)
  return target

#modified pyCopy function that does not copy the green background
def pyCopyNB(source, target, targetX, targetY):
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      color = getColor(getPixel(source,x,y))
      if ( getGreen(getPixel(source,x,y)) <= (getRed(getPixel(source,x,y)) + getBlue(getPixel(source,x,y)) ) ):
        setColor(getPixel(target, x + targetX, y + targetY), color)
  return target

def rotatePic(pic):
  w = getWidth(pic)
  h = getHeight(pic)
  pic_rotated = makeEmptyPicture(h, w)
  rX=0
  for x in range (0, w):
    rY=0
    for y in range (0, h):
      color = getColor(getPixel(pic, x, y))
      setColor(getPixel(pic_rotated, rY, w-rX-1), color)
      rY=rY+1
    rX=rX+1
  return pic_rotated

def shrink(pic):
  w2 = getWidth(pic)/2
  h2 = getHeight(pic)/2
  pic_shrinked = makeEmptyPicture(w2, h2)
  for x in range (0, getWidth(pic)-1, 2):
    for y in range (0, getHeight(pic)-1, 2):
      color = getColor(getPixel(pic, x, y))
      setColor(getPixel(pic_shrinked, x/2, y/2), color)
  return pic_shrinked


def changeVolume(sound, factor):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * factor)
   return(sound)

pic = makePicture("Spongebob_Adventure_Game.jpg")
SpongebobPic = makePicture("Spongebob.png")
spatulaPic = makePicture("spatula.png")
pattyPic = shrink(shrink(makePicture("patty.png")))
formulaPic = shrink(makePicture("formula.png"))
loseGamePic = makePicture("gameOver.jpg")
winGamePic = makePicture("win.png")
exitGamePic = makePicture("exit.jpg")
s = makeStyle(sansSerif, bold, 30)
s2 = makeStyle(sansSerif, bold, 15)

object1picked = false #spatula
object2picked = false #krabby patty
object3picked = false #secret formula
name = requestString("Enter your name:")
bubbles = changeVolume(makeSound("bubbles.wav"),2)
laugh = changeVolume(makeSound("SB_laugh.wav"),2)
evilLaugh = changeVolume(makeSound("plankton_evil_laugh.wav"),2)
patrickLaugh = changeVolume(makeSound("Patricks_laugh.wav"),2)
squidw = changeVolume(makeSound("squidward.wav"),2)
garyMeow = changeVolume(makeSound("gary.wav"),2)

def playGame():
  global pic
  pic = makePicture("Spongebob_Adventure_Game.jpg")
  sound = makeSound("SB_intro.wav")
  play(sound)
  printNow("******* Spongebob Squarepants Adventure Game *******")
  addTextWithStyle(pic, 250, 360, "Are you ready, kids?", s, red)
  repaint(pic)
  time.sleep(2)
  addTextWithStyle(pic, 250, 400, "Aye, aye, captain!", s, red)
  repaint(pic)
  time.sleep(2)
  addTextWithStyle(pic, 250, 440, "I can't hear you!", s, red)
  repaint(pic)
  time.sleep(2)
  addTextWithStyle(pic, 250, 480, "Aye, aye, captain!", s, red)
  repaint(pic)
  time.sleep(2)
  pyCopyNB(SpongebobPic,pic,0,0)
  repaint(pic)
  
  addTextWithStyle(pic, 275, 40, "Hi there, " + name + " !", s, red)
  repaint(pic)
  help()
  pineapple()

# exit function
def exit():
  global name
  global pic
  pic = copyInto(exitGamePic, pic, 0,0)
  repaint(pic)
  addTextWithStyle(pic, 310, 515, "Goodbye " + name + " !", s, red)
  repaint(pic)
  #reset objects on exit
  global object1picked, object2picked, object3picked
  object1picked = false #spatula
  object2picked = false #krabby patty
  object3picked = false #secret formula
  return

# help function
def help():
  global name
  descr = "Hi, " + name + "! "
  descr+= "How to play the game:"
  descr+= "\nYour mission is to pick a Krabby Patty from the Krusty Krab and take it to Patrick's house. "
  descr+="You are going to need a spatula to pick the krabby patty! "
  descr+="To travel from one location to another, "
  descr+="type a word like 'north', 'south', 'west',or 'east' to reach a destination. "
  descr+="You can also pick objects at some locations by typing 'pick object_name'. "
  descr+="Type 'help' at any time to redisplay this introduction. "
  descr+="Type 'exit' to quit the game at any time."
  showInformation(descr)
  
###################################
# location one: The Pineapple house
###################################
def pineapple():
  check = true
  global object1picked
  pineapplePic = makePicture("pineapple_house.jpg")
  global pic
  pic = copyInto(pineapplePic, pic, 0,0) # Jython function just like our pyCopy() but much faster!
  repaint(pic)
  
  # Description
  descr = "This is your home. You live in a pineapple house under the sea, "
  addTextWithStyle(pic, 150, 20, descr, s2, red)
  descr = "with your pet snail Gary. "
  addTextWithStyle(pic, 150, 40, descr, s2, red)
  descr = "There is a not totally obvious SECRET room inside the Pineapple House."
  addTextWithStyle(pic, 150, 60, descr, s2, red)
  descr = "If you type the name of the pet snail you might gain entrance."
  addTextWithStyle(pic, 150, 80, descr, s2, red)
  descr = "If you go to work at Krusty Krab, type 'pick spatula' to take your frying spatula."
  addTextWithStyle(pic, 150, 100, descr, s2, red)
  pyCopyNB(SpongebobPic,pic,100,300)
  tempPic = duplicatePicture(pic)
  if object1picked == false:
    pyCopyNB(rotatePic(spatulaPic),pic,400,400)
  repaint(pic)
  play(bubbles)
  # destination choice loop
  while check == true:
    dirChc = "You are in the PINEAPPLE HOUSE\n"
    dirChc += "Where would you like to go, Spongebob?\n"
    dirChc += "Type 'west' to go to Squidward's house\n"
    dirChc += "Type 'south' to go to Sandy's house\n"
    dirChc += "Type 'east' to go to the Krusty Krab\n"
    dirChc += "Type 'help' for game info.\n"
    dirChc += "or just type 'exit' to quit."
    chc = requestString(dirChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "west": # for Squidward's house
      check = false
      squidward()
    elif choice == "south": # for Sandy's house
      check = false
      sandy()
    elif choice == "east": # for Krusty Krab
      check = false
      krusty()
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "gary": # to the secret room
      check = false
      gary()
    elif (chc == "pick spatula" and object1picked == false): # to pick spatula
      object1picked = true
      addTextWithStyle(tempPic, 330, 500, "You have picked the spatula!", s, red)
      pyCopyNB(spatulaPic,tempPic,253,230)
      copyInto(tempPic, pic, 0,0)
      repaint(pic)
      play(laugh)
    elif (chc == "pick spatula" and object1picked == true): # you already have the spatula
      showInformation("You already have the spatula!")
    elif chc == "north":
      showInformation("You cannot go "+ chc +" from here, try west, east, south, or type EXIT to quit.")
      check = true

#################################
# location two: Squidward's house
#################################
def squidward():
  check = true
  squidHousePic = makePicture("squidHousePic.png")
  global pic
  pic = copyInto(squidHousePic, pic, 0,0)
  repaint(pic)
  
  # Description
  descr = "The Squidward's House is located west of the Pineaple House."
  addTextWithStyle(pic, 150, 20, descr, s2, red)
  descr = "Squidward is a cranky octopus who dislikes neighbors."
  addTextWithStyle(pic, 150, 40, descr, s2, red)
  descr = "Try not to spend to much time here."
  addTextWithStyle(pic, 150, 60, descr, s2, red)
  descr = "Squidward could get angry and you could not finish your mission in time."
  addTextWithStyle(pic, 150, 80, descr, s2, red)
  descr = "Visit other neighbors.\n"
  addTextWithStyle(pic, 150, 100, descr, s2, red)
  repaint(pic)
  pyCopyNB(SpongebobPic,pic,100,300)
  repaint(pic)
  play(bubbles)
  play(squidw)
  
  # destination choice loop
  while check == true:
    dirChc = "You are in SQUIDWARD'S HOUSE\n"
    dirChc += "Where would you like to go, Spongebob?\n"
    dirChc += "Type 'west' to go to Patrick's house\n"
    dirChc += "Type 'east' to go to the Pineapple house\n"
    dirChc += "Type 'help' for game info.\n"
    dirChc += "or just type 'exit' to quit."
    chc = requestString(dirChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "west": # for Patrick's house
      check = false
      patrick()
    elif choice == "east": # for Pineapple house
      check = false
      pineapple()
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "north" or chc == "south":
      showInformation("You cannot go "+ chc +" from here, try west, east, or type EXIT to quit.")
      check = true

#################################
# location three: Patrick's house
#################################
def patrick():
  check = true
  patrickHousePic = makePicture("patrickHousePic.jpg")
  global pic
  pic = copyInto(patrickHousePic, pic, 0,0)
  repaint(pic)
  # Description
  descr = "The house is a large brown rock with a wind vane on top."
  addTextWithStyle(pic, 120, 20, descr, s2, red)
  descr = "Like a door, the rock has hinges to open and close."
  addTextWithStyle(pic, 120, 40, descr, s2, red)
  descr = "The front yard has a long black path connecting the front of the rock and Conch Street."
  addTextWithStyle(pic, 120, 60, descr, s2, red)
  descr = "Your best friend, Patrick Star lives here. He is an unintelligent and overweight pink sea star,"
  addTextWithStyle(pic, 120, 80, descr, s2, red)
  descr = "and he is very hungry for a KRABBY PATTY!"
  addTextWithStyle(pic, 120, 100, descr, s2, red)
  repaint(pic)
  pyCopyNB(SpongebobPic,pic,100,300)
  repaint(pic)
  play(bubbles)
  
  if (object2picked == true):#if player has object2picked (the patty), he wins the game
    global name
    pic = copyInto(winGamePic, pic, 0,0)
    repaint(pic)
    play(patrickLaugh)
    time.sleep(2)
    addTextWithStyle(pic, 300, 260, "YOU WON!", s, red)
    repaint(pic)
    showInformation("Congratulations " + name + ", you won the game! Patrick is eating the delicious krabby patty!")
    check = false
    exit()
  
  # destination choice loop
  while check == true:
    dirChc = "You are in PATRICK'S HOUSE\n"
    dirChc += "Where would you like to go, Spongebob?\n"
    dirChc += "Type 'south' to go to the Jellyfish Fields\n"
    dirChc += "Type 'east' to go to Squidward's house\n"
    dirChc += "Type 'help' for game info.\n"
    dirChc += "or just type 'exit' to quit."
    chc = requestString(dirChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "south": # for Jellyfish Fields
      check = false
      jelly()
    elif choice == "east": # for Squidward's house
      check = false
      squidward()
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "north" or chc == "west":
     showInformation("You cannot go "+ chc +" from here, try south, east, or type EXIT to quit.")
     check = true

#####################################
# location four: the Jellyfish Fields
#####################################
def jelly():
  check = true
  jellyPic = makePicture("jellyfish_fields.jpg")
  global pic
  pic = copyInto(jellyPic, pic, 0,0)
  repaint(pic)
  
  # Description
  descr = "A vast area in which over 4 million jellyfish reside."
  addTextWithStyle(pic, 150, 20, descr, s2, red)
  descr = "Other creatures live here such as clams, leeches, and poisonous sea urchins."
  addTextWithStyle(pic, 150, 40, descr, s2, red)
  descr = "You come here wih Patrick to have fun catching jellyfishes with your nets. "
  addTextWithStyle(pic, 150, 60, descr, s2, red)
  repaint(pic)
  pyCopyNB(SpongebobPic,pic,470,300)
  repaint(pic)
  play(bubbles)
  
  # destination choice loop
  while check == true:
    dirChc = "You are at the JELLYFISH FIELDS\n"
    dirChc += "Where would you like to go, Spongebob?\n"
    dirChc += "Type 'north' to go to Patrick's house\n"
    dirChc += "Type 'east' to go to Sandy's house\n"
    dirChc += "Type 'help' for game info.\n"
    dirChc += "or just type 'exit' to quit."
    chc = requestString(dirChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "north": # for Patrick's house
      check = false
      patrick()
    elif choice == "east": # for Sandy's house
      check = false
      sandy()
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "south" or chc == "west":
      showInformation("You cannot go "+ chc +" from here, try north, east, or type EXIT to quit.")
      check = true

#############################
#location five: Sandy's house
#############################
def sandy():
  check = true
  domePic = makePicture("dome.png")
  global pic
  pic = copyInto(domePic, pic, 0,0)
  repaint(pic)
  # Description
  descr = "You have arrived at your friend Sandy Cheeks glass dome house, the Treedome"
  addTextWithStyle(pic, 10, 20, descr, s2, red)
  descr = "It is air-locked and contains no water, the only place in Bikini Bottom where Sandy can survive without her suit."
  addTextWithStyle(pic, 10, 40, descr, s2, red)
  descr = "Its floor is covered in grass, and features a large tree, which contains Sandy's living quarters."
  addTextWithStyle(pic, 10, 60, descr, s2, red)
  descr = "The Treedome also humorously includes a giant hamster wheel, among other backyardish things."
  addTextWithStyle(pic, 10, 80, descr, s2, red)
  descr = "The dome produces snow during the winter."
  addTextWithStyle(pic, 10, 100, descr, s2, red)
  repaint(pic)
  play(bubbles)
  
  # destination choice loop
  while check == true:
    dirChc = "You are at SANDY'S HOUSE\n"
    dirChc += "Where would you like to go, Spongebob?\n"
    dirChc += "Type 'north' to go to the Pineapple house\n"
    dirChc += "Type 'west' to go to the Jellyfish Fields\n"
    dirChc += "Type 'east' to go to the Chum Bucket\n"
    dirChc += "Type 'help' for game info.\n"
    dirChc += "or just type 'exit' to quit."
    chc = requestString(dirChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "north": # for the Pineapple house
      check = false
      pineapple()
    elif choice == "west": # for the Jellyfish Fields
      check = false
      jelly()
    elif choice == "east": # for the Chum Bucket
      check = false
      chum()
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "south":
     showInformation("You cannot go "+ chc +" from here, try west, east, north, or type EXIT to quit.")
     check = true

###############################
# location six: the Chum Bucket
###############################
def chum():
  check = true
  global object3picked
  chumPic = makePicture("chum.png")
  global pic
  pic = copyInto(chumPic, pic, 0,0)
  repaint(pic)
  # Description
  descr = "Located directly across the street from the Krusty Krab."
  addTextWithStyle(pic, 120, 20, descr, s2, red)
  descr = "Evil Plankton serves awful food here"
  addTextWithStyle(pic, 120, 40, descr, s2, red)
  descr = "He is always trying to steal the Krabby Patty secret Formula."
  addTextWithStyle(pic, 120, 60, descr, s2, red)
  descr = "The restaurant looks like a bucket with a blue hand (could be a glove)."
  addTextWithStyle(pic, 120, 80, descr, s2, red)
  pyCopyNB(SpongebobPic,pic,100,320)
  repaint(pic)
  play(bubbles)
  
  if (object3picked == true):# if player went to Chum Bucket with object3picked (secret formula), he loses the game
    global name
    pic = copyInto(loseGamePic, pic, 0,0)
    repaint(pic)
    play(evilLaugh)
    time.sleep(2)
    addTextWithStyle(pic, 350, 260, "GAME OVER!", s, red)
    repaint(pic)
    showInformation("Plankton stole your Krabby Patty Secret Formula " + name + ", and you lost the game!")
    check = false
    exit()
  
  # destination choice loop
  while check == true:
    dirChc = "You are at the CHUM BUCKET\n"
    dirChc += "Where would you like to go, Spongebob?\n"
    dirChc += "Type 'north' to go to The Krusty Krab\n"
    dirChc += "Type 'west' to go to Sandy's house\n"
    dirChc += "Type 'help' for game info.\n"
    dirChc += "or just type 'exit' to quit."
    chc = requestString(dirChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "north": # for The Krusty Krab
      check = false
      krusty()
    elif choice == "west": # for Sandy's house
      check = false
      sandy()
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "south" or chc == "east":
     showInformation("You cannot go "+ chc +" from here, try north, west, or type EXIT to quit.")
     check = true

################################
# location seven The Krusty Krab
################################
def krusty():
  check = true
  kkPic = makePicture("krusty_krab.jpg")
  global pic
  global object3picked
  pic = copyInto(kkPic, pic, 0,0)
  repaint(pic)
  
  # Description
  descr = "A fast food restaurant located in Bikini Bottom, founded and owned by Eugene H. Krabs."
  addTextWithStyle(pic, 50, 20, descr, s2, red)
  descr = "It is the most popular restaurant in Bikini Bottom. Mr. Krabs loves money!"
  addTextWithStyle(pic, 50, 40, descr, s2, red)
  descr = "This is were you work as a fry cook."
  addTextWithStyle(pic, 50, 60, descr, s2, red)
  descr = "If you have your spatula you can pick a delicious krabby patty!"
  addTextWithStyle(pic, 50, 80, descr, s2, red)
  descr = "To pick a krabby patty type 'pick patty'."
  addTextWithStyle(pic, 50, 100, descr, s2, red)
  descr = "To pick the Krabby Patty Secret Formula type 'pick formula'."
  addTextWithStyle(pic, 50, 120, descr, s2, red)
  repaint(pic)
  pyCopyNB(SpongebobPic,pic,150,350)
  pyCopyNB(pattyPic, pic, 600, 380) # unlimited number of krabby patties available
  tempPic = duplicatePicture(pic)
  if object3picked == false:
    pyCopyNB(formulaPic,pic,500,150)
  repaint(pic)
  play(bubbles)
  
  # destination choice loop
  while check == true:
    dirChc = "You are at THE KRUSTY KRAB\n"
    dirChc += "Where would you like to go, Spongebob?\n"
    dirChc += "Type 'south' to go to the Chum Bucket\n"
    dirChc += "Type 'west' to go to the Pineapple house\n"
    dirChc += "Type 'help' for game info.\n"
    dirChc += "or just type 'exit' to quit."
    chc = requestString(dirChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "south": # for the Chum Bucket
      check = false
      chum()
    elif choice == "west": # for the Pineapple house
      check = false
      pineapple()
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "pick patty":
      if object1picked == true: # player has the spatula required to pick krabby patty
        global object2picked
        object2picked = true
        addTextWithStyle(pic, 70, 570, "You have picked a krabby patty! Take it to Patrick!", s, red)
        pyCopyNB(pattyPic, pic, 115, 365)
        repaint(pic)
        play(laugh)
      else:
        showInformation("You need to pick the spatula from the Pineaple house FIRST! Go back to the Pineapple house, type 'pick spatula', and then come back.")
    elif (chc == "pick formula" and object3picked == false): # to pick the secret formula
      global object3picked
      object3picked = true
      addTextWithStyle(tempPic, 260, 530, "You have picked the Secret Formula!", s, red)
      pyCopyNB(formulaPic,tempPic,350,275)
      copyInto(tempPic, pic, 0,0)
      repaint(pic)
      play(laugh)
      showInformation("You have picked the Krabby Patty Secret Formula! Do not take it to the Chum Bucket!!!!")
    elif (chc == "pick formula" and object3picked == true): #player already has secret formula
      showInformation("You already have the Krabby Patty Secret Formula!")
    elif chc == "north" or chc == "east":
      showInformation("You cannot go "+ chc +" from here, try south, west, or type EXIT to quit.")
      check = true

############
#SECRET ROOM
############
def gary():
  check = true
  secretRoomPic = makePicture("gary.png")
  global pic
  pic = copyInto(secretRoomPic, pic, 0,0)
  repaint(pic)
  play(bubbles)
  
  
  # Description
  descr = "You found the SECRET ROOM where your belowed pet snail hides sometimes"
  addTextWithStyle(pic, 50, 20, descr, s2, red)
  descr = "Gary is a domesticated house pet with similar mannerisms to a cat, but has royal blood,"
  addTextWithStyle(pic, 50, 40, descr, s2, red)
  descr = "Gary has great intelligence (at least for a snail)."
  addTextWithStyle(pic, 50, 60, descr, s2, red)
  descr = "Gary is known for his characteristic 'meow'- in contrast to the barking of the sea worms"
  addTextWithStyle(pic, 50, 80, descr, s2, red)
  repaint(pic)
  play(garyMeow)
  
  # destination choice loop
  while check == true:
    dirChc = "You are in GARY'S SECRET ROOM\n"
    dirChc += "Where would you like to go, Spongebob?\n"
    dirChc += "Type 'pineapple' to exit Garry's SECRET room\n"
    dirChc += "Type 'help' for game info.\n"
    dirChc += "or just type 'exit' to quit."
    chc = requestString(dirChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "pineapple": # for the Pineapple house
      check = false
      pineapple()
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    elif chc == "north" or chc == "east" or chc == "west" or chc == "south":
      showInformation("You cannot go "+ chc +" from here, try 'pineapple' to exit the secret room, or type EXIT to quit.")
      check = true


playGame()
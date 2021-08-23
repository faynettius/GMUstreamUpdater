from tkinter import *

#Changelog
# ver01:
#   added - buttons and +- buttons now update automatically
# ver02:
#   added a tutorial
#   added automatic spaces to the Tournament Name field
#   added specific title to the main window
# ver03:
#   added commentator fields
#   removed the tutorial, nobody used it
# ver04:
#   Fixed the 'Commentator's twitter' throwing exceptions when it was blank
#   Now has a '+space' button that automatically adds spaces to a field

#This function makes the tutorial
def makeTut():
    # This is the start.
    tut.deiconify()
    frameWelcome()
def quit():
    tk.quit()

spacyness = 2
def update():
    fout0 = open("Stream0.txt", "w")
    fout1 = open("Stream1.txt", "w")
    fout2 = open("Stream2.txt", "w")
    fout3 = open("Stream3.txt", "w")
    fout4 = open("Stream4.txt", "w")
    fout5 = open("Stream5.txt", "w")
    ## NEW ONES ##
    fout6 = open("Stream6.txt", "w")
    fout7 = open("Stream7.txt", "w")
    fout8 = open("Stream8.txt", "w")
    fout9 = open("Stream9.txt", "w")
    ## /NEW ONES ##
    outStr = choiceVar1.get() + choiceVar2.get() + choiceVar3.get()
    fout0.write(outStr)
    fout1.write(E1.get())
    fout2.write(E2.get())
    fout3.write(E3.get())
    fout4.write(E4.get())
    ## NEW ONES ##
    fout6.write(E7.get())
    twit1 = E8.get()
    twit1 = fixTwitter(twit1)
    fout7.write(twit1)
    fout8.write(E9.get())
    twit2 = E10.get()
    twit2 = fixTwitter(twit2)
    fout9.write(twit2)
    ## /New Ones##
    # Make a special string for fout5
    wStr = E5.get()
    global spacyness
    spaces = " "*spacyness
    spacyString = spaces.join(wStr)
    fout5.write(spacyString)
    print("hoo-ha")

def addSpace(num):
    global spacyness
    spacyness += num
    if spacyness < 0:
        spacyness = 0

def fixTwitter(twit):
    if twit != "":
        if twit[0] != '@':
            twit = '@' + twit
        return twit
    else:
        return "@NULLFIELD"
def highlightUpdate():
    fout6 = open("Highlights.txt","a")
    # SSF#10 JeBB vs Zephyr Game 1 1st cloud stock
    wStr = E5.get() + " " + E1.get() + " vs " + E3.get() + " " + E6.get() + "\n"
    fout6.write(wStr)

def clearN():
    v1.set('')
    v3.set('')

def clearG():
    v2.set('0')
    v4.set('0')

def clearA():
    v0.set('')
    v1.set('')
    v2.set('')
    v3.set('')
    v4.set('')
    v5.set('')

def plusone(num):
    temp = int(E2.get());
    v2.set(str(temp+num));
    update()

def plustwo(num):
    temp = int(E4.get());
    v4.set(str(temp+num));
    update()

def switch():
    temp1 = E1.get();
    temp2 = E3.get();
    v1.set(temp2);
    v3.set(temp1);
    

tk = Tk()
tk.title("Stream Updater")
##v0 = StringVar()
L0 = Label(tk, text="Bracket Stage").grid(row = 0, column = 1, sticky = 'e')
##E0 = Entry(tk, textvariable = v0)
##E0.grid(row = 0, column = 2, columnspan=4, ipadx = 10)
##v0.set("Winner's Side - Best of 3")

choiceVar1 = StringVar(tk)
choiceVar2 = StringVar(tk)
choiceVar3 = StringVar(tk)
choices1 = {"Winner's ","Loser's ", "Grand ", "Thug ", "Crew Battle", "Iron Man"}
choices2 = {"Side - ", "Top 32 - ", "Pools - ", "Top 8 - ", "Semis - ", "Finals - ", "Quarters - ", "8ths - ", ""}
choices3 = {"Best of 3", "Best of 5",""}
choiceVar1.set("Winner's ")
choiceVar2.set("Side - ")
choiceVar3.set("Best of 3")
dropdown1 = OptionMenu(tk, choiceVar1, *choices1).grid(row = 0, columnspan = 1, column = 2)
dropdown2 = OptionMenu(tk, choiceVar2, *choices2).grid(row = 0, columnspan = 1, column = 3)
dropdown3 = OptionMenu(tk, choiceVar3, *choices3).grid(row = 0, columnspan = 1, column = 4)


v1 = StringVar()
L1 = Label(tk, text="Player 1: ").grid(row = 1, column = 1, sticky = 'e')
E1 = Entry(tk, textvariable = v1)
E1.grid(row = 1, column = 1, columnspan=4, ipadx = 10)
v1.set('Otter is innocent')

v2 = StringVar()
L2 = Label(tk, text="P1 Wins: ").grid(row = 2, column = 1, sticky = 'e')
E2 = Entry(tk, textvariable = v2)
E2.grid(row = 2, column = 1, columnspan=4, ipadx = 10)
v2.set('0')

v3 = StringVar()
L3 = Label(tk, text="Player 2: ").grid(row = 3, column = 1, sticky = 'e')
E3 = Entry(tk, textvariable = v3)
E3.grid(row = 3, column = 1, columnspan=4, ipadx = 10)
v3.set('Ike > Bowser')

v4 = StringVar()
L4 = Label(tk, text="P2 Wins: ").grid(row = 4, column = 1, sticky = 'e')
E4 = Entry(tk, textvariable = v4)
E4.grid(row = 4, column = 1, columnspan=4, ipadx = 10)
v4.set('0')

v5 = StringVar()
L5 = Label(tk, text="SSF# ").grid(row = 5, column = 1, sticky = 'e')
E5 = Entry(tk, textvariable = v5)
E5.grid(row = 5, column = 1, columnspan=4, ipadx = 10)
v5.set('Bring More Setups #56')

plusSpacesB = Button(tk, text = "+Space", command = lambda: addSpace(1)).grid(row = 5, column = 4)
minusSpacesB = Button(tk, text = "-Space", command = lambda: addSpace(-1)).grid(row = 5, column = 5)

L7 = Label(tk, text="Clear:").grid(row = 7, column = 1, sticky = 'e')

L8 = Label(tk, text="REMEMBER TO PRESS RECORD").grid(row = 8, column = 1, columnspan = 6)

# This is for the highlights part
##L9 = Label(tk, text="Highlights").grid(row = 0, column = 20, columnspan = 20)
##v6 = StringVar()
##E6 = Entry(tk, textvariable = v6)
##E6.grid(row = 1, column = 20, columnspan = 20, padx = 10)
##v6.set('Game 2 1st pika stock')

### This runs the tutorial
##runTutorial = Button(tk,text = "TUTORIAL",fg = "darkgreen",command = makeTut)
##runTutorial.grid(row = 3, column = 20, columnspan = 20, padx = 20)

##choiceVar1 = StringVar(tk)
##choiceVar1.set("Winner's ")
##WL = {"Winner's ","Loser's "}
##winnersLosers = OptionMenu(tk, choiceVar1, *WL).grid(row = 8, column = 15)

# MARK = Button(tk, text = "Mark Highlight", fg="green", command = highlightUpdate).grid(row = 2, column = 20, columnspan = 20)


QUIT = Button(tk, text = "QUIT", fg = "red", command = quit).grid(row = 8, column = 1, sticky = 'w')
# Plus Buttons
PLUSONE = Button(tk, text = "+1", fg = "blue", command =lambda: plusone(1)).grid(row = 2, column = 4)
PLUSTWO = Button(tk, text = "+1", fg = "blue", command =lambda: plustwo(1)).grid(row = 4, column = 4)

# Minus Buttons
MinusOne = Button(tk, text = "-1", fg = "blue", command =lambda: plusone(-1)).grid(row = 2, column = 5)
MinusTwo = Button(tk, text = "-1", fg = "blue", command =lambda: plustwo(-1)).grid(row = 4, column = 5)

# Switch Names Button
SWITCH = Button(tk, text = "SWITCH", fg = "blue", command = switch).grid(row = 1, column = 4)

# Updates the current information to the stream overlay
UPDATE = Button(tk, text = "UPDATE", fg = "blue", command = update).grid(row = 6, column = 3)

# Buttons that reset the values of elements to null
CLEARNAMES= Button(tk, text = "Names", fg = "green", command = clearN).grid(row = 7, column = 2)
RESETGAMES= Button(tk, text = "Games", fg = "green", command = clearG).grid(row = 7, column = 3)
CLEARALL= Button(tk, text = "ALL", fg = "green", command = clearA).grid(row = 7, column = 4,  sticky = 'e')

###################### COMMENTATOR FIELDS ######################################################


v7 = StringVar()
L10 = Label(tk, text="Comm 1").grid(row = 1, column = 20, columnspan = 2)
E7 = Entry(tk, textvariable = v7)
E7.grid(row = 1, column = 22, columnspan = 20, padx = 10)
v7.set("Privgu")
       
v8 = StringVar()
L11 = Label(tk, text="1's Twitter").grid(row = 2, column = 20, columnspan = 2)
E8 = Entry(tk, textvariable = v8)
E8.grid(row = 2, column = 22, columnspan = 20, padx = 10)
v8.set("@Privgu")

v9 = StringVar()
L12 = Label(tk, text="Comm 2").grid(row = 3, column = 20, columnspan = 2)
E9 = Entry(tk, textvariable = v9)
E9.grid(row = 3, column = 22, columnspan = 20, padx = 10)
v9.set("Final Smasher")

v10 = StringVar()
L13 = Label(tk, text="2's Twitter").grid(row = 4, column = 20, columnspan = 2)
E10 = Entry(tk, textvariable = v10)
E10.grid(row = 4, column = 22, columnspan = 20, padx = 10)
v10.set('@YiffingEveryDay')



###################### END OF COMMENTATOR FIELDS #################################################

######################## TUTORIAL ZONE ###########################################################
##
##
### This AddTo method allows tracking of each element. ele is a tkinter element
##def addTo(ele):
##    if ele not in widgets:
##        widgets.append(ele)
##    ele.pack()
##
###This clears the screen
##def unpack_all():
##    while len(widgets) != 0:
##        widgets[0].pack_forget()
##        widgets.remove(widgets[0])
##
### The following functions are "frames" of the gui, menus that you can
### switch in between at any time
##def frameWelcome():
##    unpack_all()
##    # The initial frame of the GUI
##    addTo(welcome)
##    addTo(cont)
##    #addTo(debugButton)
##
### This frame does an overview of how to run stream
##def frameOne():
##    unpack_all()
##    addTo(streamSteps)
##    addTo(pressCont)
##    addTo(loadFrame2)
##
### This is the introduction to on-screen info 
##def frameTwo():
##    unpack_all()
##    addTo(SonicImage)
##    addTo(sonicLabel)
##    addTo(pressCont)
##    addTo(loadFrame3)
##
###This frame demonstrates the Bracket Stage intricacies.
##def frameThree():
##    unpack_all()
##    addTo(FileWins)
##    addTo(fileLabel)
##    addTo(pressCont)
##    addTo(loadFrame4)
##
### This frame introduces the Stream Updater program
##def frameFour():
##    unpack_all()
##    addTo(UpdImage)
##    addTo(UpdLabel)
##    addTo(pressCont)
##    addTo(loadFrame5)
##
### This frame shows where the Start Recording button is
##def frameFive():
##    unpack_all()
##    addTo(ObsImage)
##    addTo(ObsLabel)
##    addTo(pressCont)
##    addTo(loadFrame6)
##
##def frameSix():
##    unpack_all()
##    addTo(pressExit)
##    #addTo(exitButton)
##
##    
### This is my debug frame, it is used to test if images work
##def debug():
##    unpack_all()
##    # This is for testing things that i wanna test
##    addTo(SonicImage)
##    # Put the new stuff you want to load here
##    
##def killGUI():
##    tut.quit()
##
##
##
### Make the Tutorial Module
##tut = Toplevel()
##tut.title("GMU Stream Tutorial")
##tut.withdraw()
##widgets = []
### Initialize ALL elements to be used
##
#####################################BUTTONS BUTTONS BUTTONS#######################################################
### Make ALL buttons to be used
##loadWelcome = Button(tut,text = "LWelcome", command = frameWelcome)
##debugButton = Button(tut,text = "DEBUG", command = debug, fg = "red")
##cont = Button(tut,text = "CONTINUE", command =frameOne, fg = "blue")
##loadFrame2 = Button(tut,text = "CONTINUE", command =frameTwo, fg = "blue")
##loadFrame3 = Button(tut,text = "CONTINUE", command =frameThree, fg = "blue")
##loadFrame4 = Button(tut,text = "CONTINUE", command =frameFour, fg = "blue")
##loadFrame5 = Button(tut,text = "CONTINUE", command =frameFive, fg = "blue")
##loadFrame6 = Button(tut,text = "CONTINUE", command =frameSix, fg = "blue")
##exitButton = Button(tut,text = "EXIT", command = killGUI,fg = "red")
##
#####################################MESSAGES MESSAGES MESSAGES####################################################
### Make ALL messages to be used
##streamSteps = Label(tut,text = """Running stream is pretty simple, but if you don't know what you're doing it's not fun to watch OR run.\n
##                    Here are some steps that will guide you through streaming/recording a game:\n
##                    1. Sit down and make sure your mouth is able to touch the foam of the microphone while commentating\n
##                    2. Record information like the bracket stage, players' names. No need to touch the Tournament Name. Player 1 is the leftmost player/team\n
##                    3. After the information is entered, click the 'update' button. If the players start too fast, let them know you need more time\n
##                    4. Go to OBS(the place where you can see the game) and look in the bottom right corner and you'll see a 'Start Recording' button.\n
##                    \tPress it when the players go to the stage select screen, and press it again when both the players have left their chairs
##                    """, justify = LEFT)
##pressCont = Label(tut,text = "Press 'Continue' to move on")
##
##stepTwo = Label(tut,text = "Here is an example of why Player 1 and Player 2 names matter a lot:")
##welcome = Label(tut, text="Welcome to the Tutorial!\nPlease read all text, Snack wrote it for a reason")
##sonicLabel = Label(tut,text = """Here is an example of why Player 1 and Player 2 names matter a lot\n
##                   Player 1 is on the left, so he's the darker sonic. Player 2 is on the right, so he's the lighter sonic""")
##fileLabel = Label(tut,text = """Wow File's doing pretty well vs Zephyr! I wonder where in the bracket they are?\n
##                  Also notice that it says "Winner's Side". Until Quarters for Winner's or 8ths for Loser's there's no need to mark anything but 'Side'""")
##UpdLabel = Label(tut, text = "Here's a look at the updater program. Make sure you hit 'Update', otherwise none of the text will be shown")
##ObsLabel = Label(tut, text = """Here's a quick look at the OBS program. Notice the 'Start Recording' button. it's under the 'Start Streaming' button, don't press that one.\n
##                 Remember to start recording when the players either pick the stage or get to the Stage Select screen. Stop recording when both players have left their chairs.""")
##FinalLabel=Label(tut, text = "Thanks for reading the tutorial! Remember to speak clearly and into the mic.")
##pressExit =Label(tut, text = "Press 'Exit' to end the tutorial")
##
#####################################PICTURES PICTURES PICTURES#####################################################
### Make all PICTURES to be used
##Sphoto = PhotoImage(file="sonicvsonic.gif")
##Sphoto = Sphoto.subsample(2,2)
##SonicImage = Label(tut,image=Sphoto)
##SonicImage.image = Sphoto
##
##FileImage = PhotoImage(file="matchPicture.gif")
##FileImage = FileImage.subsample(3,3)
##FileWins = Label(tut,image=FileImage)
##FileWins.image = FileImage
##
##UpdPhoto = PhotoImage(file="updShot.gif")
##UpdImage = Label(tut,image=UpdPhoto)
##UpdImage.image = UpdPhoto
##
##ObsPhoto = PhotoImage(file="obsScreen.gif")
##ObsPhoto = ObsPhoto.subsample(3,3)
##ObsImage = Label(tut,image=ObsPhoto)
##ObsImage.image = ObsPhoto
##
##
##################################END OF TUTORIAL ZONE ############################

tk.mainloop()
tk.destroy()

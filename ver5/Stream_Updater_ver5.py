from tkinter import *
import os
import socket
import sys

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
# ver05:
#   Now facilitates the input of a port
#   Highlights re-added

myip = socket.gethostbyname(socket.gethostname()) # The local IP for this computer
myPort = sys.argv[1] if len(sys.argv) >1 else "NOPORT"

if "stream_elements" not in os.listdir(os.getcwd()):
    os.mkdir("stream_elements")

def quit():
    tk.quit()

# Sends the output files from this computer to the client computer
def writeIndex(lol, indexName):
    wStr = ""
    for l in lol:
        wStr += f"{l[0]},{l[1]}|"
    with open(indexName,'w') as index:
        index.write(wStr)
    return


spacyness = 2 #The amount of spaces between letter in the tournament title
# Writes the information on the GUI to a file
def update():
    opFolder = "stream_elements" + os.sep
    fout0 = open(opFolder + "bracketStage.txt", "w+")
    fout1 = open(opFolder + "p1Name.txt", "w+")
    fout2 = open(opFolder + "p1Score.txt", "w+")
    fout3 = open(opFolder + "p2Name.txt", "w+")
    fout4 = open(opFolder + "p2Score.txt", "w+")
    fout5 = open(opFolder + "eventName.txt", "w+")
    ## NEW ONES ##
    fout6 = open(opFolder + "twitter1Name.txt", "w+")
    fout7 = open(opFolder + "twitter1AT.txt", "w+")
    fout8 = open(opFolder + "twitter2Name.txt", "w+")
    fout9 = open(opFolder + "twitter2AT.txt", "w+")
    sentFiles = [fout0,
                 fout1,
                 fout2,
                 fout3,
                 fout4,
                 fout5,
                 fout6,
                 fout7,
                 fout8,
                 fout9]
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
    # Make a list of lists of the content inside tyhe files we just wrote
    content = []
    for o in sentFiles:
        pair = []
        o.seek(0)
        pair.append(o.name)
        pair.append(o.read())
        content.append(pair)
    # Close all the files
    for f in sentFiles:
        f.close()
    indexName = 'stream_elements.html'
    writeIndex(content, indexName) # Writes to index.html
    stream_elements = opFolder[:-1]
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

# Appends a highlight mark to a .csv
def highlightUpdate():
    fn = "Highlights.csv"
    # Write a header if the file doesn't exist
    if fn not in os.listdir(os.getcwd()):
        with open(fn,"a") as f:
            header = ["Tournament Name",
                      "p1",
                      "p2",
                      "Bracket Stage",
                      "Game #",
                      "Comment"]
            f.write(",".join(header) + "\n")
    # Write the highlights by reading entry boxes
    bracket_stage = choiceVar1.get() + choiceVar2.get().replace("-","")
    with open(fn,"a") as f:
        # EXAMPLE: BMS#100,JeBB,Zephyr,Grand Finals,Game 1,Comment
        elements = [E5.get(), # Tournament Name
                    E1.get(), # p1 Name
                    E3.get(), # p2 Name
                    bracket_stage, # Bracket Stage
                    "Game " + str(1 + int(E2.get()) + int(E4.get())), # Game Number
                    E6.get()
                    ]
        # wStr = E5.get() + " " + E1.get() + " vs " + E3.get() + " " + E6.get() + "\n"
        wStr = ",".join(elements)
        f.write(wStr + "\n")

# Clears the "Names" field
def clearN():
    v1.set('')
    v3.set('')

# Clears the "Games" field
def clearG():
    v2.set('0')
    v4.set('0')

# Clears all fields
def clearA():
    # v0.set('')
    v1.set('')
    v2.set('')
    v3.set('')
    v4.set('')
    v5.set('')

# Adds +1 to the first player's game score
def plusone(num):
    temp = int(E2.get());
    v2.set(str(temp+num));
    update()

# Adds +1 to the second player's game score
def plustwo(num):
    temp = int(E4.get());
    v4.set(str(temp+num));
    update()

# Swaps the names of player 1 and player 2
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

# Dropdown Setup
choiceVar1 = StringVar(tk)
choiceVar2 = StringVar(tk)
choiceVar3 = StringVar(tk)
bracketSide = {"Winner's ","Loser's ", "Grand ", "Thug ", "Crew Battle", "Iron Man"}
bracketStage = {"Side - ", "Top 32 - ", "Pools - ", "Top 8 - ", "Semis - ", "Finals - ", "Quarters - ", "8ths - ", ""}
bestOf = {"Best of 3", "Best of 5", "Best of 7",""}
choiceVar1.set("Winner's ")
choiceVar2.set("Side - ")
choiceVar3.set("Best of 3")
dropdown1 = OptionMenu(tk, choiceVar1, *bracketSide).grid(row = 0, columnspan = 1, column = 2)
dropdown2 = OptionMenu(tk, choiceVar2, *bracketStage).grid(row = 0, columnspan = 1, column = 3)
dropdown3 = OptionMenu(tk, choiceVar3, *bestOf).grid(row = 0, columnspan = 1, column = 4)

# Player 1 name
v1 = StringVar()
L1 = Label(tk, text="Player 1: ")
L1.grid(row = 1, column = 1, sticky = 'e') # Places the item on the GUI
E1 = Entry(tk, textvariable = v1)
E1.grid(row = 1, column = 1, columnspan=4, ipadx = 10)
v1.set('Alternis')

# Player 1 Score
v2 = StringVar()
L2 = Label(tk, text="P1 Wins: ").grid(row = 2, column = 1, sticky = 'e')
E2 = Entry(tk, textvariable = v2)
E2.grid(row = 2, column = 1, columnspan=4, ipadx = 10)
v2.set('0')

# Plyer 2 Name
v3 = StringVar()
L3 = Label(tk, text="Player 2: ").grid(row = 3, column = 1, sticky = 'e')
E3 = Entry(tk, textvariable = v3)
E3.grid(row = 3, column = 1, columnspan=4, ipadx = 10)
v3.set('Rocketman')

# Player 2 Score
v4 = StringVar()
L4 = Label(tk, text="P2 Wins: ").grid(row = 4, column = 1, sticky = 'e')
E4 = Entry(tk, textvariable = v4)
E4.grid(row = 4, column = 1, columnspan=4, ipadx = 10)
v4.set('0')

#Tournament Name
v5 = StringVar()
L5 = Label(tk, text="Event: ").grid(row = 5, column = 1, sticky = 'e')
E5 = Entry(tk, textvariable = v5)
E5.grid(row = 5, column = 1, columnspan=4, ipadx = 10)
v5.set('Bring More Setups #97')

#Buttons that add spaces in between the letter for the tournament name
plusSpacesB = Button(tk, text = "+Space", command = lambda: addSpace(1)).grid(row = 5, column = 4)
minusSpacesB = Button(tk, text = "-Space", command = lambda: addSpace(-1)).grid(row = 5, column = 5)

# Button that clears the names and games
L7 = Label(tk, text="Clear:").grid(row = 7, column = 1, sticky = 'e')
# Reminder to those
if myPort != "NOPORT":
    L8 = Label(tk, text=f"{myip}:{myPort}", font='Helvetica 10 bold').grid(row = 8, column = 1, columnspan = 6)

# Highlights
v6 = StringVar()
L9 = Label(tk, text="Highlights").grid(row = 5, column = 20, columnspan = 20)
E6 = Entry(tk, textvariable = v6)
L9 = Label(tk, text="Comment")
L9.grid(row = 6, column = 20, columnspan = 2)
E6.grid(row = 6, column = 22, columnspan = 20, padx = 20)
v6.set('Alternis taking first stock')

MARK = Button(tk, text = "Mark Highlight", fg="green", command = highlightUpdate)
MARK.grid(row = 7, column = 20, columnspan = 20)



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

# Commentator 1 Name
v7 = StringVar()
L10 = Label(tk, text="Comm 1").grid(row = 1, column = 20, columnspan = 2)
E7 = Entry(tk, textvariable = v7)
E7.grid(row = 1, column = 22, columnspan = 20, padx = 10)
v7.set("Vichi")

# Commentator 1 Twitter
v8 = StringVar()
L11 = Label(tk, text="1's Twitter").grid(row = 2, column = 20, columnspan = 2)
E8 = Entry(tk, textvariable = v8)
E8.grid(row = 2, column = 22, columnspan = 20, padx = 10)
v8.set("@vvvichi")

# Commentator 2 Name
v9 = StringVar()
L12 = Label(tk, text="Comm 2").grid(row = 3, column = 20, columnspan = 2)
E9 = Entry(tk, textvariable = v9)
E9.grid(row = 3, column = 22, columnspan = 20, padx = 10)
v9.set("File")

# Commentator 2 Twitter
v10 = StringVar()
L13 = Label(tk, text="2's Twitter").grid(row = 4, column = 20, columnspan = 2)
E10 = Entry(tk, textvariable = v10)
E10.grid(row = 4, column = 22, columnspan = 20, padx = 10)
v10.set('@SmashFiles')



###################### END OF COMMENTATOR FIELDS #################################################

tk.mainloop()
tk.destroy()

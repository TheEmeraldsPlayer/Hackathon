import turtle,time
bg = turtle.Screen()
bg.bgcolor("grey")
bg.setup(width = 1280, height = 720)
class turt():
    def addallshapes(direct):
        for x in os.listdir(direct):
            if os.path.isfile(os.path.join(direct,x)):
                bg.addshape(os.path.join(direct,x))
    def newshape(var,shape,default,room):
        if default == True:
            globals()[var].shape(shape)
        else:
            globals()[var].shape(os.path.join(direct,'pictures',room,shape))
    def addturtle(var,pos,size,colour,hide):
        globals()[var] = turtle.Turtle()
        globals()[var].speed(0)
        globals()[var].penup()
        globals()[var].goto(pos)
        if hide == True:
            globals()[var].hideturtle()
        globals()[var].pencolor(colour)
        globals()[var].turtlesize(float(size[0]),float(size[1]),float(size[2]))
def createtextbox():
        turt.addturtle('textbox',(-5,-230),(12,63,1),'white',True)
        turt.newshape('textbox','square',True,None)
        turt.addturtle('textwrite',(-620,-160),(1,1,1),'white',True)
        turt.addturtle('charbox',(-500,-60),(5,10,1),'white',True)
        turt.newshape('charbox','square',True,None)
        turt.addturtle('charname',(-500,-90),(1,1,1),'white',True)
def loadtext(text,name,nar):
    global clicked,writing
    writing = True
    clicked = False
    textbox.showturtle()
    charbox.showturtle()
    if nar == False:
        charbox.hideturtle()
    bg.update()
    bg.tracer(1)
    line=0
    textwrite.goto(-620,-160-50*line)
    if nar == True:
        charname.write(name,False,align='center',font=('Comic Sans MS',24,'normal'))
    for word in text.split(' '):
        if textwrite.xcor() + len(word)*24 > 650:
            line+=1
            textwrite.goto(-620,-160-50*line)
        for letter in word:
            time.sleep(0.05)
            textwrite.write(letter,True,font=('Comic Sans MS',24,'normal'))
        textwrite.write('   ',True)       
    bg.tracer(0)
    turt.addturtle('con',(0,-340),(1,1,1),"white",True)
    bg.onscreenclick(click)
    sizecount = 24
    resize = 0
    change = 1
    while not clicked:
        time.sleep(0.05)
        if abs(resize) == 4:
            change *=-1
        con.write('Click anywhere to continue',False,align='center',font=('Pristina',sizecount+resize,'bold'))
        resize += change
        con.clear()
    textwrite.clear()
    charname.clear()
    textbox.hideturtle()
    charbox.hideturtle()
    writing = False
    bg.update()
def click(x,y):
    global clicked
    clicked = True

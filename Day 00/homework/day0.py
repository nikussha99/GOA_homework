from turtle import*
speed(6)#kedlebi
color("purple")
forward(-300)
right(90)
forward(300)
left(90)
forward(300)
left(90)
forward(300)
left(90)
forward(300)
left(90)
forward(300)




 





#end of the roof


penup()
goto(-130,-50)
pendown()
forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(70)

penup()
goto(-180,-50)
pendown()
forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(70)

#door
penup()
goto(-100,-300)
color("red")
pendown()
begin_fill()

forward(100)
left(90)
forward(100)
left(90)
forward(100)
end_fill()

#roof
penup()
goto(0,0)
color("blue")

pendown()

begin_fill()
left(210)
forward(280)
left(116)
forward(293)
end_fill()






exitonclick()

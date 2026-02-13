from robot import *

bFlag1 = is_free_right() and is_free_down()
bFlag2 = is_free_left() and is_free_down()
bFlag3 = is_free_left() and is_free_up()
bFlag4 = is_free_right() and is_free_up()

while bFlag1:
    if bFlag1:
        move_right()
        move_down()
    bFlag1 = is_free_right() and is_free_down()
        
while bFlag2:
    if bFlag2:
        move_left()
        move_down()
    bFlag2 = is_free_left() and is_free_down()
        
while bFlag3:
    if bFlag3:
        move_left()
        move_up()
    bFlag3 = is_free_left() and is_free_up()
        
while bFlag4:
    if bFlag4:
        move_right()
        move_up()
    bFlag4 = is_free_right() and is_free_up()
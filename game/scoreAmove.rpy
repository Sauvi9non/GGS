init:
    default score = 0
    # $ score += 1
    default Gscore = 0
    # $ Gscore += 1

    $ GS = 10
    $ GGS = 11

transform moveleft:
    linear 0.5 xalign 0.25
transform moveright:
    linear 0.5 xalign 0.75
transform moveM:
    linear 0.5 xalign 0.5
transform movell:
    linear 0.5 xalign 0.0
transform moverr:
    linear 0.5 xalign 1.0

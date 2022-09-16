## endingList 스크린 ##############################################################
## 게임 진행에 따라 해금한 엔딩들을 볼 수 있는 곳

screen endingList():
    tag menu
    add "endingList.png"

    frame:
        #xalign 0.5 yalign 0.5
        fixed:
            imagebutton auto "gui/ed_ch1_%s.png" xpos 570 ypos 45 focus_mask True action ShowMenu("Chap1") hovered
            imagebutton auto "gui/ed_ch2_%s.png" xpos 570 ypos 217 focus_mask True action ShowMenu("Chap2") hovered
            imagebutton auto "gui/ed_ch3_%s.png" xpos 569 ypos 397 focus_mask True action ShowMenu("Chap3") hovered
            imagebutton auto "gui/ed_ch4_%s.png" xpos 570 ypos 569 focus_mask True action ShowMenu("Chap4") hovered
            text '' size 20

            imagebutton auto "gui/undo_%s.png" xpos 1222 ypos 23 focus_mask True action Hide("endingList"), ShowMenu("main_menu") hovered

    frame:
        text "수집한 엔딩" size 32 xpos 50 ypos 300
        $ temp = 0
        for i in range(1, 31):
            if eval('persistent.ec' + str(i)): #여기에 무언가 조건을 더 추가? #persistent.ec+i가 true면
                $temp += 1
                $ce = temp #ce변수에 1추가
        text "[ce] / 30" size 48 xpos 54 ypos 350

screen Chap1():
    add "eachChapEnding.png"
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            for i in range(1, 8):
                if eval('persistent.ending' + str(i)):
                    text eval('persistent.ending' + str(i)) size 40
                else:
                    text '???' size 40 xalign 0.5
            text '' size 20
    fixed:
        imagebutton auto "gui/undo_%s.png" xpos 1220 ypos 25 focus_mask True action Hide("Chap1"), ShowMenu("endingList") hovered

screen Chap2():
    add "eachChapEnding.png"
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            for i in range(8, 15):
                if eval('persistent.ending' + str(i)):
                    text eval('persistent.ending' + str(i)) size 40
                else:
                    text '???' size 40 xalign 0.5
            text '' size 20
    fixed:
        imagebutton auto "gui/undo_%s.png" xpos 1220 ypos 25 focus_mask True action Hide("Chap2"), ShowMenu("endingList") hovered

screen Chap3():
    add "eachChapEnding.png"
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            for i in range(15, 22):
                if eval('persistent.ending' + str(i)):
                    text eval('persistent.ending' + str(i)) size 40
                else:
                    text '???' size 40 xalign 0.5
            text '' size 20
    fixed:
        imagebutton auto "gui/undo_%s.png" xpos 1220 ypos 25 focus_mask True action Hide("Chap3"), ShowMenu("endingList") hovered


screen Chap4():
    add "eachChapEnding.png"
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            for i in range(22, 31):
                if eval('persistent.ending' + str(i)):
                    text eval('persistent.ending' + str(i)) size 40
                else:
                    text '???' size 40 xalign 0.5
            text '' size 20
    fixed:
        imagebutton auto "gui/undo_%s.png" xpos 1220 ypos 25 focus_mask True action Hide("Chap4"), ShowMenu("endingList") hovered

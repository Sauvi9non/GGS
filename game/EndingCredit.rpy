#엔딩 크레딧

label End:

    $ quick_menu = False

    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(1.5, hard=True)
    hide theend
    with dissolve
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    #with Pause(credits_speed, hard=True)
    $ renpy.pause(credits_speed, hard=True)
    show andi:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(1.25, hard=True)
    hide andi
    with dissolve
    show you:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(2, hard=True)
    hide you
    with dissolve
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(2, hard=True)
    #with Pause(2, hard=True)
    hide thanks
    with dissolve
    return

init python:
    credits = ('기획', 'D.i / 왜가리 / 소비뇽'), ('제작', 'D.i / 왜가리 / 소비뇽'), ('시나리오', 'D.i / 왜가리 / 소비뇽'), ('스크립트', 'D.i'), ('프로그래밍', 'D.i / 소비뇽'), ('UI 디자인', 'D.i / 왜가리 / 소비뇽'), ('로고 디자인', '소비뇽'), ('캐릭터 디자인', '왜가리'), ('그림/일러스트', '왜가리')
    credits += ('배경', 'D.i / 왜가리'), ('','')
    credits_s = "{size=80}광공 시뮬레이터\n\n팀 프랑스빙하수\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=40}Ren'py [renpy.version_only]" #Don't forget to set this to your Ren'py version

init:
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The end", text_align=0.5)
    image andi = Text("{size=80}And", text_align=0.5)
    image you = Text("{size=80}YOU", text_align=0.5)
    image thanks = Text("{size=80}플레이 해주셔서 감사합니다!", text_align=0.5)

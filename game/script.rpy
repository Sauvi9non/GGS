# 이 파일에 게임 스크립트를 입력합니다.
init:
    default fault = 0
# 게임에서 사용할 캐릭터를 정의합니다.
define S = Character('서광호', color="#151515")
define L = Character('이연조', color="#00BFFF")
define Nn = Character('내비게이션', color="#585858")
define Sy = Character('비서', color="#585858")
define ea = Character('???', color="#585858")

# 여기에서부터 게임이 시작합니다.
label start:
    $ persistent.endingList_unlocked = True
    play music "/audio/おしゃれなカフェ_일상.mp3" fadeout 1.0
    scene black
    show text '이 게임은 비주얼 노벨 엔진 렌파이로 제작되었습니다.' at truecenter
    pause 1

    jump ch1

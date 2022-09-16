#4챕터 스크립트

label ch4:
    scene bgS OE
    with fade
    show SH Si:
        xalign 0.25
    show IZ Ii2:
        xalign 1.0
        moveright
    play music "audio/おしゃれなカフェ_일상.mp3" fadeout 1.0 fadein 1.0 loop
    "서광호는 업무 관련 자료를 받기 위해 이연조를 불렀다."
    L "서류.. 여기 있습니다."
    "이연조는 힘이 없어 보이는 목소리로 서류를 건넸다."
    "요 며칠간 바쁜 업무가 많았기 때문에 피곤할 만도 했다."
    "오늘따라 이연조가 더 힘들어 보이는 얼굴을 하고 있었기에,"
    "서광호는 이연조의 몸 상태가 좋지 않다는 것을 금방 알아차렸다."

    hide SH Si
    hide IZ Ii2
    menu:
        "야근 시키기":
            show SH Si:
                xalign 0.25
            show IZ Ii2:
                xalign 0.75
            "하지만 서광호는 개의치 않고 추가 근무를 지시했다."
            S "오늘 할 일이 많으니 회사에 남아있도록."
            S "이제 나가봐."
            L "저기.. 사장님.. 사실 오늘 제가 몸이 안 좋아서..."
            S "내가 신경 쓸 일은 아닌 것 같군."
            play music "audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            S "애초에 몸 관리를 못한 본인 탓 아닌가?"
            hide IZ Ii2
            show IZ Ii11:
                xalign 0.75
            "이연조는 얼굴빛이 어두워지더니 옆에 있던 파일철을 집어 들었다."
            "이연조는 아픈 몸 상태로 인해 매우 예민해져 있는 상태였다."
            hide IZ Ii11
            show IZ Ii6:
                xalign 0.75
            "이연조는 파일철을 집어 그대로 서광호의 머리를 내리쳤다."
            "깡!!!"
            "서광호는 갑작스레 머리를 얻어맞고는 그대로 책상 위로 엎어졌다."
            hide IZ Ii6
            show IZ Ii11:
                xalign 0.75
            L "이런 곳에서 더 이상 일 못 하겠습니다."
            hide IZ Ii11
            show IZ Ii11:
                xalign 0.75
                moverr
            pause 0.5
            hide IZ Ii11
            scene black
            with dissolve
            "이연조는 쓰러진 서광호를 뒤로한 채 방을 나가버렸다."
            $persistent.ending22 = '22.우리 회사 블랙 기업이에요?'
            $ persistent.ec22 = True
            show text '{size=25}{color=#FFFFFF}22.우리 회사 블랙 기업이에요?{/color}{/size}' at truecenter
            stop music fadeout 1.0
            with dissolve
            pause 1
            hide text
            with dissolve
            return

        "약 챙겨주기":
            show SH Si:
                xalign 0.25
            show IZ Ii2:
                xalign 0.75
            "이연조를 말없이 보고 있던 서광호는 서랍에서 꺼낸 것을 건넸다."
            S "이거 가져가."
            "이연조는 얼떨결에 받은 것이 회사에서 개발한 약이라는 걸 어렵지 않게 알 수 있었다."
            hide IZ Ii2
            show IZ Ii4:
                xalign 0.75
            L "...! 감사합니다..!"

        "조기 퇴근 시키기":
            $ score += 1
            show SH Si:
                xalign 0.25
            show IZ Ii2:
                xalign 0.75
            S "퇴근해."
            hide IZ Ii2
            show IZ Ii4:
                xalign 0.75
            L "..네?"
            S "조기 퇴근하고, 병원에 가던 집에서 쉬던 해."
            hide IZ Ii4
            show IZ Ii3:
                xalign 0.75
            L "그래도 되나요..?"
            S "쓰러지기라도 하면 곤란하니까."
            L "네 알겠습니다..그럼 돌아가 보겠습니다."

    scene bgS OE
    with fade
    "그 후로 몇 달이 평화롭게 지나갔다."
    show IZ Ii
    "예전보다는 덜하지만, 이연조는 여전히 종종 실수하곤 했다."
    hide IZ Ii
    show SH Si
    "마찬가지로 예전보다는 덜하지만, 서광호는 여전히 이연조에게 차가웠다."
    "남들보다 이연조에게 조금 덜 차가운 이유는 서광호도 알지 못했다."

    scene bgS OE
    with fade
    show SH Si:
        xalign 0.25
    show IZ Ii:
        xalign 0.75
    S "해외 출장은 이 비서가 가지."
    hide IZ Ii
    show IZ Ii4:
        xalign 0.75
    L "네? 제가요?"
    S "회사에 급한 일이 있을 때 이 비서한테 맡기는 것보다는."
    "그렇게 말하는 서광호의 시선은 다른 비서에게 향해있었다."
    hide IZ Ii4
    show IZ Ii:
        xalign 0.75
    "이연조는 알았다는 듯 고개를 끄덕였다."

    scene bgS AE
    with fade
    show SH Si:
        xalign 0.25
    show IZ Ii15:
        xalign 0.75
    "며칠 후, 출장 일이 되었다."
    "이연조는 업무로 나가는 것인데도 왜인지 들떠 보였다."
    scene black
    with fade
    "계약은 순조롭게 진행되었다."
    show SH Si
    "서광호는 비서로 이연조를 데려오길 잘했다고 생각했다."
    hide SH Si
    show IZ Ii
    "이연조에게 대화가 잘 나오는 분위기를 끌어내는 데 탁월한 능력이 있었기 때문이다."
    scene bgS HR
    with fade
    play music "audio/Rainy_Blue_광호 일상.mp3" fadeout 1.0 fadein 1.0 loop
    show SH Si
    "주요한 일정이 끝난 뒤, 서광호는 자신의 방에서 쉬고 있었다."
    "그때 휴대폰이 울렸다."
    "이연조로부터 온 메시지였다."
    L "[[사장님 모처럼 해외까지 왔는데 어디 놀러 가는 거 어떠세요?]"

    hide SH Si
    menu:
        "거절한다":
            show SH Si
            S "[[나는 별로인데, 혼자 다녀와.]"
            "서광호는 문자에 답장한 후, 침대에 가만히 앉아서 정적을 즐겼다."
            "그런데 이연조의 에너지에 너무 익숙해졌던 탓인지 곧 지루함이 몰려오기 시작했다."
            play music "audio/hard rain_선택지 잘못 골랐을 때.mp3 " fadeout 1.0 fadein 1.0 loop
            S "'이런 적은 한 번도 없었는데…'"
            scene black
            with dissolve
            "앞으로의 시간을 대체 어떻게 보내야 할지 서광호는 막막해졌다."
            $persistent.ending23 = '23.이럴 거면 그렇게 하지 말걸 그랬군.'
            $ persistent.ec23 = True
            show text '{size=25}{color=#FFFFFF}23.이럴 거면 그렇게 하지 말걸 그랬군.{/color}{/size}' at truecenter
            stop music fadeout 1.0
            with dissolve
            pause 1
            hide text
            with dissolve
            return

        "수락한다":
            $ score += 1
            show SH Si
            "서광호는 잠시 고민하는 듯싶더니 [[그러지.] 세 글자를 전송했다."
            "메시지를 전송한 지 얼마 되지 않아 노크 소리가 들렸다."
            hide SH Si
            show SH Si:
                xalign 0.5
                moveleft
            show IZ Ii5:
                xalign 1.0
                moveright
            play music "audio/goingOut.mp3" fadeout 1.0 fadein 1.0 loop
            S "...빨리 오는군."
            L "옆방이니까요! 바로 나가도 괜찮으시겠어요?"
            S "..그렇게 해."

    scene bgS MT
    with fade
    show IZ Ii5:
        xalign 1.0
        moveleft
    show SH Si:
        xalign 1.0
        moveright
    "호텔 밖으로 나오자 날씨는 아주 좋았고, 시간은 저녁 시간대를 향해가고 있었다."
    "이연조는 목적지를 정했는지 앞서 나가고 있었고, 서광호는 그 뒤를 따라갔다."
    L "한 번쯤 꼭 가보고 싶었거든요!"
    "두 사람이 향한 곳은 다름 아닌 시장이었다."
    L "사장님 혹시 관심 있는 거 있으세요?"
    S "글쎄."
    L "저기 귀여운 걸 파는 것 같아요!"
    "가까이 다가가자 집안에 장식할 수 있는 아기자기한 소품들을 판매하고 있었다."
    L "이거 저 닮지 않았어요?"
    "서광호는 이연조의 목소리에 고개를 돌렸다."
    "이연조가 손에 든 것은 작은 곰 장식이었다."
    S "그보다는 이쪽이."
    "닮은 것 같은데. 라며 서광호가 가리킨 것은 강아지 장식이었다."
    hide IZ Ii5
    show IZ Ii14:
        xalign 0.25
    "이연조는 서광호의 손끝을 보고는 조금 놀란 듯 보였다."
    hide IZ Ii14
    show IZ Ii5:
        xalign 0.25
    L "닮았나? 제가 이렇게 귀여워요?"
    "손에 들고 있던 것을 제자리에 두고 강아지 장식을 손에 든 이연조가 물었다."
    "서광호는 잠시 고민하다가 고개를 끄덕였다."
    hide IZ Ii5
    show IZ Ii14:
        xalign 0.25
    "이연조가 다시 놀란 표정을 지었지만, 서광호는 그대로 놔두기로 했다."
    hide IZ Ii14
    show IZ Ii5:
        xalign 0.25
    L "그럼 이거 사야겠다. 잠시만 기다려주세요!"
    "이연조는 금방 계산을 마치고 돌아왔다."
    L "출출한데 뭐라도 사 먹을까요?"
    S "흠.."
    "서광호가 별다른 대답을 하지 않자 자기 멋대로 해석한 이연조가 어딘가를 가리켰다."
    L "저쪽에서 음식을 파는 것 같아요!"
    "신나서 말하던 이연조가 서광호의 손을 잡고 끌었다."
    "놀라거나 돌아보지 않은 것으로 보아 아마 이연조도 무의식중에 한 일일 것이다."
    "서광호는 왜인지 오랜만에 닿은 온기가 싫지 않았다."

    scene bgS MT
    with fade
    show IZ Ii5:
        xalign 0.25
    show SH Si:
        xalign 0.75
    "이연조가 고른 음식들이 하나둘 늘어났다."
    "한 명은 당연하고 두 명이 먹기에도 좀 많을 것 같은 양이었다."
    "서광호는 음식을 째려보다시피 보고 있었다."
    "평소의 서광호라면 길거리에서 파는 음식은 먹지 않았을 것이다."
    "하지만 신나하는 이연조를 보고 있으니 적어도 먹는 척은 해줘야겠다고 생각했다."

    hide IZ Ii5
    hide SH Si
    menu:
        "연조가 고른 길거리 음식을 먹어버리기":
            show IZ Ii5:
                xalign 0.25
            show SH Si:
                xalign 0.75
            "이연조가 계산을 마치자 음식들이 건네졌다."
            play music "audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            "서광호는 길거리 음식을 먹어야 한다는 압박감 때문인지 음식을 받자마자 먹기 시작했다."
            hide IZ Ii5
            show IZ Ii4:
                xalign 0.25
            L "사장님?! 드시는 건 상관없는데 여기 말고 테이블에서..!"
            "하지만 서광호에게는 이연조의 목소리가 들리지 않는 것 같았다."
            "특유의 무표정한 얼굴로 빠르지만 깔끔하게 음식들을 먹어 치웠다."
            "모든 음식이 없어지고 나서야 서광호가 멈췄다."
            "음식을 잔뜩 먹은 서광호는 급격히 몰려오는 졸음을 느꼈다."
            scene black
            with dissolve
            "그리고 그대로 꿈나라로 떠났다."
            $persistent.ending24 = '24.사장님? 여기서 주무시면 안 돼요...'
            $ persistent.ec24 = True
            show text '{size=25}{color=#FFFFFF}24.사장님? 여기서 주무시면 안 돼요...{/color}{/size}' at truecenter
            stop music fadeout 1.0
            with dissolve
            pause 1
            hide text
            with dissolve
            return

        "그냥 두기":
            $ Gscore +=1
            show IZ Ii5:
                xalign 0.25
            show SH Si:
                xalign 0.75
            "이연조는 음식을 계산하고 서광호를 돌아봤다."
            L "사장님 따로 드시고 싶은 건 없으세요?"
            S "딱히."
            hide IZ Ii5
            show IZ Ii12:
                xalign 0.25
            L "네..."

        "계산해주기":
            $ score +=1
            show IZ Ii5:
                xalign 0.25
            show SH Si:
                xalign 0.75
            S "{i}이거 계산해주시고, 2개 더 포장해주세요.{/i}"
            hide IZ Ii5
            show IZ Ii4:
                xalign 0.25
            L "????!??! 엇...제가 계산해도 되는데..."
            S "그냥 복지의 일환이라고 생각해. 포장한 건 이 비서가 가져가."

    scene bgS MT
    with fade
    show IZ Ii5:
        xalign 0.25
    show SH Si:
        xalign 0.75
    hide IZ Ii5
    show IZ Ii3:
        xalign 0.25
    L "그런데 사장님은 안 드세요..?"
    S "그런 음식은 취향이 아니라서."
    L "맛있는데... 그래도 한입 드셔보실래요?"
    hide IZ Ii3
    show IZ Ii5:
        xalign 0.25
    L "의외로 맛있을지도 모르잖아요!"
    "이연조는 음식을 살짝 들어 보이며 말했다."
    hide IZ Ii5
    show IZ Ii3:
        xalign 0.25
    "서광호는 이연조가 입 앞으로 가져다준 음식을 살짝 베어 물었다."
    "예상했던 대로 이 음식은 서광호의 입맛에 맞지 않았다."
    "그러나 한껏 긴장한 채 맛이 어떠냐고 물어보는 이연조 앞에서 차마 별로라고 할 수 없었던 서광호는 애써 덤덤한 표정을 지으며 말했다."
    S "나쁘지 않군."
    hide IZ Ii3
    show IZ Ii5:
        xalign 0.25
    L "그쵸?"
    "서광호는 이연조의 뿌듯해하는 모습을 보자 한입 정도 먹어준 보람이 있다고 생각했다."
    "이런 일이 몇 번 반복되자 이연조는"
    L "이렇게 보니까 사장님 아기 새 같으시네요!"
    "라고 말해버렸다."
    hide SH Si
    show SH Si2:
        xalign 0.75
    "그로 인해 서광호의 기분이 조금 나빠졌지만 되돌릴 수는 없었다.."

    scene bgS MT
    with fade
    show IZ Ii12:
        xalign 0.0
        moveright
    show SH Si:
        xalign 0.0
        moveleft
    "식사가 끝나고, 이연조와 서광호는 걸어왔던 길을 따라 시장을 벗어났다."
    "이연조는 조금 아쉬운 표정을 하고 있었다."
    L "일이 좀 더 일찍 끝났으면 좋았을 텐데요.."
    S "..그런가."
    hide IZ Ii12
    show IZ Ii:
        xalign 0.75
    L "아, 아니 그래도 이만큼이나 돌아볼 수 있어서 즐거웠어요!"
    L "앗, 혹시 사장님은 다른 거 하고 싶은 거 없으세요?"

    hide IZ Ii
    hide SH Si
    menu:
        "호텔로 돌아가기":
            $ Gscore += 1
            show IZ Ii:
                xalign 0.75
            show SH Si:
                xalign 0.25
            S "호텔로 돌아가지."
            hide IZ Ii
            show IZ Ii12:
                xalign 0.75
            "이연조가 아쉬워 보이긴 했지만, 밖을 더 돌아다니는 것은 피곤했다."
            L "네, 어차피 늦어서 따로 할 만한 것도 없으니까요.."
            "두 사람은 호텔로 돌아갔다."
            play music "audio/goingOut.mp3" fadeout 1.0

        "야경 보기":
            $ score += 1
            show IZ Ii:
                xalign 0.75
            show SH Si:
                xalign 0.25
            S "전망대라도 갈까."
            hide IZ Ii
            show IZ Ii4:
                xalign 0.75
            L "전망대요?"
            S "싫으면 호텔로 돌아가지."
            hide IZ Ii4
            show IZ Ii7:
                xalign 0.75
                moveM
            L "아뇨! 가고 싶어요! 야경 보고 싶어요!"
            hide SH Si
            play music "audio/Sky_After_Fireworks_전망대.mp3" fadeout 2.0 fadein 1.0
            show SH Si:
                xalign 0.25
                movell
            hide IZ Ii7
            show IZ Ii15:
                xalign 0.5
                moveleft
            scene bgS OY
            with fade
            show IZ Ii5:
                xalign 0.0
                moverr
            show SH Si:
                xalign 0.0
                moveM
            pause 0.5
            hide IZ Ii5
            "전망대의 최상층에 도착하자 이연조는 재빠르게 야경이 잘 보이는 자리로 향했다."
            "늦은 시간임에도 전망대에는 사람이 많았다."
            hide SH Si
            #show IZ Ii8:
            #    xalign 0.75
            #pause 0.25
            #show SH Si:
            #    xalign 0.0
            #    moveleft
            scene black
            with dissolve
            scene nightView
            "서광호가 도착할 때쯤, 이연조는 이미 눈을 빛내고 있었다."
            L "사장님, 저쪽 진짜 예뻐요!"
            "솔직히 서광호는 야경을 즐기는 사람이 아니었다."
            "애초에 자신의 집에서도 밤이면 볼 수 있기도 하고."
            "하지만 그 빛을 보고 즐거워하는 이연조를 보는 것은 새로운 기분이었다."
            "누가 보더라도 반해버릴 정도로 이연조는 빛나고 있었고,\n"
            "서광호도 예외는 아니었다."
    scene black
    with fade

    show SH Si:
        xalign 0.75
        moveleft
    show IZ Ii12:
        xalign 1.0
        moveright
    "호텔에 돌아왔지만 이연조는 여전히 아쉬운 표정이었다."
    "피곤하긴 했지만, 잠깐의 시간을 할애하는 것은 그리 어려운 일이 아니었다."
    play music "audio/Somebody_(Prod._Khaim)_바.mp3" fadeout 1.0 fadein 1.0 loop
    hide IZ Ii12
    show IZ Ii:
        xalign 0.75
    "서광호는 이연조에게 바에 들를지를 물었고, 예상대로 긍정적인 반응이 돌아왔다."
    scene bgS HB
    with fade
    show SH Si:
        xalign 1.0
        moveleft
    show IZ Ii:
        xalign 1.0
        moveright


    "둘은 바에 들어가 자리를 잡았다."
    "그리고 안주를 고르는 일은 이연조에게 맡기고, 서광호는 어떤 걸 주문할지 잠시 고민했다."

    hide SH Si
    hide IZ Ii
    menu:
        "맥주":
            show SH Si:
                xalign 0.25
            show IZ Ii:
                xalign 0.75
            "시원한 맥주였다."
            "하루종일 이연조와 같이 다녀서 맥주가 생각난 서광호였다."
            play music "audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            "서광호에게 제공된 맥주는 거품요정이라도 다녀간 것인지 9:1 비율의 환상적인 거품의 양을 자랑하고 있었다."
            hide SH Si
            show SH Si2:
                xalign 0.25
            "서광호는 거품의 양에 어이가 없었다."
            "심지어 한 모금을 마셔보니 달달한 과일 맥주였다."
            scene black
            with dissolve
            "예상치 못한 단맛에 서광호는 정신을 잃고 쓰러졌다."
            $persistent.ending25 = '25.거품요정 같은 건 없어.'
            $ persistent.ec25 = True
            show text '{size=25}{color=#FFFFFF}25.거품요정 같은 건 없어.{/color}{/size}' at truecenter
            stop music fadeout 1.0
            with dissolve
            pause 1
            hide text
            with dissolve
            return

        "칵테일":
            show SH Si:
                xalign 0.25
            show IZ Ii:
                xalign 0.75
            "딱히 끌리는 게 없었던 서광호는 이연조를 슬쩍 바라봤다."
            L "아 저는 칵테일로 하려고요. 사장님은 정하셨어요?"
            "갑자기 이연조의 입맛이 궁금해진 서광호는 이연조와 같은 메뉴를 시켰다."
            "곧이어 칵테일이 나오고 서광호는 칵테일을 한 모금 마셔봤다."
            "칵테일에서는 달고 신 맛이 났다."
            S "'이비서는 이런걸 좋아하나 보군.'"

        "위스키":
            $ score += 1
            $ Gscore += 1
            show SH Si:
                xalign 0.25
            show IZ Ii:
                xalign 0.75
            "서광호의 주문은 위스키였다."
            hide IZ Ii
            show IZ Ii10:
                xalign 0.75
            "서광호가 기다리는 동안 옆에서 한참 이야기를 하던 이연조는,\n"
            "실제로 보는 것은 처음이라며 위스키를 신기하게 바라봤다."
            "잠시 고민하던 서광호는 같은 메뉴를 하나 더 주문했다."
            "그리고 나온 것은 이연조에게 내밀어졌다."
            hide IZ Ii10
            show IZ Ii4:
                xalign 0.75
            S "본 김에 마셔봐."
            hide IZ Ii4
            show IZ Ii3:
                xalign 0.75
            L "..이거 도수 높은가요?"
            S "...술 못하면 마시지 말고."
            L "그건 아닌데....처음 마셔보는 거라서요."
            S "맛만 보고 별로면 남겨."
            "이연조는 고민하는가 싶더니 곧 잔으로 입을 가져갔다."
            hide IZ Ii3
            show IZ Ii5:
                xalign 0.75
            "그리고 입에 맞았는지 금세 신난 표정이 지어졌다."
            L "이거 맛있네요..!"
            "주변을 의식해서인지 평소보다는 작은 목소리였다."
            S "입에 맞는다면 다행이군."
            hide IZ Ii5
            show IZ Ii:
                xalign 0.75
            L "평소에도 자주 드세요?"
            S "같은 걸 연달아 마시는 취미는 없지만."
            L "다른 건 어떤 거 드시는데요?"
            "그렇게 시작된 이야기는 화제가 바뀌어 가며 이어졌다."
            "다음날에 크게 지장이 가지 않을 정도의 시간까지 길게."
    scene bgS AE
    with fade
    show SH Si:
        xalign 0.25
    show IZ Ii13:
        xalign 0.75
    play music "audio/Rainy_Blue_광호 일상.mp3" fadeout 1.0 fadein 1.0 loop
    "돌아가는 비행기 안."
    "이연조는 피곤했는지 꾸벅꾸벅 졸고 있었다."
    S "'자는 모습이 꽤.. 귀엽군.'"
    S "'내가 왜 이런 생각을...'"
    S "'나도 피곤한가 보군...'"
    "서광호도 눈을 감더니 이내 잠들었다."
    scene bgS OE
    with fade
    show SH Si:
        xalign 0.25
    show IZ Ii:
        xalign 0.75
    play music "audio/おしゃれなカフェ_일상.mp3" fadeout 1.0 fadein 1.0 loop
    "출장에서 돌아온 지 약 한 달 뒤, 드물게 야근을 하던 날이었다."
    "선임 비서는 먼저 퇴근한 상태로 서광호의 집무실에서 이연조가 함께 있는 상태였다."
    hide IZ Ii
    "이연조가 잠시 서류를 인쇄하기 위해 밖으로 나갔다."
    scene black
    pause 0.4
    stop music
    scene bgS OE
    pause 0.4
    scene black
    pause 0.3
    scene bgS OE
    pause 0.3
    scene black
    pause 0.2
    scene bgS OE
    pause 0.2
    scene black
    pause 0.1
    scene bgS OE
    pause 0.1
    scene black
    "그리고 돌아와서 문을 닫은 순간, 갑자기 정전이 일어났다."
    "데이터는 일정 시간마다 저장되기 때문에 큰 문제는 없을 것이다."
    S "'정전인가.'"
    L "우와앗… 무슨 일 난건 아니겠죠…?"
    L "이연조는 무섭다는 듯 몸을 움츠렸다."
    menu:
        "내버려 두기":
            play music "audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            "서광호는 무서워하는 연조를 내버려 두고 심각한 표정을 지었다."
            "서광호는 업무에 관한 일을 생각하느라 심각한 표정을 지은 것이지만 이연조는 정말 회사에 무슨 일이 난 줄 알고 패닉에 빠져버렸다."
            L "저기… 사장님 저희 괜찮은 거 맞죠?? 무슨 일 난 거 아니죠??"
            S "정신 사나우니까 좀 가만히 있어."
            L "사장님… 죄송..합니다…! 전 여기서 빠져나가야겠어요!!"
            "이연조는 사장실을 박차고 도망을 쳐버렸다."
            "당황한 서광호는 이연조를 붙잡으려 급히 일어서다 그만 넘어지고 말았다."
            S "크윽..."
            "서광호의 정신이 점점 희미해져 갔다."
            $persistent.ending26 = '26.위험한 상황에는 빠르고 침착하게 대처해야 해요.'
            $ persistent.ec26 = True
            show text '{size=25}{color=#FFFFFF}26.위험한 상황에는 빠르고 침착하게 대처해야 해요.{/color}{/size}' at truecenter
            stop music fadeout 1.0
            with dissolve
            pause 1
            hide text
            with dissolve
            return

        "괜찮다고 말하기":
            S "별일 아니야 좀 있으면 다시 전기가 들어오겠지."
            L "그..그렇겠죠?"
            "이연조는 애써 침착한 모습을 했다."
            "하지만 서광호의 눈에 이연조는 여전히 불안해 보였다."
            "서광호는 이연조의 어깨를 가볍게 두드리며 불이 켜질 때 까지 괜찮을 거라고 말해주었다."

        "손잡아주기":
            $ score += 1
            "서광호는 안절부절 못해 하는 이연조의 손을 잡아주었다."
            S "좀 진정하는 편이 좋겠군."
            S "...금방 전기가 들어올 거야."
            L "아...감사합니다."
            "이연조는 금방 안정을 찾았다."
            "서광호는 이연조의 차가웠던 손이 점점 따뜻해지는 것을 느꼈다."
            "이연조는 손을 빤히 쳐다봤다."
            L "이제...손 놔주셔도 괜찮아요."
            S "...실례했군."

    scene bgS OE
    with fade
    show SH Si:
        xalign 0.25
    show IZ Ii9:
        xalign 0.75
    play music "audio/おしゃれなカフェ_일상.mp3" fadein 1.0
    "정전이 해결되고 나자 이연조는 조금 부끄러웠는지 빠른 속도로 서광호에게서 멀어졌다."
    L "..감사합니다..."
    "그러면서도 감사의 인사는 빼먹지 않는 것이 이연조다웠다."
    "서광호는 가볍게 고개를 끄덕여 답했다."
    S "그럼 마저 하도록 하지."

    scene bgS OE
    with fade
    show IZ Ii
    "선임 비서가 이연조를 불렀다."
    hide IZ Ii
    show IZ Ii4
    L "파티 참석이요?"
    Sy "평소와 크게 다를 것 없이 사장님 곁에만 붙어있으면 됩니다."
    hide IZ Ii4
    show IZ Ii2
    L "저 근데 입고 갈만한 옷이 없는 것 같은데요.."
    hide IZ Ii2
    show IZ Ii2:
        xalign 0.5
        moveright
    show SH Si:
        xalign 0.0
        moveleft
    S "그럼 새로 사야겠군."
    hide IZ Ii2
    show IZ Ii4:
        xalign 0.75
    L "네, 새로 사...네?"
    S "말이 나온 김에 지금 사러 가지."
    L "지금요?!"
    S "곧 퇴근 시간이고, 알아서 사라고 하기엔."
    "적당한 걸 사 올 수 있을지 잘. 이라고 서광호가 덧붙였다."
    S "아무튼 가지."
    hide SH Si
    show SH Si:
        xalign 0.25
        movell
    "서광호가 먼저 엘리베이터로 향하자 이연조의 선배가 빨리 쫓아가라며 떠밀었다."

    scene bgS DP
    with fade
    "매장에 도착하자 직원이 서광호와 이연조를 반겼다."
    "그리고 곧 이연조의 반강제 패션쇼가 시작되었다..."

    show SH Si:
        xalign 0.25
    ea "이번 건 어떠세요?"
    show IZ In2:
        xalign 1.0
        moveright
    "그렇게 말하는 직원의 옆에는 조금 어색한 자세로 서 있는 이연조가 있었다."
    "이미 꽤 많은 걸 입어본 참이라 적응할 때도 됐는데 여전히 어색해 보였다."
    "이번이 마지막 옷이라 선택지가 별로 없었다."
    "서광호는 이연조를 머리에서 발끝까지 한 번 훑어본 다음 감상을 말했다."

    hide SH Si
    hide IZ In2
    menu:
        "어쩔 수 없다":
            show SH Si:
                xalign 0.25
            show IZ In2:
                xalign 0.75
            S "어쩔 수 없군."
            hide IZ In2
            show IZ In14:
                xalign 0.75
            L "네?"
            S "마지막 옷이고, 지금까지 중에는 제일 나으니."
            hide IZ In14
            show IZ In2:
                xalign 0.75
            L "앗, 네.."
            "둘의 대화를 듣고 있던 직원이 고민하다가 이내 결심한 듯 목소리를 냈다."
            ea "저 혹시.."
            hide IZ In2
            show IZ In14:
                xalign 0.75
            L "네?"
            ea "괜찮으시다면 조금 특이하지만 남은 옷을 가져와 볼까요?"
            "서광호가 고개를 끄덕이자 직원은 바로 사라졌다."
            "이연조는 옷을 더 입어봐야 한다는 사실에 조금 멍해졌다."
            play music "audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            scene bgS DP
            with fade
            show SH Si:
                xalign 0.25
            show IZ In4:
                xalign 0.75
            "직원이 가져온 옷은 매우 휘황찬란하고 빛이 나며 그 어떤 옷보다 화려했다."
            "심지어 이 옷은 날개도 달려있었다."
            L "이.. 이건..."
            ea "후후...알아보시겠나요. 이번 시즌 최고의 작품 ‘날아오르는 새’입니다."
            hide SH Si
            show SH Si2:
                xalign 0.25
            "서광호는 이런 옷을 입은 이연조와 함께 파티에 갈 생각을 하니 정신이 아찔해졌다."
            scene black
            with dissolve
            "정신을 차리고 옷을 똑바로 보려고 했지만, 옷의 엄청난 기운에 눌려 그만 정신을 잃고 말았다."
            $persistent.ending27 = '27.그런 옷을 왜 만드는 거지?'
            $ persistent.ec27 = True
            show text '{size=25}{color=#FFFFFF}27.그런 옷을 왜 만드는 거지?{/color}{/size}' at truecenter
            stop music fadeout 1.0
            with dissolve
            pause 1
            hide text
            with dissolve
            return

        "나쁘지 않다":
            $ Gscore += 1
            show SH Si:
                xalign 0.25
            show IZ In2:
                xalign 0.75
            S "나쁘지 않군."
            hide IZ In2
            show IZ In14:
                xalign 0.75
            L "그런가요?"
            "이연조는 잘 모르겠다는 얼굴로 자신의 몸을 둘러보았다."
            "그러자 직원이 이연조를 거울 앞으로 안내해주었다."
            hide IZ In14

        "어울린다":
            $ score += 1
            show SH Si:
                xalign 0.25
            show IZ In2:
                xalign 0.75
            S "어울리는군."
            hide IZ In2
            show IZ In5:
                xalign 0.75
            L "정말요?"
            "이연조는 기쁜 얼굴을 하고 서광호를 바라봤다."
            S "본인 맘에 드는지도 확인해야지."
            "그렇게 말하며 서광호는 턱짓으로 거울을 가리켰다."
            "이연조는 깨달았다는 듯 거울 앞으로 갔다."
            hide IZ In5

    show IZ In:
        xalign 0.75
        moverr
    pause 0.5
    hide IZ In
    show IZ In12:
        xalign 1.0
    L "..."
    "거울 앞에 선 이연조의 표정이 묘해졌다."
    hide SH Si
    show SH Si:
        xalign 0.25
        moveM
    S "맘에 안 드나?"
    hide IZ In12
    show IZ In14:
        xalign 1.0
    L "네? 아뇨? 그냥 좀.."
    hide IZ In14
    show IZ In12:
        xalign 1.0
    "마음에 들지 않는 것이 아니라면 굳이 더 망설일 필요는 없었다."
    "이미 많은 옷을 입어본 뒤기도 하고."

    scene bgS DP
    with fade
    show SH Si:
        xalign 0.25
    show IZ Ii16:
        xalign 1.0
        moveright
    "계산을 마친 서광호에게 다시 옷을 갈아입고 나오던 이연조가 급하게 다가왔다."
    L "제가 계산해야 하는데..!"
    "그런 이연조를 서광호가 물끄러미 바라봤다."
    S "이 비서 월급으로는 조금 힘들 텐데."
    L "그래도요..!"
    S "업무상 필요한 거니까."
    hide IZ Ii16
    show IZ Ii2:
        xalign 0.75
    hide SH Si
    show SH Si:
        xalign 0.25
        moveM
    "이연조가 곤란한 표정을 짓자 서광호는 이연조의 귀 쪽으로 몸을 숙였다."
    "조금 당황하던 이연조는 서광호의 입에서 정장의 금액이 나오자 침착해졌다."
    S "아직 내고 싶은 마음이 남았나?"
    hide IZ Ii2
    show IZ Ii12:
        xalign 0.75
    L "마음은 있는데...통장이 없네요....."
    hide SH Si
    show SH Si:
        xalign 0.5
        movell
    pause 0.5
    hide SH Si
    "시무룩해진 이연조의 어깨를 두드려 준 서광호가 먼저 밖으로 나섰다."
    hide IZ Ii12
    show IZ Ii:
        xalign 0.75
        movell
    pause 0.5
    hide IZ Ii
    "이연조도 옷을 받아들고 바로 따라나섰다."

    scene bgS OE
    with fade
    show SH Si:
        xalign 0.25
    show IZ In:
        xalign 0.75
    "이연조의 옷을 골라주고 난 며칠 뒤 파티 날이 되었다."
    scene bgS SC
    with fade
    show SH Si:
        xalign 0.25
    show IZ In:
        xalign 0.75
    "서광호와 이연조는 함께 파티가 열리는 호텔로 향했다."
    scene bgS HY2
    with fade
    play music "/audio/Rainy_Blue_광호 일상.mp3" fadeout 1.0 fadein 1.0 loop
    scene bgS HH
    with fade
    show SH Si:
        xalign 0.75
        moveleft
    show IZ In14:
        xalign 1.0
        moveright
    "초대장 확인 과정을 거치고 입장한 파티장은 당연하게도 화려했다."
    hide IZ In14
    show IZ In:
        xalign 0.75
    "파티에 도착한 서광호와 이연조는 파티의 주요 관계자들과 인사를 나눴다."
    hide IZ In
    show IZ In3:
        xalign 0.75
    L "저 이런 데 처음 와봐요.."
    S "일하다 보면 익숙해지겠지."
    hide IZ In3
    show IZ In2:
        xalign 0.75
    L "그건 그렇지만..일단 지금은 좀 울렁거리는 것 같아요..."
    S "괜찮아질 때까지 벽에 기대있던가 해. 심하면 와서 말하고."
    hide IZ In2
    show IZ In14:
        xalign 0.75
    L "그 정도는 아닌데요! 사장님 곁에 붙어있는 게 제 역할인걸요!"
    S "..맘대로 해."
    "파티는 어느 정도 마무리되었고, 이연조가 우려했던 일은 일어나지 않았다."
    scene bgS HY2
    with fade
    show SH Si:
        xalign 0.75
        moveleft
    show IZ In:
        xalign 1.0
        moveright
    "파티장을 벗어나는 이연조의 얼굴은 입장할 때보다 훨씬 편해져 있었다."
    "서광호는 잠시 호텔 옥상에 있는 정원에 들렀다 가도 되냐는 이연조의 제안을 받아들였다."
    scene bgS HP
    with fade
    show SH Si:
        xalign 0.75
        moveleft
    show IZ In:
        xalign 1.0
        moveright
    play music "audio/Spring of Life Short.ver_고백.mp3" fadeout 1.0 fadein 1.0 loop
    "벤치에 앉아 야경을 구경하던 이연조가 서광호 쪽으로 고개를 돌렸다."
    L "저 오늘 괜찮았나요?"
    "서광호가 이연조를 바라보고 있었기 때문에 두 사람의 시선이 바로 마주쳤다."
    S "...나쁘진 않았지."
    L "다행이다..저도 이제 좀 비서 같아졌나 봐요."
    hide IZ In
    show IZ In15:
        xalign 0.75
    L "사장님에게 잘 어울리는 비서가 되고 싶어요!"
    hide IZ In15
    show IZ In5:
        xalign 0.75
    L "그러니까 앞으로도 잘 부탁드릴게요."
    "그렇게 말하며 환하게 웃는 이연조의 모습에 서광호는 무언가를 깨달았다."
    S "다른 걸 해볼 생각은?"
    hide IZ In5
    show IZ In4:
        xalign 0.75
    L "네? 저 지금 일에 만족하는데요..저 잘리나요?!"
    S "그건 아니고."
    hide IZ In4
    show IZ In14:
        xalign 0.75
    L "그럼 갑자기 왜 그런 걸 물어보세요?"
    S "내가 이 비서를 좋아하는 것 같아서."
    hide IZ In14
    show IZ In4:
        xalign 0.75
    L "네...네?"
    S "이제 내려갈까."
    "집까지 태워주겠다고 말하는 서광호의 목덜미가 조금 붉게 변해있었다."
    scene black
    with dissolve
    show text '챕터 4 End' at truecenter
    stop music fadeout 5.0
    pause 3

show text '세이브를 생활화합시다' at truecenter
pause 3
jump chE

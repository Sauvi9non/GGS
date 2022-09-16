#엔딩 스크립트

label chE:

    if (score < GS) and (Gscore != GGS): #배드
        play music "/audio/Rainy_Blue_광호 일상.mp3" fadeout 1.0 fadein 1.0 loop
        scene bgS OE
        with fade
        show SH Si
        "주말이 지나고, 서광호와 이연조는 평소와 다름없이 출근했다."
        "서광호는 늘 그렇듯 사장실에 앉아 업무를 보고 있었다."
        "그때 누군가의 노크 소리가 들려왔다."
        S "들어와."
        hide SH Si
        show SH Si:
            xalign 0.5
            moveleft
        show IZ Ii2:
            xalign 1.0
            moveright
        "사장실 문을 연 사람은 다름 아닌 이연조였다."
        L "저..사장님 다름이 아니라..."
        L "업무 외 이야기로 전해드릴 말이 있어서..."
        S "말해봐."
        L "그때 하신 말씀 생각해 봤는데요..."
        L "역시 사장님 마음은 못 받을 것 같습니다. 죄송합니다..."
        S "...알겠으니 나가서 일 봐."
        L "..네."
        #play music "/audio/涙雨_배드엔딩.mp3" fadeout 1.0 fadein 1.0 loop
        play music "/audio/badEnding.mp3" fadeout 1.0 fadein 1.0 loop
        hide IZ Ii2
        show IZ Ii2:
            xalign 0.75
            moverr
        pause 0.5
        hide SH Si
        show SH Si:
            xalign 0.25
            moveM
        "서광호는 이연조가 나가고 나서 허망하게 천장을 바라봤다."
        "그리고는 반쯤 정신이 나간 채로 보던 업무를 봤다."
        "그러다 보니 평소의 서광호라면 하지 않았을 실수를 하고 말았다."
        Sy "...별일이네요. 사장님이 실수를 다 하시고."
        S "..."
        hide SH Si
        show SH Si3
        S "'말도 안 돼...내가 실수를 하다니..."

        scene bgS SKL
        with fade
        show SH Si
        "그렇게 정신없이 하루가 지나갔고 서광호는 자신의 집에 도착했다."
        "최근 이연조와 보낸 시간이 많아서일까."
        "서광호는 자신이 생각하는 것보다 이연조의 밝은 분위기에 익숙해져 있었다."
        "집에 도착하니 검은색의 인테리어가 서광호를 반겼고,\n"
        "그건 서광호에게 자신의 집이 삭막하다는 생각이 들게 했다."
        "그것뿐만이 아니었다."
        "집은 전체적으로 아무것도 없었고, 심지어 냉장고에는 물밖에 없다는 것을 깨달았다."
        "평소엔 신경 쓰지 않았던 것들이 하나하나 다 신경 쓰이기 시작했다."
        hide SH Si
        show SH Si6
        S "'벽지와 바닥은 왜 죄다 까만색인 거지...?'"
        S "'대체 왜 티비에선 예능이 나오지 않는 거야.'"
        S "'집안에 음식이 하나도 없다니...난...도대체...'"
        "서광호는 낙담한 채 털썩 주저앉아 바닥을 내려쳤다."
        "바닥을 내려쳐봤자 바뀌는 것은 없다."
        "사실 바뀌고 싶었지만 바뀌면 안 될 것만 같았다."
        "이제 와서 생활패턴을 바꾸기엔 너무 오랜 기간을 이렇게 살아왔다."
        "서광호는 사람이 갑자기 바뀌면 죽는다는 말이 왜인지 진짜일 것 같다는 기분이 들었다."

        #(뭐랄까 한번 경험해봤던 것처럼…) #엔딩 있을 때만
        if persistent.fe1 or persistent.fe2 or persistent.fe3:
            "뭐랄까 한번 경험해봤던 것처럼…"

        scene bgS SB1
        show SH Si6
        "서광호는 지금까지의 자신의 삶을 후회하며 앞으로도 이렇게 살아야 한다는 것을 받아들이지 못한 채 침대로 가서 엉엉 울었다..."
        scene black
        with dissolve
        "그렇게 서광호는..."
        $persistent.ending28 = 'End 01.이연조가 없는 삶으로 돌아갈 수 없어..'
        $ persistent.ec28 = True
        $ persistent.fe1 = True
        show text '{size=25}{color=#FFFFFF}End 01.이연조가 없는 삶으로 돌아갈 수 없어..{/color}{/size}' at truecenter
        with dissolve
        pause 1
        hide text
        with dissolve

    if (score >= GS) and (Gscore != GGS): #연애
        play music "/audio/Spring of Life Short.ver_고백.mp3" fadeout 1.0 fadein 1.0 loop
        #play music "/audio/askingOut.mp3" fadeout 1.0 fadein 1.0 loop
        scene bgS OE
        with fade
        show SH Si:
            xalign 0.25
        show IZ Ii2:
            xalign 0.75
        L "저..조금 시간이 필요할 것 같아요."
        "서광호가 자신의 마음을 전한 날이었다."
        "한참 머뭇거리던 이연조가 겨우 입을 열었다."
        "전 같으면 맘에 차지 않았을 말이 기꺼웠다."
        hide SH Si
        show SH Si7:
            xalign 0.25
        S "알겠습니다."
        "기다리는 일 정도는 크게 어렵지 않다."
        play music "/audio/Rainy_Blue_광호 일상.mp3" fadeout 1.0 fadein 1.0 loop
        #play music "/audio/SHDaily.mp3" fadeout 1.0 fadein 1.0 loop
        scene bgS OE
        with fade
        show SH Si
        "주말이 지나고, 서광호와 이연조는 평소와 다름없이 출근했다."
        "서광호는 늘 그렇듯 사장실에 앉아 업무를 보고 있었다."
        "그때 누군가의 노크 소리가 들려왔다."
        S "들어와."
        hide SH Si
        show SH Si:
            xalign 0.5
            moveleft
        show IZ Ii9:
            xalign 1.0
            moveright
        "사장실 문을 연 사람은 다름 아닌 이연조였다."
        L "저..사장님 다름이 아니라..."
        L "업무 외 이야기로 전해드릴 말이 있어서..."
        S "말해봐."
        L "그때 하신 말씀 생각해 봤는데요..."
        L "음..그러니까....."
        L "사장님은 참 좋은 분이라고 생각해요."
        L "겉으로는 차가워도 친절하게 대해주시기도 하고.."
        L "의외로 잘 챙겨주시기도 하고.."
        stop music fadeout 1.5
        "이연조는 한참이나 이런저런 말을 늘어놓더니 갑자기 조용해졌다."
        S "..그래서?"
        play music "/audio/Feel_of_Spring_연애엔딩.mp3" fadein 1.0 loop
        #play music "/audio/loveEnding.mp3" fadein 1.0 loop
        L "그...저도 사장님을 좋아하고 있었어요."
        S "그럼..."
        hide IZ Ii9
        show IZ Ii5:
            xalign 0.75
        L "저랑 만나보실래요?"
        "이연조는 해맑게 웃으며 말했다."
        "서광호는 애써 침착한 척 고개를 끄덕였지만, 심장은 좀처럼 진정되지 않았다."

        scene bgS OE
        with fade
        show SH Si:
            xalign 0.25
        show IZ Ii:
            xalign 0.75
        S "오늘 퇴근하고 영화 보러 가지."
        hide IZ Ii
        show IZ Ii4:
            xalign 0.75
        L "네?"
        S "영화 보러."
        hide IZ Ii4
        show IZ Ii12:
            xalign 0.75
        L "..통보식으로 말씀하시면 안 되죠."
        S "아."
        hide SH Si
        show SH Si7:
            xalign 0.25
        S "오늘 퇴근하고 영화 보러 가시겠습니까?"
        L "흠..."
        "서광호는 서툴렀지만 노력하고 있었고."
        L "좋아요."
        "이연조도 그 사실을 알고 있다."
        "또한, 자신이 바뀌는 것을 이연조가 마냥 기다려줄 수 없다는 사실을 서광호도 알고 있다."
        scene bgS OE
        with fade
        "그래서 서광호는 이연조가 너무 오래 기다리지 않도록 최선을 다해야 했다."
        scene black
        with fade
        "끝이 어찌 될지는 알 수 없지만."
        scene bgS SC
        with fade
        show SH Si:
            xalign 0.25
        show IZ Ii:
            xalign 1.0
            moveright
        pause 0.5
        hide IZ Ii
        show IZ Ii14:
            xalign 0.75
        L "이게 뭐예요?"
        hide SH Si
        show SH Si8:
            xalign 0.25
        S "..선물입니다."
        hide IZ Ii14
        show IZ Ii10:
            xalign 0.75
        L "이렇게 큰 꽃다발을 그냥요? 고백하러 가는 줄 알았겠는데요?"
        hide SH Si8
        show SH Si7:
            xalign 0.25
        S "그럼 그런 걸로 하죠."
        hide IZ Ii10
        show IZ Ii15:
            xalign 0.75
        L "어어- 누구한테 하게요?"
        S "당연히 이연조씨한테."
        L "저는 이미 받았는데요?"
        S "할 때마다 받아주면 좋을 것 같아서요."
        scene loveEnding
        pause 1
        L "..이번 건 좀 멋있었다."
        S "합격인가요?"
        L "....네."
        S "그럼 다행입니다."
        "두 사람의 시작은 서로에게 만족스러워 보였다."
        scene black
        with dissolve
        $persistent.ending29 = 'End 02.시작하는 두 사람'
        $ persistent.ec29 = True
        $ persistent.fe2 = True
        show text '{size=25}{color=#FFFFFF}End 02.시작하는 두 사람{/color}{/size}' at truecenter
        with dissolve
        pause 1
        hide text
        with dissolve

    if Gscore == GGS: #광공
        play music "/audio/Rainy_Blue_광호 일상.mp3" fadeout 1.0 fadein 1.0 loop
        #play music "/audio/SHDaily.mp3" fadeout 1.0 fadein 1.0 loop
        scene bgS OE
        with fade
        show SH Si
        "주말이 지나고, 서광호와 이연조는 평소와 다름없이 출근했다."
        "서광호는 늘 그렇듯 사장실에 앉아 업무를 보고 있었다."
        "그때 누군가의 노크 소리가 들려왔다."
        S "들어와."
        hide SH Si
        show SH Si:
            xalign 0.5
            moveleft
        show IZ Ii2:
            xalign 1.0
            moveright
        "사장실 문을 연 사람은 다름 아닌 이연조였다."
        L "저..사장님 다름이 아니라..."
        L "업무 외 이야기로 전해드릴 말이 있어서..."
        S "말해봐."
        L "그때 하신 말씀 생각해 봤는데요..."
        L "역시 사장님 마음은 못 받을 것 같습니다. 죄송합니다..."
        S "...알겠으니 나가서 일 봐."
        L "..네."
        hide IZ Ii2
        show IZ Ii2:
            xalign 0.75
            moverr
        pause 0.5
        hide IZ Ii2
        hide SH Si
        show SH Si:
            xalign 0.25
            moveM
        "서광호는 그렇게 고백을 거절당했지만, 생각보다 아무 느낌이 없었다."
        play music "/audio/Lights - Patrick Patrikios_광공엔딩.mp3" fadeout 1.0 fadein 1.0 loop
        #play music "/audio/GGEnding.mp3" fadeout 1.0 fadein 1.0 loop
        "이연조에게 미련이 남지도 않았고, 슬프지도 않았다."
        "오히려 신경 쓰고 있던 일이 해결되어 후련한 기분이었다."
        "서광호는 다시 본연의 모습으로 돌아갈 것이다."
        "이제 서광호는 연애 같은 일에 신경 쓰지 않고 일에만 집중할 수 있었다."
        "서광호는 평소보다 더 좋은 컨디션으로 업무를 끝냈다."
        scene bgS OE
        with fade
        show SH Si:
            xalign 0.0
            moveleft
        show IZ Ii:
            xalign 0.75
        S "일 끝났으면 가지."
        hide SH Si
        show SH Si:
            xalign 0.25
            moverr
        pause 0.5
        hide SH Si
        "서광호는 차가운 표정으로 퇴근했다."
        scene black
        with fade
        "이연조에게 어떤 감정이 있어서 그랬다기보단, 그저 평소의 모습으로 돌아온 것이다."
        scene bgS SKL
        with fade
        show SH Si
        pause 0.25
        scene bgS SB2
        with fade
        show SH Gn
        pause 0.25
        scene bgS SKL
        with fade
        show SH Gn
        pause 0.25
        scene bgS SB1
        with fade
        show SH Pa
        pause 0.25
        scene black
        with dissolve
        "서광호는 집에 도착하고 나서 프랑스빙하수를 마시고 가볍게 샤워를 한 후 잠에 들었다."
        "오늘도 평소와 다를 바 없는 하루가 끝났다."
        scene GGEnding
        "아마도 서광호의 일과는 그다음 날도 똑같이 반복될 것이다."
        "그다음 날도."
        "그다음 날도.."
        "그다음 날도..."
        "영원히…"
        with dissolve
        scene black
        $persistent.ending30 = 'End 03.서광호'
        $ persistent.ec30 = True
        $ persistent.fe3 = True
        show text '{size=25}{color=#FFFFFF}End 03.서광호{/color}{/size}' at truecenter
        with dissolve
        pause 1
        hide text
        with dissolve

jump End

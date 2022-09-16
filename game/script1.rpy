#1챕터 스크립트

label ch1:
    stop music
    scene bgS SB1
    with fade
    play music "/audio/Rainy_Blue_광호 일상.mp3" fadeout 1.0 fadein 1.0 loop
    show SH Pa
    "이 남자는 서광호. 33세 남성이자 광공이다."
    "서광호는 매사에 철저하고 시간 낭비를 싫어하는 남자다.
    \n그에게는 하루가 매일매일 똑같이 반복된다."
    scene bgS SB2
    with fade
    show SH Gn
    "오늘도 어김없이 같은 시간에 일어나 씻기 위해 욕실에 들어갔다.
    \n샤워를 하기 위해 서광호는 샤워기를 틀었다."

    hide SH Gn
    menu:
        "해바라기 샤워기":
            show SH Gn
            "서광호는 위에서 떨어지는 물을 맞으며 오늘의 일정을 생각했다."
            "빈틈이 없는 그는 샤워하는 모습도 마치 CF의 한 장면 같았다."

        "코브라 샤워기":
            show SH Gn3
            "서광호는 평소와 다른 욕실의 모습에 혼란스러웠다."
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            "그의 눈에 코브라 샤워기는 너무 기괴하게 보였다."
            scene black
            with dissolve
            "이에 충격을 받은 서광호는 그만 정신을 잃고 말았다......"
            $ persistent.ending1 = '1.코브라 샤워기가 뭐지.'
            $ persistent.ec1 = True
            show text '{size=25}{color=#FFFFFF}1.코브라 샤워기가 뭐지.{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

    scene bgS SKL
    with fade
    show SH Gn
    "샤워가 끝난 후 간단히 아침을 해결하기 위해 서광호는 냉장고로 향했다."
    "냉장고를 열자 안에 있던 어떤 음식이 눈에 띄었다."

    hide SH Gn
    menu:
        "프랑스 빙하수":
            show SH Gn
            "서광호에게 아침을 먹을 시간 따위는 없다.
            \n그는 1분 1초가 아까운 남자다."
            "망설임없이 프랑스 빙하수를 집어 배를 채우곤 출근 준비를 시작했다."

        "먹다 남은 치킨":
            show SH Gn
            "이런 음식이 서광호의 집에 있을리가 없다."
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            scene black
            with dissolve
            "서광호는 현실과의 괴리감을 느끼고 그만 정신을 잃고 말았다."
            $ persistent.ending2 = '2.냉장고에 그런 게 있을 리 없잖아요...'
            $ persistent.ec2 = True
            show text '{size=25}{color=#FFFFFF}2.냉장고에 그런 게 있을 리 없잖아요...{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

    "서광호는 물을 마신 뒤에 출근 준비를 위해 드레스룸으로 향했다."
    scene bgS SKL
    with fade
    show SH Si
    "늘 입던 것과 같은 옷을 입고, 손목에는 시계를 착용했다."

    hide SH Si
    menu:
        "명품 시계":
            show SH Si
            "서광호는 정말 머리부터 발끝까지 완벽했다.
            \n잘생긴 데다가 일도 잘하고 심지어 돈도 많았다."
            "서광호는 가지런히 정리된 명품시계 중 하나를 손목에 찬 뒤 집을 나섰다."

        "스마트 워치":
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            show SH Si
            "이전에 선물 받았던 스마트워치가 오늘따라 눈에 띄었다."
            "스마트워치를 차고 집을 나서자 어떤 소리가 들렸다."
            "\"현재 심박수는 70bpm 편안한 상태입니다.\""
            "\"현재 심박수는 85bpm 안정이 필요한 상태입니다.\""
            show SH Si2
            "계속되는 소음에 서광호는 신경질이 났다."
            "\"현재 심박수는 120bpm 안정을 취해주십시오.\""
            scene black
            with dissolve
            "알림이 계속 울리자 서광호는 혈압이 올라 그만 쓰러지고 말았다..."
            $ persistent.ending3 = '3.그 시계는 별로인데.'
            $ persistent.ec3 = True
            show text '{size=25}{color=#FFFFFF}3.그 시계는 별로인데.{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

    "서광호는 사람이 북적이는 곳은 질색이었기에 출근길에는 주로 자가용을 이용했다."
    scene bgS PT
    with fade
    show SH Si
    "그는 전용 주차장으로 내려가 자신의 차를 찾았다."
    "그리고는 차 키를 꺼내 차 문을 열고 차에 탑승했다."

    hide SH Si
    menu:
        "검은색 승용차":
            scene bgS SC
            with fade
            show SH Si
            "검은색 승용차는 그의 이미지와 딱 어울렸다.
            \n깔끔하고 잘 정돈된 느낌의 차내가 그를 반겼다."
            "서광호는 차에 탄 뒤 능숙한 운전으로 회사로 향했다."

        "붉은색 스포츠카":
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            show SH Si
            "스포츠카는 붉은색을 내뿜으며 휘황찬란하게 빛나고 있었다."
            hide SH Si
            show SH Si2
            "평생 이렇게까지 강렬한 색을 접한 경험이 별로 없는 그는 잘빠진 스포츠카의 강렬함에 눈이 멀어 버릴 거 같았다."
            scene black
            with dissolve
            "그리고 곧 눈앞이 깜깜해졌다...."
            $ persistent.ending4 = '4.차를 잘못 본 거 아니에요?'
            $ persistent.ec4 = True
            show text '{size=25}{color=#FFFFFF}4.차를 잘못 본 거 아니에요?{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

    scene bgS OE
    with fade
    show SH Si
    "회사에 도착한 뒤 서광호는 자리에 앉아 간단히 본인의 자리를 정리하고 곧 있을 오전 브리핑 때 사용할 펜을 찾았다."
    "기본적인 것들은 전산화되어있지만 서광호는 본 업무에 들어가기 전 수필로 간단하게 메모하는 습관이 있다."
    "서광호는 펜꽂이에서 펜을 집어 들고는 메모를 시작했다."

    hide SH Si
    menu:
        "만년필":
            show SH Si
            "서광호답게 사용하는 펜은 일반적으로 접하기 힘든 고급 만년필이었다."
            "검은색과 은색의 조화가 주는 고급스러운 분위기가 그와 잘 어울렸다."

        "당근 샤프":
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            show SH Si
            "그가 사용하기엔 너무 귀여운 샤프였다."
            S "'이런 게 왜 여기에 있는 거지.'"
            hide SH Si
            show SH Si2
            "라고 생각한 서광호는 왜인지 모를 불쾌감을 느끼며 속이 울렁거리는 듯한 느낌을 받았다."
            scene black
            with dissolve
            "당근 샤프에 충격을 받은 서광호는 그만 정신을 잃었다..."
            $ persistent.ending5 = '5.나는 그런 펜을 쓰지 않아.'
            $ persistent.ec5 = True
            show text '{size=25}{color=#FFFFFF}5.나는 그런 펜을 쓰지 않아.{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

    scene bgS OE
    with fade
    show SH Si
    "어느새 점심이 시간이 되어 간단하게 점심을 해결한 뒤, 서광호는 다시 업무를 보기 위해 자리에 앉았다.
    \n그때 노크 소리가 들리고 부하직원이 말을 건넸다."
    ea "사장님 커피 한잔 드시겠어요?"
    "머리를 식힐 겸 커피 한잔 정도는 괜찮다고 생각한 그는 부하직원의 물음에 응했다."
    S "그러지."

    "부하직원이 사 온 커피는?"

    hide SH Si
    menu:
        "아메리카노":
            show SH Si
            "한 잔의 아메리카노는 피로를 해소해주며 머리 회전에 도움이 된다."
            "커피의 맛 또한 적당히 산미가 있어 서광호는 나쁘지 않다고 생각했다."

        "바닐라 라떼":
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            show SH Si2
            S "'...평소 마시던 것과 다르군.'"
            "가볍게 들이켠 커피에서 강렬한 단맛이 났다."
            "서광호의 인생에 단 것은 치명적이다."
            scene black
            with dissolve
            "서광호는 순간 어지러움을 느끼고는 정신을 잃었다."
            $ persistent.ending6 = '6.그건...사장님은 안 좋아하실 것 같은데요..'
            $ persistent.ec6 = True
            show text '{size=25}{color=#FFFFFF}6.그건...사장님은 안 좋아하실 것 같은데요..{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

    scene bgS OE
    with fade
    show SH Si
    "점심시간 이후.
    \n주말동안 밀린 결재서류들을 처리하다 보니 퇴근 시간이었다."
    scene bgS SC
    with fade
    show SH Si
    "서광호는 휴식을 중요하게 여겼다.
    \n휴식을 취하는 것은 다음날 컨디션에 도움이 되기 때문이다."
    scene bgS SKL
    with fade
    show SH Pa
    "그는 집에 도착한 뒤 음악을 틀고 휴식을 취했다."

    hide SH Pa
    menu:
        "클래식":
            show SH Pa
            "클래식의 잔잔한 음색이 서광호의 마음을 편안하게 한다."
            "서광호는 클래식을 들으며 잠시 눈을 감고 편안하게 휴식을 취했다."

        "트로트":
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            show SH Pa
            "음악을 틀자 신나는 분위기의 트로트가 흘러나왔다."
            hide SH Pa
            show SH Pa2
            "서광호가 듣기엔 너무 시끄러웠고 그 때문에 머리가 아파졌다."
            scene black
            with dissolve
            "그는 머리를 부여잡더니 이내 바닥에 쓰러졌다."
            $ persistent.ending7 = '7.이 노래는 당신 취향인가?'
            $ persistent.ec7 = True
            show text '{size=25}{color=#FFFFFF}7.이 노래는 당신 취향인가?{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

    scene black
    with dissolve
    show text '챕터 1 End' at truecenter
    stop music fadeout 1.0
    with dissolve
    pause 2

show text '세이브를 생활화합시다' at truecenter
with dissolve
pause 2

show text '챕터 2' at truecenter
with dissolve
pause 2
hide text
with dissolve

jump ch2

#2챕터 스크립트

label ch2:
    scene bgS SB1
    with fade
    play music "/audio/Rainy_Blue_광호 일상.mp3" fadeout 1.0 fadein 1.0 loop
    show SH Pa
    "따스한 아침햇살이 서광호를 잠에서 깨웠다."
    hide SH Pa
    show SH Pa2
    "그에게 아침햇살은 그리 달갑지 않은 손님이다."
    "서광호는 짜증스레 커튼을 닫고, 출근 준비를 하기 위해 움직였다."
    scene bgS SB2
    with fade
    show SH Gn
    "씻기 위해 욕실에 들어간 서광호는, 머리를 감기 시작했다."

    hide SH Gn
    menu:
        "샴푸":
            show SH Gn
            "그의 욕실에는 그의 신경을 거슬리게 하지 않는 색상과 향의 세면도구들이 비치되어있다."

        "한방샴푸":
            show SH Gn
            "이전 협력사와의 미팅에서 신제품이라며 선물로 받은 한방 샴푸다."
            hide SH Gn
            show SH Gn2
            S "이건...처리하라고...일렀...을...텐데..."
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            "한방샴푸는 광공들의 체질과 맞지 않은 제품이 대부분이기에 사용할 경우 치명적인 부작용을 일으킨다."
            scene black
            with dissolve
            "차디찬 물줄기 아래, 서광호의 의식이 점점 흐려져 갔다."
            $ persistent.ending8 = '8.사장님 몸에서 한약 향이 나요..'
            $ persistent.ec8 = True
            show text '{size=25}{color=#FFFFFF}8.사장님 몸에서 한약 향이 나요..{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

    scene bgS SKL
    with fade
    show SH Gn
    "샤워를 마치고, 늘 그랬듯 프랑스 빙하수로 배를 채운 뒤, 빠르게 출근 준비를 끝냈다."
    "모든 과정을 같은 순서로 거친 다음, 서광호는 출근을 위해 차에 탔다."

    scene bgS SC
    with fade
    menu:
        "내비게이션":
            show SH Si
            "평소엔 잘 작동시키지 않는 내비게이션을 켰다."
            "내비게이션은 작동되자 말을 하기 시작했다."
            Nn "목적지를 말씀해주세요."
            "음성인식이 가능한 모델이었던 모양이다."
            S "회사."
            "서광호는 이 내비게이션을 한 번도 사용한 적이 없다."
            "당연하게도 내비게이션에는 회사의 정보가 입력되어 있지 않다."
            Nn "잘 모르겠어요. 다시 말씀해주세요."
            hide SH Si
            show SH Si2
            S "..회사."
            Nn "잘 모르겠어요. 다시 말씀해주세요."
            S "...회사."
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            "이와 같은 대화를 계속 반복하다가 서광호는 극심한 두통을 느꼈다."
            scene black
            with dissolve
            "그리고 그걸 끝으로 정신을 잃었다."
            $ persistent.ending9 = '9.이 기계는 형편없군.'
            $ persistent.ec9 = True
            show text '{size=25}{color=#FFFFFF}9.이 기계는 형편없군.{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

        "그냥 가기":
            show SH Si
            "서광호는 한 번 본 길은 한 번에 외울 정도로 머리가 좋았다."
            "따라서 출근길 같이 매일 반복되는 길은 내비게이션의 안내를 받을 필요도 없었다."
            "순조롭게 차를 몰아 회사로 향했다."

    scene bgS OE
    with fade
    show SH Si
    "회사에 도착해 자신의 위치로 향하는 서광호의 발걸음도 평소와 같았다."
    scene bgS OE
    with fade
    show SH Si
    "특별한 일이나 업무는 없었기 때문에, 일하다 보니 자연스레 점심시간이었다."
    Sy "사장님 그럼 점심은 어떻게 하시겠습니까?"

    hide SH Si
    menu:
        "편의점 도시락":
            show SH Si
            S "알아서 준비해."
            Sy "..네, 금방 준비해서 올리겠습니다."

            ea "XX 비서님이 바쁘셔서 제가 대신 준비했습니다."
            S "이건.."
            "서광호에게는 익숙하지 않은 음식이었다."
            ea "그럼 이만 나가보겠습니다."
            "그렇게 말한 직원은 문을 닫고 나갔다."
            S "'아마도 편의점에서 판매하는 것 같은데.'"
            hide SH Si
            show SH Si2
            S "하.."
            "한숨을 내쉰 서광호는 비서의 문제는 우선 미루고 도시락을 열어 한 입 먹어보았다."
            "그리고 곧 망설임 없이 쓰레기통에 버렸다."
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            "입안에 남은 맛은 서광호에게는 너무 끔찍한 맛이었다."
            scene black
            with dissolve
            "서광호는 얼굴을 찌푸리더니 이내 책상에 엎어지고 말았다..."
            $ persistent.ending10 = '10.우리 사장님은요..편의점 도시락을 못 드세요....'
            $ persistent.ec10 = True
            show text '{size=25}{color=#FFFFFF}10.우리 사장님은요..편의점 도시락을 못 드세요....{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

        "샐러드":
            show SH Si
            S "연어 아보카도 샐러드로."
            Sy "네, 금방 준비해서 올리겠습니다."
            "그는 까다로운 미각을 가졌기에 결코 아무 음식이나 먹지 않는다."
            "비서가 가져온 음식도 회사 근방의 한 셰프의 레스토랑에서 주문하여 가져온 것이다."
            "하지만 이런 음식마저 그냥 남겨질 때가 많았다."
            "서광호는 좋다 싫다 둘 중 어떤 감정도 없이 샐러드를 입에 넣었다."

    "점심시간을 마치고, 서광호는 업무로 복귀했다."
    scene bgS OE
    with fade
    show SH Si
    "얼마나 시간이 지났을까, 문을 두드리는 소리가 들렸다."
    S "들어와."
    hide SH Si
    show SH Si:
        xalign 0.5
        moveleft
    show IZ Ii:
        xalign 1.0
        moveright
    "비서가 누군가와 함께 안으로 들어왔다."
    "서광호는 누군지 설명하라는 말을 턱짓 한 번으로 대신했다."
    "서광호의 비서로 일한 것이 하루 이틀이 아니기에, 비서는 간단하게 소개를 했다."
    Sy "이쪽은 이번에 새로 입사한 비서, 이연조씨입니다."
    play music "/audio/おしゃれなカフェ_일상.mp3" fadeout 1.0 fadein 1.0 loop
    L "열심히 하겠습니다, 잘 부탁드립니다!"
    "잠시 이연조에게 향했던 비서의 시선은 다시 서광호에게로 향했다."
    Sy "추가적인 설명이 필요하십니까?"

    hide SH Si
    hide IZ Ii
    menu:
        "길게 듣는다.":
            show SH Si:
                xalign 0.25
            show IZ Ii:
                xalign 0.75
            "서광호는 다른 말 없이 고개를 끄덕였다."
            "그러자 비서의 설명이 이어졌다."
            Sy "이름 이연조, 나이 25세."
            Sy "XX 초등학교, XX 중학교, XX 고등학교를 졸업했습니다."
            Sy "그리고 XX 대학교를 졸업해 현재 우리 회사에 입사했습니다."
            Sy "이력으로는 XX 사에서 주최한 공모전 입상."
            Sy "XX 대학교 주-"
            hide SH Si
            show SH Si2:
                xalign 0.25
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            "끊임없이 이어지는 비서의 설명에 서광호는 치밀어오르는 답답함을 느꼈다."
            scene black
            with dissolve
            "그리고 그걸 해소하지 못한 채 기절하듯 쓰러지고 말았다."
            $persistent.ending11 = '11.저런 무능한 비서는 채용한 기억이 없는데.'
            $ persistent.ec11 = True
            show text '{size=25}{color=#FFFFFF}11.저런 무능한 비서는 채용한 기억이 없는데.{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

        "짧게 듣는다.":
            show SH Si:
                xalign 0.25
            show IZ Ii:
                xalign 0.75
            S "짧게 듣지."
            Sy "네."
            "비서 신입의 이력을 짧고 간결하게 정리해 소개했다."

    Sy "그럼 이만 데리고 나가보겠습니다."
    S "그래."
    hide IZ Ii
    hide SH Si
    show SH Si:
        xalign 0.25
        moveM
    play music "/audio/Rainy_Blue_광호 일상.mp3" fadeout 1.0 fadein 1.0 loop
    "비서와 이연조는 인사를 한 뒤, 다시 밖으로 나갔다."
    "서광호는 읽던 서류로 눈을 돌렸다."

    scene bgS OE
    with fade
    show SH Si
    "서광호가 퇴근 시간을 목전에 두고 결재를 진행하고 있었다."
    "작은 것들을 제외하고는 아무런 소리도 들리지 않는 방 안."
    "서광호는 마지막 결재를 마무리하고, 퇴근 시간이 되어 방 밖으로 나섰다."
    scene bgS OE
    with fade
    show SH Si
    play music "/audio/おしゃれなカフェ_일상.mp3" fadeout 1.0 fadein 1.0 loop
    Sy "이연조씨. 입사하자마자.."
    hide SH Si
    show SH Si:
        xalign 0.5
        moveleft
    show IZ Ii2:
        xalign 1.0
        moveright
    L "죄송합니다..죄송합니다..."
    S "무슨 일이지."
    Sy "아, 사장님 죄송합니다. 이연조씨가.."
    L "사장님, 저 그게..."

    "이연조의 이야기를 들을까?"

    hide SH Si
    hide IZ Ii2
    menu:
        "듣는다.":
            show SH Si:
                xalign 0.25
            show IZ Ii2:
                xalign 0.75
            S "말해봐."
            Sy "네?"
            hide IZ Ii2
            show IZ Ii:
                xalign 0.75
            L "앗..들어주실 건가요?"
            S "일단 들어보지."
            "서광호는 자신의 입이 멋대로 움직인다고 생각했다."
            "하지만 그렇다고 해서 이미 한 말을 번복할 마음도 들지 않았다."
            L "어떻게 된 거냐면요.."
            L "그러니까..! 여기 바닥이 미끄러워서 넘어지는 바람에..."
            hide SH Si
            show SH Si2:
                xalign 0.25
            S "세 살짜리 꼬마도 아니고 바닥이 미끄러워서 넘어지나?"
            "서광호는 이연조의 말을 어이없다고 여기며 퇴근을 하기 위해 발걸음을 옮겼다."
            "그 순간.."
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            scene black
            with dissolve
            "서광호는 미끄러졌고 이내 정신을 잃었다."
            $persistent.ending12 = '12.거봐요, 제가 미끄럽다고 했잖아요...'
            $ persistent.ec12 = True
            show text '{size=25}{color=#FFFFFF}12.거봐요, 제가 미끄럽다고 했잖아요...{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

        "듣지 않는다.":
            show SH Si:
                xalign 0.25
            show IZ Ii2:
                xalign 0.75
            S "무슨 일이지."
            "서광호는 이연조의 말을 가볍게 넘기고 비서에게 물었다."

    Sy "큰 실수는 아니지만, 서류가 뒤섞여버리는 바람에 그랬습니다."
    Sy "제가 알아서 처리하겠습니다."
    "이연조는 입을 다물고 안절부절못하는 모습이었다."

    hide SH Si
    hide IZ Ii2
    menu:
        "괜찮다며 타이르기":
            show SH Si4:
                xalign 0.25
            show IZ Ii2:
                xalign 0.75
            "작은 미소를 지으며 연조에게 다가갔다."
            S "그래도 너무 자책하지는 말고, 신입 시절에 실수는 누구나 할 수 있…윽…"
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            "서광호는 난생처음 지어보는 표정을 지으며 얼굴에 경련이 오는 걸 느꼈다."
            hide IZ Ii2
            show IZ Ii4:
                xalign 0.75
            L "사…사장님? 괜찮으세요??"
            S "뭐가..말이지…?"
            scene black
            with dissolve
            "서광호는 웃는 얼굴을 유지하려다 그만 얼굴에 경련이 와서 쓰러지고 말았다…"
            $persistent.ending13 = '13.내가 왜 타일러줘야 하지.'
            $ persistent.ec13 = True
            show text '{size=25}{color=#FFFFFF}13.내가 왜 타일러줘야 하지.{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

        "한숨 쉬기":
            show SH Si2:
                xalign 0.25
            show IZ Ii2:
                xalign 0.75
            "서광호는 한숨을 내쉬었다."
            S "그럼 난 이만 가보지."
            Sy "네, 조심히 들어가세요."
            L "조, 조심히 들어가세요!"

    stop music fadeout 1.0
    scene bgS SKL
    with fade
    show SH Pa2
    play music "/audio/Rainy_Blue_광호 일상.mp3" fadeout 1.0 fadein 1.0 loop
    "다사다난했던 일과가 끝이 나고, 그의 집으로 돌아온 서광호."
    "새로 들어온 신입 비서 때문에 머리가 지끈거리는 것 같았다."

    hide SH Pa2
    menu:
        "두피 마사지기를 이용한다.":
            show SH Pa
            "서광호의 눈에 이상하게 생긴 도구 하나가 들어왔다."
            "앞에 놓인 쪽지에는 '두피 마사지기'라는 이름과 사용법이 쓰여있었다."
            "이런 게 왜 여기 있는지 모르겠는 서광호였지만 이상하게 그 물건에 관심이 갔다."
            S "'이렇게 사용하는 건가..?'"
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            scene black
            with dissolve
            "두피마사지를 어색하게 사용하다가 급소를 건드려 서광호는 쓰러지고 말았다."
            $persistent.ending14 = '14.어떻게 하면 그걸로 급소를 건드려요?!'
            $ persistent.ec14 = True
            show text '{size=25}{color=#FFFFFF}14.어떻게 하면 그걸로 급소를 건드려요?!{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

        "두통약을 먹는다.":
            show SH Pa2
            "서광호는 두통약과 물을 입에 털어 넣었다."
            hide SH Pa2
            show SH Pa
            "조금 시간이 지나면 두통이 사라질 것이다."

    S "이연조…라고 했나."
    S "'그런 멍청한 비서라니..'"
    "서광호는 앞으로의 일들이 막막해진 것을 느끼며 잠을 청했다."

    scene black
    with dissolve
    show text '챕터 2 End' at truecenter
    stop music fadeout 1.0
    with dissolve
    pause 2

show text '세이브를 생활화합시다' at truecenter
with dissolve
pause 2

show text '챕터 3' at truecenter
with dissolve
pause 2
hide text
with dissolve

jump ch3

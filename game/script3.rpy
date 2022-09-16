#3챕터 스크립트

label ch3:
    scene bgS OE
    with fade
    play music "/audio/Rainy_Blue_광호 일상.mp3" fadeout 1.0 fadein 1.0 loop
    show SH Si
    "서광호는 이연조를 계속 지켜보기로 했다."
    "그리고 두 달 정도를 지켜본 결과, 이연조의 평가는 의외로 나쁘지 않았다."
    "서광호가 이연조를 관찰하게 된 이유는..."

    hide SH Si
    menu:
        '연조를 좋아해서':
            show SH Si
            S "'그래, 내가 이연조를 좋아해서..'"
            hide SH Si
            show SH Si3
            S "'음?'"
            "서광호는 스스로의 생각에 놀랐다."
            "누군가를 좋아한다니, 서광호에게는 말도 안 되는 이야기였다."
            "그럼에도 불구하고 이연조의 몇몇 모습들이 서광호의 기억에 새겨졌다."
            "그리고 이 기억들이 죽은 서광호의 연애 세포를 되살리는 계기가 된 것이다."
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            "하지만 모두가 알고 있듯이 세포 하나하나는 생명이다."
            scene black
            with dissolve
            "생명을 다시 되살리는 것에는 큰 대가가 따른다."
            $persistent.ending15 = '15.연애 세포는 살렸지만 나를 살리진 못했군.'
            $ persistent.ec15 = True
            show text '{size=25}{color=#FFFFFF}15.연애 세포는 살렸지만 나를 살리진 못했군.{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

        '별다른 이유 없이':
            show SH Si
            "별다른 이유는 없었다."
            "이연조의 존재감이 워낙 강해서거나,
            \n전의 비서들과는 전혀 다른 분위기 때문일지도 모르겠다."
            "아니면 그저 그의 업무상 눈에 보이는 일이 많아서일까."
            "서광호는 어느 쪽이든 크게 상관없다고 생각했다."

        '문제가 생겼을 때를 대비하기 위해':
            $ score += 1
            $ Gscore += 1
            show SH Si
            S "'그래야 문제가 있을 때 바로 해결할 수 있으니.'"
            S "'물론 문제 해결 이후에 이연조의 해고나 부서 이동도 고민해야 하겠지만.'"
            "이런 상황들에 대비하기 위해서는 꼭 필요한 일이었다."

    "예상한 것에 비해 큰 실수는 하지 않았고, 작은 실수가 많은 것도 아니었다."
    "서광호는 그 정도의 실수로 바로 사람을 바꾸지는 않는다."
    "애초에 적응이 좀 된 사람과 새로 들어온 사람 중에서는 전자가 나았다."
    "이런 것들과 상관없이, 서광호는 자신과 다른 이연조의 모습에 관심을 두게 되었다."
    "사람을 대할 때 항상 밝은 모습으로 대하려고 하는 것이나,
    \n모든 일을 긍정적으로 보려는 태도 같은 것들."
    "물론 서광호 스스로는 어떤 이유에서인지조차 알지 못했지만."

    scene bgS OE
    with fade
    show SH Si
    "오늘은 설명회 건으로 외근을 나가야 하는 날이었다."
    "다른 사람이 대신할 수 없는 일이라 서광호가 직접 가야만 했다."
    "이연조가 믿음직스럽지는 않지만, 다른 비서가 휴가를 떠났기 때문에 별다른 수가 없었다."
    hide SH Si
    show SH Si:
        xalign 0.0
        moveleft
    show IZ Ii2:
        xalign 1.0
        moveright
    play music "/audio/おしゃれなカフェ_일상.mp3" fadeout 1.0 fadein 1.0 loop
    "출발하려던 시간이 되었지만, 준비를 마쳤어야 할 이연조가 아직 꾸물대고 있었다."

    hide SH Si
    hide IZ Ii2
    menu:
        '연조의 등짝을 때린다':
            show SH Si:
                xalign 0.25
            show IZ Ii2:
                xalign 0.75
            S "정신."
            S "안 차리나?"
            "서광호가 이연조의 등짝을 찰싹찰싹 때렸다."
            hide IZ Ii2
            show IZ Ii4:
                xalign 0.75
            "이연조가 놀란 눈으로 서광호를 쳐다봤고, 서광호는 방정맞은 자신의 태도에 의문을 가졌다."
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            "이연조는 잠시 서광호를 빤히 바라보더니, 잠시 후 서광호의 등을 내리쳤다."
            scene black
            with dissolve
            "아무런 대비도 하고 있지 않았던 서광호는 그대로 앞으로 쓰러지며 머리를 부딪쳤다."
            $persistent.ending16 = '16.사장님. 눈에는 눈, 이에는 이에요.'
            $ persistent.ec16 = True
            show text '{size=25}{color=#FFFFFF}16.사장님. 눈에는 눈, 이에는 이에요.{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

        '화를 꾹 참고 연조를 도와준다':
            show SH Si:
                xalign 0.25
            show IZ Ii2:
                xalign 0.75
            "서광호는 치밀어 오르는 화를 꾹 참고 이연조에게 다가가 말을 걸었다."
            S "뭐가 문제지?"
            L "아 그게.. 파일을 정리하느라...죄송합니다 빨리하겠습니다!!"
            "서광호는 말없이 서류를 같이 정리해주곤 먼저 주차장으로 향했다."

        '연조를 뒤로 한 채 먼저 나가버린다':
            $ score += 1
            $ Gscore += 1
            show SH Si2:
                xalign 0.25
            show IZ Ii2:
                xalign 0.75
            S "'쓸 만하다고 생각을 하면 바로 저런 바보짓을…'"
            "서광호는 꾸물거리는 이연조를 무시하고 먼저 사무실 밖으로 나섰다."
            hide SH Si2
            with dissolve

    "이연조는 방을 나간 광호를 멍하니 바라보다가 자신도 급하게 따라나섰다."
    scene bgS SC
    with fade
    show SH Si:
        xalign 0.25
    show IZ Ii:
        xalign 0.75
    S "내 차니까 운전은 내가 하지. 이 비서는 조수석에 앉아."
    hide IZ Ii
    show IZ Ii4:
        xalign 0.75
    L "제가 못 미더우신 건가요?!"
    hide SH Si
    show SH Si2:
        xalign 0.25
    S "하…내가 이 비서 친구인가? 말은 가려서 하지. 선은 지켜."
    "그의 말대로 서광호는 이연조가 못 미더운 게 맞았다."
    "이연조를 쓸만한 비서라고는 생각하고 있지만, 그 이상은 아니었다."
    "'쓸만한' 정도의 비서에게 맡기느니 차라리 제가 하겠다는 의미다."
    scene bgS SC
    with fade
    show SH Si:
        xalign 0.25
    show IZ Ii:
        xalign 0.75
    play music "/audio/Rainy_Blue_광호 일상.mp3" fadeout 1.0 fadein 1.0 loop
    "이대로 평화롭게 도착하려나 생각하던 찰나에 길이 막히기 시작했다."
    hide IZ Ii
    show IZ Ii3:
        xalign 0.75
    L "사장님, 앞쪽에서 사고가 난 것 같은데요?"
    "무슨 일인지 알아보려고 열심히 앞쪽을 보던 이연조가 그렇게 말했다."

    hide SH Si
    hide IZ Ii3
    menu:
        "차에서 내려서 화를 낸다":
            scene bgS RD
            with fade
            show SH Si:
                xalign 0.0
                moveleft
            "서광호는 차 문을 열고 내렸다."
            show IZ Ii4:
                xalign 1.0
                moveright
            "이연조는 그 모습을 멍하니 지켜보다가 급하게 따라 내렸다."
            hide SH Si
            show SH Si5:
                xalign 0.25
            hide IZ Ii4
            show IZ Ii2:
                xalign 0.75
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            S "지금 뭐 하는 겁니까?!"
            ea "당신은 뭔데 소리를 지르고 난리야!"
            S "당신들 때문에 일정에 차질이 생겼습니다. 어떻게 책임질 거죠?"
            ea "뭔 소리야 우리가 사고 내고 싶어서 사고 냈어??"
            hide SH Si5
            show SH Si2:
                xalign 0.25
            S "하.. 말이 안 통하는군..."
            "결국, 말다툼이 주먹다짐이 되어버렸고 서광호는 밀쳐져 머리를 부딪쳤다."
            scene black
            with dissolve
            "그리고 정신을 잃었다."
            $persistent.ending17 = '17.내가 그 정도로 허술해 보이나?'
            $ persistent.ec17 = True
            show text '{size=25}{color=#FFFFFF}17.내가 그 정도로 허술해 보이나?{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

        "인상을 찌푸리고 한숨을 쉰다":
            show SH Si2:
                xalign 0.25
            show IZ Ii:
                xalign 0.75
            S "하..."
            "서광호는 인상을 찌푸린 채 한숨을 쉬었다."
            "시간약속을 중요히 여기는 그로서는 용납할 수 없는 일이었다."
            hide IZ Ii
            show IZ Ii3:
                xalign 0.75
            L "저.. 사장님 여기로 돌아서 가면 시간은 조금 걸리더라도 아슬아슬하게 맞춰서 도착할 수 있을 거예요."
            hide SH Si2
            show SH Si:
                xalign 0.25
            "서광호는 곁눈질로 핸드폰을 흘끗 보더니, 운전을 하기 시작했다."
            "원래도 알고 있는 길이기에 내비게이션을 켤 필요는 없었다."

        "다른 길을 찾는다":
            $ score += 1
            $ Gscore += 1
            show SH Si:
                xalign 0.25
            show IZ Ii:
                xalign 0.75
            "서광호는 알고 있는 길들을 잠시 떠올려보고는 핸들을 꺾었다."
            "사고 때문에 길이 막혀 늦어졌기 때문에 시간에 맞추기 위해서는 바로 움직여야 했다."

    S "이 비서. 행사장에 연락해서 시작 시간 늦추라고 연락해."
    L "넵!"

    scene bgS HY
    with fade
    show SH Si:
        xalign 0.0
        moveleft
    show IZ Ii:
        xalign 1.0
        moveright
    "해프닝이 있었지만, 그래도 크게 늦지 않게 목적지에 도착할 수 있었다."
    "안으로 들어서자 먼저 가 있던 본사 직원이 둘을 맞이했다."
    ea "오셨습니까, 사장님. 이쪽으로 모시겠습니다."
    hide IZ Ii
    show IZ Ii2:
        xalign 0.75
    "무미건조한 표정으로 세미나실로 향하는 서광호와 직원들."
    "그 주위에 감도는 공기는 삭막하기만 했다."
    hide SH Si
    show SH Si2:
        xalign 0.25
    "이번 신약 설명회에서 서광호가 어땠는지, 그의 아버지 귀에도 들어갈 것이다."
    "그런 자리에서 고의는 아니었으나,
    \n제시간에 도착하지 못하고 일정을 늦춘 것이 이미 마이너스가 될 터."
    "그 생각에 서광호는 벌써부터 머리가 아프기 시작했다."
    scene bgS HM
    with fade
    show SH Si2:
        xalign 0.0
        moveM
    "세미나실에 들어선 서광호는 표정을 굳힌 채 자리에 착석했다."
    hide SH Si2
    show IZ Ii:
        xalign 0.0
        moveM
    "그리고 이연조가 서광호를 대신해 설명회가 지연된 것에 대해 말하기 시작했다."
    L "안녕하세요. 서 사장님 비서 이연조라고 합니다."
    L "오는 길에 앞쪽에서 사고가 나는 바람에 설명회가 조금 지연되었습니다."
    L "다들 귀한 시간 내주셔서 참석해주셨을 텐데 불편하게 해드려 죄송합니다."
    hide IZ Ii
    "이연조가 분위기를 잘 환기해주어 세미나실 내의 삭막했던 기류는 나아졌다."
    show SH Si
    "서광호는 왜 시키지도 않은 짓을 하냐는 눈빛을 했지만, 이내 거두었다."

    scene bgS SC
    with fade
    show SH Si:
        xalign 0.25
    show IZ Ii:
        xalign 0.75
    "설명회는 무사히 끝났다."
    "두 사람은 올 때와 마찬가지로 같은 차를 이용해 회사로 돌아가는 길이었다."

    hide SH Si
    hide IZ Ii
    menu:
        "운다":
            show SH Si6:
                xalign 0.25
            show IZ Ii:
                xalign 0.75
            "서광호는 감동의 눈물을 흘리며 참 잘했다고 덕분에 살았다며 칭찬해줬다."
            hide IZ Ii
            show IZ Ii4:
                xalign 0.75
            "과한 리액션에 이연조는 당황스러움을 감추지 못했다."
            L "사장님..?"
            scene black
            with dissolve
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            "평소에 눈물을 흘려본 적 없는 서광호는 탈수로 그만 쓰러지고 말았다..."
            $persistent.ending18 = '18.사장님 우세요?'
            $ persistent.ec18 = True
            show text '{size=25}{color=#FFFFFF}18.사장님 우세요?{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

        "무표정하게 있는다":
            $ Gscore += 1
            show SH Si:
                xalign 0.25
            show IZ Ii:
                xalign 0.75
            "서광호는 별다른 표정 없이 묵묵히 운전했다."
            "평소와 크게 다를 것이 없어서인지 이연조도 서광호도 이상하게 생각하지 않았다."

        "수고했다고 말한다":
            $ score += 1
            show SH Si:
                xalign 0.25
            show IZ Ii:
                xalign 0.75
            "서광호가 입을 열자 이연조는 조금 긴장한 듯 보였다."
            S "수고했어."
            hide IZ Ii
            show IZ Ii4:
                xalign 0.75
            L "네??"
            "서광호는 두 번 말하지 않았다."
            hide IZ Ii4
            show IZ Ii5:
                xalign 0.75
            "이전 같으면 신나서 계속 말을 걸었을지도 모르지만,
            \n두 달을 일하며 서광호에게 적응한 이연조는 속으로만 기뻐했다."

    scene bgS OE
    with fade
    show SH Si
    "며칠 뒤, 두 사람은 급하게 처리해야 할 일이 생겨 야근을 하게 되었다."
    "서광호가 한참 일을 하는 도중, 문을 두드리는 소리가 들리더니 곧 열렸다."
    hide SH Si
    show SH Si:
        xalign 0.5
        moveleft
    show IZ Ii:
        xalign 1.0
        moveright
    play music "/audio/おしゃれなカフェ_일상.mp3" fadeout 1.0 fadein 1.0 loop
    "열린 문에서는 어찌 보면 당연하게도 이연조가 나왔다."
    hide IZ Ii
    show IZ Ii5:
        xalign 0.75
    L "야근할 때는 역시 야식이죠!"
    "그렇게 말하며 이연조는 서광호를 끌고 가기 시작했다."
    scene bgS OE
    with fade
    show IZ Ii5:
        xalign 0.0
        moveright
    show SH Si:
        xalign 0.0
        moveleft
    "이전 같으면 거절했을 서광호지만, 오늘은 순순히 이연조를 따라 직원 휴게실로 향했다."
    L "짜잔! 타코야끼랑 마카롱이에요!"
    "이연조는 의자를 꺼낸 뒤 반강제로 서광호를 앉혔다."
    L "마실 것도 있어요!"
    "부스럭대는 소리를 내며 이연조가 비닐봉지에서 무언가를 꺼내 들었다."

    hide IZ Ii5
    hide SH Si
    menu:
        '맥주':
            show IZ Ii:
                xalign 0.75
            show SH Si:
                xalign 0.25
            "테이블 위에 올려진 것은 맥주였다."
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            "서광호는 어이가 없었다."
            "아무리 야근이라고는 하지만 업무 중이었다."
            "게다가 집에서 하는 재택근무도 아니고 회사에서 술이라니."
            hide SH Si
            show SH Si5:
                xalign 0.25
            S "지금 제정신입니까?"
            hide IZ Ii
            show IZ Ii2:
                xalign 0.75
            L "아니 그게.."
            hide SH Si5
            show SH Si2:
                xalign 0.25
            S "회사에서 술이라니 대체.."
            L "아니 그러니까 이건-"
            S "됐습니다."
            "서광호는 그 말을 끝으로 자리에서 일어났다."
            hide IZ Ii2
            show IZ Ii6:
                xalign 0.75
            "그리고 이연조는 잠시 멍한 채로 있다가 정신을 차리고는 화를 냈다."
            L "이거 무알콜 맥주라고요!"
            "너무 화가 난 나머지 이연조가 집어던진 맥주 캔이 서광호의 머리를 향했다."
            scene black
            with dissolve
            "서광호는 바로 정신을 잃었다."
            $persistent.ending19 = '19.그런 것도 있나.'
            $ persistent.ec19 = True
            show text '{size=25}{color=#FFFFFF}19.그런 것도 있나.{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

        '콜라':
            show IZ Ii:
                xalign 0.75
            show SH Si:
                xalign 0.25
            L "콜라로 했는데, 혹시 안 드시나요?"
            "꺼내진 1.5리터짜리 콜라를 보며 서광호는 고개를 끄덕였다."
            "이연조는 아쉽다며 어쩔 수 없이 자신이 다 마셔야겠다고 말했다."
            S "'저걸 혼자 다 마실 생각인 건가.'"
            "물론 그렇다고 해서 서광호가 콜라를 마실 생각은 없었다."
            "그래서 그냥 알아서 해결하도록 두기로 했다."
            hide IZ Ii
            show IZ Ii5:
                xalign 0.75

        '물':
            $ score += 1
            $ Gscore += 1
            show IZ Ii5:
                xalign 0.75
            show SH Si:
                xalign 0.25
            L "회사에도 정수기는 있지만, 비서님이 가르쳐 주셔서요!"
            "사장님 물은 이것만 드신다면서요?
            \n라고 덧붙이며 이연조가 내민 것은 프랑스 빙하수였다."
            "서광호는 고개를 끄덕이며 이연조가 내민 페트병을 받아들었다."
            S "'자신이 비서라는 자각은 있었군.'"

    L "아 그리고 이거 회사 근처에 맛집으로 소문난 타코야끼 집에서 주문했거든요,
    \n하나 드셔보실래요?"
    "서광호가 타코야끼와 눈싸움을 할 기세로 째려보고 있자,
    \n이연조가 아예 젓가락으로 타코야끼를 집어 서광호의 입 앞으로 가져갔다."

    hide SH Si
    hide IZ Ii5
    menu:
        '한입에 먹는다':
            show SH Si:
                xalign 0.25
            show IZ Ii4:
                xalign 0.75
            "서광호는 아무 생각없이 뜨거운 타코야끼를 한입에 먹어버렸다."
            hide SH Si
            show SH Si2:
                xalign 0.25
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            "그리고 입안이 불타는 듯한 느낌을 받으며 인상을 썼다."
            scene black
            with dissolve
            "입천장을 데어버린 서광호는 처음 겪어 보는 종류의 고통에 충격을 받아 쓰러지고 말았다."
            $persistent.ending20 = '20.사장님 안에 타코야끼를 꾹 삼킨 채..'
            $ persistent.ec20 = True
            show text '{size=25}{color=#FFFFFF}20.사장님 안에 타코야끼를 꾹 삼킨 채..{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

        '아주 조금만 먹는다':
            show SH Si:
                xalign 0.25
            show IZ Ii:
                xalign 0.75
            "이연조의 권유를 거절했다가는 또 귀찮게 굴 것이 뻔하기 때문에 서광호는 타코야끼를 아주 조금만 베어 물었다."
            hide SH Si
            show SH Si2:
                xalign 0.25
            "질척거리는 식감에 서광호는 기분이 나빠졌다."
            "서광호는 미간을 찌푸렸다."
            hide IZ Ii
            show IZ Ii3:
                xalign 0.75
            L "입에 안 맞으세요..?"
            "서광호는 고개를 끄덕이고는 물로 입을 헹궜다."
            hide SH Si2
            show SH Si:
                xalign 0.25
            hide IZ Ii3
            show IZ Ii:
                xalign 0.75

        '안 먹는다':
            $ score += 1
            $ Gscore += 1
            show SH Si:
                xalign 0.25
            show IZ Ii:
                xalign 0.75
            "서광호는 손을 잡아 타코야끼를 이연조의 입 앞으로 가져다줬다."
            S "취향이 아니라서."

    L "그럼 마카롱은 어떠세요? 비싼 건 아니지만.."
    "다음으로 이연조가 내민 것은 서광호가 아는 것과는 달랐다."
    "원래도 단 것을 즐기지 않는 서광호이기에 필링이 가득 들어간 마카롱이 입에 맞을 리가 없다."
    S "난 됐어."
    "그리고 서광호는 테이블에서 일어났다."
    "이연조가 조금 실망한 것 같았지만 그렇다고 서광호가 억지로 입에 안 맞는 음식을 먹을 이유는 없었다."
    hide SH Si
    show SH Si:
        xalign 0.25
        movell
    hide SH Si
    "천천히 먹어도 상관없다는 말을 한 뒤 서광호는 다시 집무실로 향했다."

    scene bgS OE
    with fade
    play music "/audio/Rainy_Blue_광호 일상.mp3" fadeout 1.0 fadein 1.0 loop
    "꽤 늦은 시각, 모든 업무가 끝이 났다."
    show SH Si:
        xalign 0.0
        moveleft
    show IZ Ii:
        xalign 0.75
    S "이제 그만 가지."
    L "아 네..!"
    scene bgS SC
    with fade
    show SH Si
    "서광호가 주차장을 나섰을 때, 회사 앞에서 고민하는 이연조가 눈에 띄었다."
    "이연조의 근처로 차를 몬 서광호가 이유를 묻자 교통편 때문이라는 것을 알게 되었다."
    "서광호는 어쩔 수 없었다고는 하지만 야근의 이유가 자신에게도 있다고 생각했다."
    S "타."
    hide SH Si
    show SH Si:
        xalign 0.5
        moveleft
    show IZ Ii4:
        xalign 1.0
    L "네?"
    S "차에 타. 데려다주지."
    hide IZ Ii4
    show IZ Ii:
        xalign 1.0
        moveright
    L "넵."
    "차에 올라탄 이연조에게 집을 묻자 근처의 지하철역을 말했다."

    hide SH Si
    hide IZ Ii
    menu:
        '종이 지도를 펼친다':
            show SH Si:
                xalign 0.25
            show IZ Ii:
                xalign 0.75
            "그 순간 서광호는 전국 지도를 펼쳤다."
            S "여기서 어디지?"
            hide IZ Ii
            show IZ Ii2:
                xalign 0.75
            "이연조는 여기서 지하철역을 찍으라는 건가 싶어 당황한 표정으로 서광호를 바라봤다."
            L "어..음..대충 이정도일까..요..?"
            "서광호는 알았다는 듯 종이 지도를 보며 운전을 시작했다."
            play music "/audio/hard rain_선택지 잘못 골랐을 때.mp3" fadeout 1.0 fadein 1.0 loop
            "하지만 도착할리는 없었고 이상한 길로만 빙빙 돌다가 결국 아침이 밝고 말았다..."
            scene black
            with dissolve
            "서광호는 오랜 운전으로 인해 지쳤고 갓길에 차를 세운 후 쓰러지고 말았다."
            $persistent.ending21 = '21.전국 지도를 사용해 본 건 처음이군.'
            $ persistent.ec21 = True
            show text '{size=25}{color=#FFFFFF}21.전국 지도를 사용해 본 건 처음이군.{/color}{/size}' at truecenter
            with dissolve
            stop music fadeout 1.0
            pause 1
            hide text
            with dissolve
            return

        '연조에게 알려달라고 한다':
            show SH Si:
                xalign 0.25
            show IZ Ii5:
                xalign 0.75
            "서광호가 잘 알지 못하는 곳이라 이연조에게 길을 물었다."
            L "제가 잘 안내해드릴게요!"
            "자신 있게 말한 것과는 별개로, 이연조는 안내에 소질이 없었던 모양이다."
            "그래도 조금 헤맸을 뿐 무사히 역에 도착할 수 있었다."

        '이미 알고 있다':
            $ score += 1
            $ Gscore += 1
            show SH Si:
                xalign 0.25
            show IZ Ii:
                xalign 0.75
            S "'그 근처인가.'"
            "서광호는 웬만한 길은 다 알고 있었기에 그 이상의 대화는 필요치 않았다."
            "조금씩 말을 거는 이연조에게 짧은 답변을 돌려주기는 했지만."

    scene bgS SC
    with fade
    show SH Si:
        xalign 0.25
    show IZ Ii:
        xalign 0.75
    "서광호는 이연조가 내리기 전,
    \n오늘은 수고했으니 다음 날은 오후에 출근해도 좋다는 말을 덧붙였다."

    #play music "/audio/Rainy_Blue_광호 일상.mp3" fadeout 1.0 fadein 1.0 loop
    scene bgS OE
    with fade
    show SH Si
    "점심시간 끝날 때가 지났음에도 이연조가 오지 않았다."
    "서광호는 자기가 너무 늦게까지 남겨둔 탓에 몸살이라도 걸려 일에 지장이 갈까 봐 신경이 쓰였다."
    "얼마나 지났을까, 밖에서 큰 소리가 들려왔다."
    play music "/audio/ころころピアノ_연조 지각.mp3" fadeout 1.0 fadein 1.0 loop
    hide SH Si
    show SH Si:
        xalign 0.0
        moveleft
    show IZ Ii7:
        xalign 1.0
        moveright
    "무슨 이유인지 확인하려고 나온 서광호의 시야에,
    \n누가 봐도 지각했다는 것을 알 수 있을 이연조가 들어왔다."
    L "늦어서 죄송합니다!!!"
    S "'기운찬 걸 보니 아픈 건 아니군.'"
    S "앉아서 일이나 해."
    "평소 같았으면 차가운 태도로 이연조를 혼냈을 것이다."
    "하지만 어제 무리시킨 일이 마음에 걸렸는지 서광호는 별 말없이 일에만 집중했다."

    scene black
    with dissolve
    show text '챕터 3 End' at truecenter
    with dissolve
    stop music fadeout 1.0
    pause 3

show text '세이브를 생활화합시다' at truecenter
with dissolve
pause 3

show text '챕터 4' at truecenter
with dissolve
pause 3
hide text
with dissolve

jump ch4

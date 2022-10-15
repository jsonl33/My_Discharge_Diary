define player = Character("[playerName]")
define kwon = Character("권상병", color = "#aaccff") 
define lee = Character("이병장", color = "#FF6219")

image kwon_happy = "kwon_happy.png"
image kwon_angry = "kwon_angry.png"
image kwon_vangry = "kwon_veryangry.png"
image kwon_vhappy = "kwon_veryhappy.png"
image kwon_blankmind = "kwon_blankmind.png"

image kwon = "kwon.png"
image lee = "lee.png"
image lim = "lim.png"
image kim = "kim.png"

image office = "bg_office.png"
image barrack = "bg_barrack.png"
image entrance = "bg_entrance.png"
image bedroom = "bg_bedroom.png"

image youdied = "bg_youdied.png"

default kwon_affection = 0

label start:
    scene black

    "이 게임에 나오는 등장인물들은 실존인물을 바탕으로 만들어진 허구의 인물이며 실제 성격과 다소 다를 수 있습니다."
    "만든 이유도 프로그래밍 연습할겸 그냥 재미로 만든거니 과몰입 하시면 안됩니다 ㅇㅋ?"
    $ playerName = renpy.input("주인공의 이름을 입력해주십쇼: ")

    $ playerName = playerName.strip()
    if playerName == "":
        $ playerName = "호돌이"

    scene bedroom with dissolve
    player "후임들과 간부들에게 시달리고 근무로 찌들었던 날들..."
    player "내 전역은 이제 얼마 남지 않았고 오늘은 비번이다."
    player "복지시설 이용도 질리고 휴대폰으로 볼만한 것도 없으니 애들이랑 얘기나 하러 가볼까."
    jump kwon_route

label kwon_route:
    player "오늘은 권상병이나 만나러 가자."
    player "늘 그렇듯 행보관의 짬처리를 하고있을테니 행정반에 있겠지."
    "(당신은 행정반으로 향합니다.)"

    scene bg_office with dissolve

    show kwon at left with dissolve
    "예상했던대로 불쌍한 북극곰은 행정반에서 악랄한 인간들에게 노동착취를 당하고 있었습니다."
    "무슨 말을 하시겠습니까?"

    menu:
        "헤이 작은 아기고양이 여기서 뭐해?":
            jump choice1_a
        "많이 힘들지..?":
            jump choice1_b
        "주말에 일하는 흑우가 있다?!?! 엌ㅋㅋㅋㅋㅋㅋ":
            jump choice1_c

label choice1_a:
    hide kwon_happy
    show kwon_vangry 
    $ kwon_affection -= 10
    kwon "?? (눈빛에 경멸이 느껴집니다.)"
    kwon "난 곰이라곰."
    hide kwon_vangry with dissolve
    jump after_choice1
label choice1_b:
    hide kwon_happy
    show kwon_vhappy 
    $ kwon_affection += 10
    kwon "그래도 아직까진 견딜만 한 것 같아.."
    hide kwon_vhappy with dissolve
    jump after_choice1
label choice1_c:
    hide kwon_happy
    show kwon_angry 
    kwon "하..하..하..."
    hide kwon_angry with dissolve
    jump after_choice1

label after_choice1:
    show kwon_blankmind with dissolve
    "권상병은 넋나간 표정으로 다시 컴퓨터로 뭔가를 하기 시작합니다."
    player "이게 뭐하는거야?"
    hide kwon_blankmind
    show kwon_happy
    kwon "이건 0창에서 받아야 하는것들 품목이랑 수량 정리하는거고 이건 간부들 분기별 중식 예산이야."
    player "이야 보급관한테 제대로 짬처리 당했구나.. 힘들겠다"
    kwon "항상 그렇지 뭐.. [playerName] 너는 무슨 일로 왔어?"

    menu:
        "전역하면 아마 몇달은 못볼테니 얘기나 좀 하러 왔지.":
            jump choice2_a
        "내 맘이지 짬찌쉑 니가 고참의 맘을 알어?!?!":
            jump choice2_b
        "개인정비 못하고 일한다니까 꼽주러왔지 ㅋㅋㅋㅋㅋ":
            jump choice2_c

label choice2_a:
    hide kwon_happy
    show kwon_vhappy 
    $ kwon_affection += 10
    kwon "그래? 감동이네"
    hide kwon_vhappy
    jump after_choice2
label choice2_b:
    hide kwon_happy
    show kwon_vangry
    $ kwon_affection -= 10
    kwon "?? 그렇긴 하지.."
    hide kwon_vangry
    jump after_choice2
label choice2_c:
    hide kwon_happy
    show kwon_angry 
    kwon "허허.."
    hide kwon_angry
    jump after_choice2

label after_choice2:
    show kwon_happy
    kwon "그러고보니까 [playerName] 너 전역이 얼마 안남았구나.."
    player "그러게 벌써 시간이 이렇게 됐네"
    kwon "너한테 이래저래 도움도 많이 받고 많이 배웠는데 조금 아쉽긴 하다"

    menu:
        "너 전문하사 한다고 하면 나도 생각해봄 ㅋ":
            jump choice3_a
        "아쉽긴 해도 갈 사람은 가야지 어쩌겠나!":
            jump choice3_b
        "그러게 갈 때 되면 하나도 안아쉬울 줄 알았는데..":
            jump choice3_c

label choice3_a:
    $ kwon_affection -= 10
    kwon "어후 그건 좀..."
    hide kwon_happy
    jump after_choice3
label choice3_b:
    hide kwon_happy
    show kwon_vhappy  
    kwon "그게 맞지 ㅋㅋ"
    hide kwon_vhappy
    jump after_choice3
label choice3_c:
    hide kwon_happy
    show kwon_vhappy 
    $ kwon_affection += 10
    kwon "그 동안 잘 해줘서 고마웠어."
    hide kwon_vhappy
    jump after_choice3

label after_choice3:
    lee "상황실에서 전파드립니다.\n현 시간부로 임무 분담제에 의한 청소 실시해주시고 생활관 및 담당구역 환기 실시해주시기 바랍니다."
    player "아 벌써 청소시간이네 가야겠다"
    kwon "그러게 얘기 재밌었어 잘가"
    scene black with fade
    "그렇게 시간이 흘러 기다리고 기다리던 전역날이 되었다."
    jump kwon_ending

label kwon_ending:
    if kwon_affection == 0:
        scene barrack with dissolve
        "집으로 가려던 중 우연히 권상병을 마주쳤다."
        player "나 간다 남은 군생활 잘 해라."
        kwon "잘가 [playerName] 가끔 생각나면 연락할게"
        player "그래 언젠가 인연이 닿으면 보자."
        "그렇게 난 전역을 했고 수 개월이 지난 지금 권상병과 딱히 연락을 주고받거나 하진 않고있다."
        "언젠가 인연이 닿으면 볼 수도 있겠지."
        "-노멀엔딩-"
    elif 10 <= kwon_affection < 30:
        scene barrack with dissolve
        "집으로 가려던 중 권상병을 마주쳤다. 나를 기다린 듯하다."
        player "나 간다 남은 군생활 잘 해라."
        "권상병이 미련 가득한 눈빛으로 당신을 바라봅니다."
        kwon "그리울거야 [playerName] 잘 가고 나도 전역하면 가끔 얼굴 보고 살자."
        player "그래 ㅋㅋ 고생해라"
        "그렇게 계속 연락을 주고받다가 수 개월이 지나 권상병도 전역을 했고 가끔 만나 밥이나 한끼 하면서 인생얘기 하는 좋은 친구가 되었다."
        "-해피엔딩-"
    elif kwon_affection >= 30:
        scene entrance with dissolve
        player "야~ 이제 들어가 뭐하러 여기까지 나왔어"
        "권상병은 금방이라도 울 것 같습니다."
        "저벅저벅"
        "와락"
        "권상병이 당신을 끌어안습니다."
        player "아 새끼 안울려고 했는데 눈물나게.."
        "권상병이 미련 가득한 눈빛으로 당신을 바라봅니다."
        kwon "잘가 [playerName]"
        "멀리서 서서히 동이 틉니다."
        "남자는 등으로 인사하는 법이니 당신은 뒤돌아보지 않고 손짓으로 인사합니다."
        "그렇게 당신과 권상병은 절친이 되었고 수 년이 지난 지금도 딱히 멀어질 것 같지 않습니다."
        "-베스트엔딩-"
    elif -10 >= kwon_affection > -30 :
        scene entrance with dissolve
        "당신은 집으로 가는 길에 전우들과 인사를 나눴고 권상병과도 인사를 하고 싶었지만 결국 마주치지 못했습니다."
        player "뭐 어쩔 수 없지 모두와 친하게 지낼 순 없는거니까.."
        player "이 찝찝함은 아마 오래도록 나와 함께 할 것 같다.."
        "-배드엔딩-"
    elif  kwon_affection <= -30:
        scene barrack with dissolve
        "집으로 가려던 중 권상병을 마주쳤다. 나를 기다린 듯하다."
        "눈빛이 조금 이상하다. 평소의 권상병이 아닌 것 같다.."
        player "어.. 저기.. 권상병?"
        kwon "\"쿠어엉\""
        "권상병의 몸에서 하얀 털이 돋아나고 키가 3m까지 커지며 이빨과 발톱이 자라납니다."
        "아무래도 북극곰이라는 별명은 별명이 아니라 진짜였나 봅니다."
        "하하 X발"
        # play audio "sfx/youdied.mp3" noloop
        scene youdied with Dissolve(3.0)
        pause(2.0)
        scene black with Dissolve(3.0)

return

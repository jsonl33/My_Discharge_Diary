define player = Character("[playerName]")
define kwon = Character("권상병")

label start:
    scene black

    "이 게임에 나오는 등장인물들은 실존인물을 바탕으로 만들어진 허구의 인물이며 실제 성격과 다소 다를 수 있습니다."
    "만든 이유도 프로그래밍 연습할겸 그냥 재미로 만든거니 과몰입 하시면 안됩니다 ㅇㅋ"
    $ playerName = renpy.input("주인공의 이름을 입력해주십쇼: ")

    $ playerName = playerName.strip()
    if playerName == "":
        $ playerName = "호돌이"

    player "후임들과 간부들에게 시달리고 근무로 찌들었던 날들..."
    player "내 전역은 이제 얼마 남지 않았고 오늘은 비번이다."
    player "복지시설 이용도 질리고 휴대폰으로 볼만한 것도 없으니 애들이랑 얘기나 하러 가볼까."
    jump kwon_route

label kwon_route:
    player "오늘은 권상병이나 만나러 가자."
    player "늘 그렇듯 행보관의 짬처리를 하고있을테니 행정반에 있겠지."
    "(당신은 행정반으로 향합니다.)"

    "저벅저벅"

    "예상했던대로 불쌍한 북극곰은 행정반에서 악랄한 인간들에게 노동착취를 당하고 있었습니다."
    "무슨 말을 하시겠습니까?"

    
                

return

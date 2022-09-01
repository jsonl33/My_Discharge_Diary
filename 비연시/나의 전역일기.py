import time
import os

def clearWithTime():
    time.sleep(1)
    os.system("cls")
    
def playerName():
    playerName = input("주인공의 이름을 입력해주십쇼: ")
    time.sleep(1)
    os.system("cls")
    return playerName
    
def userSelection():
    print()
    userSelection = int(input("선택: "))
    time.sleep(1)
    os.system("cls")
    return userSelection

def pressEnterToContinue():
    print()
    input("계속하려면 엔터를 눌러주십쇼.")
    time.sleep(1)
    os.system("cls")

heroine = ["권상병","김병장","이병장"]

while True:
    relationshipPoint = 0

    def change_relationship_point(plus_or_minus):
        global relationshipPoint

        if plus_or_minus == "+":
            relationshipPoint = relationshipPoint + 10
            print("호감도가 10 상승했습니다.")
            print("현재 호감도: {}".format(relationshipPoint)) 
        elif plus_or_minus == "-":
            relationshipPoint = relationshipPoint - 10
            print("호감도가 10 하락했습니다.")
            print("현재 호감도: {}".format(relationshipPoint))
        pressEnterToContinue()

    print("-"*40)
    print()
    print("\t     나의 전역일기")
    print()
    print("-"*40)
    print("1. 게임시작")
    print("2. 종료")
    print()
    gameStart = int(input("입력: "))
    clearWithTime()

    if gameStart == 1:
        print("                                    *************주의*************")
        print("이 게임에 나오는 등장인물들은 실존인물을 바탕으로 만들어진 허구의 인물이며 실제 성격과 다소 다를 수 있습니다.")
        print("만든 이유도 프로그래밍 연습할겸 그냥 재미로 만든거니 과몰입 하시면 안됩니다 ㅇㅋ?")
        pressEnterToContinue()

        playerName = input("주인공의 이름을 입력해주십쇼: ")
        time.sleep(1)
        os.system("cls")

        print("{}: 후임들과 간부들에게 시달리고 근무로 찌들었던 날들...".format(playerName))
        pressEnterToContinue()

        print("{}: 내 전역은 이제 얼마 남지 않았고 오늘은 비번이다.".format(playerName))
        pressEnterToContinue()

        print("{}: 복지시설 이용도 질리고 휴대폰으로 볼만한 것도 없으니 애들이랑 얘기나 하러 가볼까.".format(playerName))
        pressEnterToContinue()

        print("누구를 만나러 가시겠습니까? ※현재 기술적인 이유로 {} 외에 선택 불가능합니다※".format(heroine[0]))
        print()
        print("1. {}".format(heroine[0]))
        print("2. {}".format(heroine[1]))
        print("3. {}".format(heroine[2]))
        print()
        characterSelect = int(input("입력: "))
        clearWithTime()


        
        if characterSelect == 1:
            print("{}: 그래 오늘은 {}이나 만나러 가자.".format(playerName, heroine[0]))
            pressEnterToContinue()

            print("{}: 늘 그렇듯 행보관의 짬처리를 하고있을테니 행정반에 있겠지.".format(playerName))
            print("(당신은 행정반으로 향합니다.)")
            pressEnterToContinue()

            print("예상했던대로 불쌍한 북극곰은 행정반에서 악랄한 인간들에게 노동착취를 당하고 있었습니다.")
            pressEnterToContinue()

            print("무슨 말을 하시겠습니까?")
            print()
            print("1. 헤이 작은 아기고양이 여기서 뭐해?")
            print("2. 많이 힘들지..?")
            print("3. 주말에 일하는 흑우가 있다?!?! 엌ㅋㅋㅋㅋㅋㅋ")
            conversationSelect = int(input("입력: "))
            clearWithTime()
            
            if conversationSelect == 1:
                change_relationship_point("-")

                print("{}: ?? (눈빛에 경멸이 느껴집니다.)".format(heroine[0]))
                pressEnterToContinue()
        
            elif conversationSelect == 2:
                change_relationship_point("+")
    
                print("{}: 그래도 아직까진 견딜만 한 것 같아..".format(heroine[0]))
                pressEnterToContinue()
        
            elif conversationSelect == 3:
                print("{}: 하.하.하...".format(heroine[0]))
                pressEnterToContinue()

            print("{}은 넋나간 표정으로 다시 컴퓨터로 뭔가를 하기 시작합니다.".format(heroine[0]))
            pressEnterToContinue()

            print("{}: 이게 뭐하는거야?".format(playerName))
            pressEnterToContinue()

            print("{}: 이건 0창에서 받아야 하는것들 품목이랑 수량 정리하는거고 이건 간부들 분기별 중식 예산이야.".format(heroine[0]))
            pressEnterToContinue()

            print("{}: 이야 보급관한테 제대로 짬처리 당했구나.. 힘들겠다".format(playerName))
            pressEnterToContinue()

            print("{}: 항상 그렇지 뭐.. {} 너는 무슨 일로 왔어?".format(heroine[0], playerName))
            pressEnterToContinue()

            print("무슨 말을 하시겠습니까?")
            print()
            print("1. 전역하면 아마 몇달은 못볼테니 얘기나 좀 하러 왔지.")
            print("2. 내 맘이지 짬찌쉑 니가 고참의 맘을 알어?!?!")
            print("3. 개인정비 못하고 일한다니까 꼽주러왔지 ㅋㅋㅋㅋㅋ")
            print()
            conversationSelect = int(input("입력: "))
            clearWithTime()
    

            if conversationSelect == 1:
                change_relationship_point("+")   

                print("{}: 그래? 감동이네".format(heroine[0]))
                pressEnterToContinue()      

            elif conversationSelect == 2:
                change_relationship_point("-")

                print("{}: ?? 그렇긴 하지..".format(heroine[0]))
                pressEnterToContinue()

            elif conversationSelect == 3:
                print("{}: 허허..".format(heroine[0]))
                pressEnterToContinue()

            print("{}: 그러고보니까 {} 너 전역이 얼마 안남았구나..".format(heroine[0],playerName))
            pressEnterToContinue()

            print("{}: 그러게 벌써 시간이 이렇게 됐네".format(playerName))
            pressEnterToContinue() 

            print("{}: 너한테 이래저래 도움도 많이 받고 많이 배웠는데 조금 아쉽긴 하다".format(heroine[0]))
            pressEnterToContinue()  

            print("무슨 말을 하시겠습니까?")
            print()
            print("1. 너 전문하사 한다고 하면 나도 생각해봄 ㅋ")
            print("2. 아쉽긴 해도 갈 사람은 가야지 어쩌겠나!")
            print("3. 그러게 갈 때 되면 하나도 안아쉬울 줄 알았는데..")
            print()
            conversationSelect = int(input("입력: "))
            clearWithTime()
    

            if conversationSelect == 1:
                change_relationship_point("-")

                print("{}: 어후 그건 좀...".format(heroine[0]))
                pressEnterToContinue()
        
            elif conversationSelect == 2:
                print("{}: 그게 맞지 ㅋㅋ".format(heroine[0]))
                pressEnterToContinue()       

            elif conversationSelect == 3:
                change_relationship_point("+")     

                print("{}: 그 동안 잘 해줘서 고마웠어.".format(heroine[0]))
                pressEnterToContinue()       
            
            print("{}: 상황실에서 전파드립니다.\n현 시간부로 임무 분담제에 의한 청소 실시해주시고 생활관 및 담당구역 환기 실시해주시기 바랍니다.".format(heroine[2]))
            pressEnterToContinue()

            print("{}: 아 벌써 청소시간이네 가야겠다".format(playerName))
            pressEnterToContinue()

            print("{}: 그러게 얘기 재밌었어 잘가".format(heroine[0]))
            pressEnterToContinue()

            print("그렇게 시간이 흘러 기다리고 기다리던 전역날이 되었다.")
            pressEnterToContinue()

            # 엔딩 분기
            if relationshipPoint == 0:
                print("집으로 가려던 중 우연히 {}을 마주쳤다.".format(heroine[0]))
                pressEnterToContinue()       

                print("{}: 나 간다 남은 군생활 잘 해라.".format(playerName))
                pressEnterToContinue()

                print("{}: 잘가 {} 가끔 생각나면 연락할게".format(heroine[0],playerName))
                pressEnterToContinue()

                print("{}: 그래 언젠가 인연이 닿으면 보자.".format(playerName))
                pressEnterToContinue()

                print("그렇게 난 전역을 했고 수 개월이 지난 지금 {}과 딱히 연락을 주고받거나 하진 않고있다.".format(heroine[0]))
                pressEnterToContinue()

                print("언젠가 인연이 닿으면 볼 수도 있겠지.")
                pressEnterToContinue()

                print("-"*40)
                print()
                print("\t\t노멀 엔딩")
                print()
                print("-"*40)
                print()
                pressEnterToContinue()
                
            elif 10 <= relationshipPoint < 30:
                print("집으로 가려던 중 {}을 마주쳤다. 나를 기다린 듯하다.".format(heroine[0]))
                pressEnterToContinue()       

                print("{}: 나 간다 남은 군생활 잘 해라.".format(playerName))
                pressEnterToContinue()

                print("{}이 미련 가득한 눈빛으로 당신을 바라봅니다.".format(heroine[0]))
                pressEnterToContinue()

                print("{}: 그리울거야 잘 가고 나도 전역하면 가끔 얼굴 보고 살자.".format(heroine[0]))
                pressEnterToContinue()

                print("{}: 그래 ㅋㅋ 고생해라".format(playerName))
                pressEnterToContinue()      

                print("그렇게 계속 연락을 주고받다가 수 개월이 지나 {}도 전역을 했고 가끔 만나 밥이나 한끼 하면서 인생얘기 하는 좋은 친구가 되었다.".format(heroine[0]))
                pressEnterToContinue()

                print("-"*40)
                print()
                print("\t\t해피 엔딩")
                print()
                print("-"*40)
                print()
                pressEnterToContinue()

            elif relationshipPoint >= 30:
                print("{}: 야~ 이제 들어가 뭐하러 여기까지 나왔어".format(playerName))
                pressEnterToContinue()

                print("{}은 금방이라도 울 것 같습니다.".format(heroine[0]))
                pressEnterToContinue()

                print("저벅저벅")
                pressEnterToContinue()

                print("와락")
                pressEnterToContinue()

                print("{}이 당신을 끌어안습니다.".format(heroine[0]))
                pressEnterToContinue()

                print("{}: 아 새끼 안울려고 했는데 눈물나게..".format(playerName))
                pressEnterToContinue()

                print("{}이 미련 가득한 눈빛으로 당신을 바라봅니다.".format(heroine[0]))
                pressEnterToContinue()

                print("{}: 잘가".format(heroine[0]))
                pressEnterToContinue()

                print("멀리서 서서히 동이 틉니다.")
                pressEnterToContinue()

                print("남자는 등으로 인사하는 법이니 당신은 뒤돌아보지 않고 손짓으로 인사합니다.")
                pressEnterToContinue()

                print("그렇게 당신과 {}은 절친이 되었고 수 년이 지난 지금도 딱히 멀어질 것 같지 않습니다.".format(heroine[0]))
                pressEnterToContinue()

                print("-"*43)
                print()
                print("\t\t베스트 엔딩")
                print()
                print("-"*43)
                print()
                pressEnterToContinue()

            elif -10 >= relationshipPoint > -30 :
                print("당신은 집으로 가는 길에 전우들과 인사를 나눴고 {}과도 인사를 하고 싶었지만 결국 마주치지 못했습니다.".format(heroine[0]))
                pressEnterToContinue()    

                print("뭐 어쩔 수 없지 모두와 친하게 지낼 순 없는거니까..")
                pressEnterToContinue()

                print("이 찝찝함은 아마 오래도록 나와 함께 할 것 같다..")
                pressEnterToContinue()

                print("-"*40)
                print()
                print("\t\t배드 엔딩")
                print()
                print("-"*40)
                pressEnterToContinue()

            elif  relationshipPoint <= -30:
                print("집으로 가려던 중 {}을 마주쳤다. 나를 기다린 듯하다.".format(heroine[0]))
                pressEnterToContinue()

                print("눈빛이 조금 이상하다. 평소의 {}이 아닌 것 같다..".format(heroine[0]))
                pressEnterToContinue()

                print("{}: 어.. 저기.. {}?".format(playerName, heroine[0]))
                pressEnterToContinue()

                print("{}: \"쿠어엉\"".format(heroine[0]))
                pressEnterToContinue()

                print("{}의 몸에서 하얀 털이 돋아나고 키가 3m까지 커지며 이빨과 발톱이 자라납니다.".format(heroine[0]))
                print("아무래도 북극곰이라는 별명은 별명이 아닌 진짜였나 봅니다.")
                pressEnterToContinue()

                print("{}: 하하 X발".format(playerName))
                pressEnterToContinue()

                print("-"*40)
                print()
                print("\t\tYou Died")
                print()
                print("-"*40)
                pressEnterToContinue()

        elif characterSelect == 2:
            print("{}: 그래 오늘은 {}이나 만나러 가자.".format(playerName, heroine[1]))
            pressEnterToContinue()

            print("예상했던대로 {}은 생활관에 누워 넷플릭스를 시청하고 있었습니다.\n커튼이 쳐져있고 불이 꺼져있어 생활관이 어둡습니다.".format(heroine[1]))
            pressEnterToContinue()

            print("예상했던대로 {}은 생활관에 누워 넷플릭스를 시청하고 있었습니다.\n커튼이 쳐져있고 불이 꺼져있어 생활관이 어둡습니다.".format(heroine[1]))
            pressEnterToContinue()

            print("무슨 말을 하시겠습니까?")
            print()
            print("1. 뭐 보고있어?")
            print("2. (불을 켜며) 빛이 당신을 태울 것입니다!")
            print("3. 어둠의 자식이냐? 왜 이렇게 어둡게 하고있어")
            print()
            conversationSelect = int(input("입력: "))
            clearWithTime()

            if conversationSelect == 1:
                print("{}: 드라마 보고있어.".format(heroine[1]))
                pressEnterToContinue()

                print("{}: 무슨 드라마 보는데?".format(playerName))
                pressEnterToContinue()

                print("{}: 나의 해방일지라고 이번에 나온건데 재밌더라".format(heroine[1]))
                pressEnterToContinue()

            elif conversationSelect == 2:
                change_relationship_point("-")

                print("{}: 키에에에에에엑!!!!".format(heroine[1]))
                pressEnterToContinue()

                print("{}: ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 이 집 리액션 맛있네".format(playerName))
                pressEnterToContinue()

                print("{}: 아 눈뽕 뭔데 ㅡㅡ".format(heroine[1]))
                pressEnterToContinue()

                print("{}: 군인이라면 섬광탄에 대한 면역을 기르기 위해 이런 훈련이 필요하다고 생각해.".format(playerName))
                pressEnterToContinue()

                print("{}: 지랄하고 자빠졌네.".format(heroine[1]))
                pressEnterToContinue()

            elif conversationSelect == 3:
                change_relationship_point("+")

                print("{}: 아 신경 끄셔 ㅡㅡ 별걸로 참견이야".format(heroine[1]))
                pressEnterToContinue()

                print("{}: 사람이 좀 밝은곳에서 생활하고 그래야지".format(playerName))
                pressEnterToContinue()

                print("{}: ?? 너도 맨날 불꺼놓고 어둡게 해놓잖아".format(heroine[1]))
                pressEnterToContinue()

                print("{}: 나는 나고 너는 너지 어떻게 같겠니?".format(playerName))
                pressEnterToContinue()

                print("{}: 내로남불 지리네 가끔 보면 넌 진짜 미친놈인 것 같아.".format(heroine[1]))
                pressEnterToContinue()

                print("{}: 그게 내 매력이 아닐까-☆".format(playerName))
                pressEnterToContinue()

                print("{}: 에휴 말을 말아야지".format(heroine[1]))
                pressEnterToContinue()

            print("{}: 근데 평소에 근무 없으면 게임방에 박혀 살더니 어쩐 일로 말을 걸었대?".format(heroine[1]))
            pressEnterToContinue()

            print("{}: 그냥~ 이제 게임방도 질려서 사람들이랑 얘기 나누는 낙에 사는거지 뭐..".format(playerName))
            pressEnterToContinue()

        elif characterSelect == 3:
            print("아직 구현되지 않은 기능입니다.")
            break

    elif gameStart == 2:
        print("게임을 종료합니다.")
        break
    else:
        print("잘못입력하셨습니다.")



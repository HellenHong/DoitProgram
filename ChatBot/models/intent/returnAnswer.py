import json

class returnAnswer:

    filepath = r"D:\school\team_project\chatBot\chatbotEngine\models\intent\chatbotAnswer.json"   # 답변 json 파일이 저장될 위치




    def strToJSON(i):   #string을 지정 경로에 json 파일로 저장
        answer = ""
        answer = str(i)
        data = {}
        data['posts'] = []
        data['posts'].append({
            "answer" : answer
        })
        with open(returnAnswer.filepath, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile,ensure_ascii=False)
        print("json 파일 생성 완료")


    def makeA(i):
        answer = ""
        int(i)
        if (i == 0):
            answer = "안녕하세요, 화연봇이에요. 묻고 싶은 것을 알려주세요."
        elif (i == 1):
                answer = "그런 말은 하면 안 돼요. 묻고 싶은 것을 알려주세요."
        elif (i == 2):
                answer = "강의를 추가하려면 일정표 우측 하단의 아이콘을 클릭하고, 강의 추가 아이콘을 클릭해주세요."
        elif (i == 3):
                answer = "강의를 삭제하려면 강의명을 길게 누른 후 삭제 선택지를 클릭해주세요."
        elif (i == 4):
                answer = "네, 그렇군요. 그 외에 묻고싶은 건 없으신가요?"
        elif (i == 5):
                answer = "학교 공지사항 url : http://www.ewha.ac.kr/ewha/news/notice.do"
        else :
                answer = "예기치 못한 오류가 발생했습니다. 다시 시도해주세요."

        return answer

    def returnA(i):
        answer = ""
        answer = returnAnswer.makeA(i)
        returnAnswer.strToJSON(answer)
        return answer

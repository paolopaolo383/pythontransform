import requests
import json
from kakaotrans import Translator
translator = Translator()


url = "https://dapi.kakao.com/v3/translation/language/detect"
for i in range(len(material_list)) :
    queryString = {
        "query" : material_list[i]
    }
    header = {"Authorization": "KakaoAK kkkkkkkkkkkkkkkkkkkk"}
    r = requests.get(url, headers=header, params=queryString)

  # resoponse 딕셔너리로 변환
    r_dic= r.json()

  # 딕셔너리에 있는 "language_info" 값 추출
    language_info = r_dic["language_info"]

  # language_info의 첫번째 결과 추출
    language_info_first = language_info[0]

  # "code" 값 추출
    lan_list.append(language_info_first["code"])
for i in range(len(material_list)) :
    material_result_list.append(translator.translate(material_list[i], src=lan_list[i], tgt='de'))
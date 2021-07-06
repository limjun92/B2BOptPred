import sys
import os
import pickle
import pandas as pd
import warnings
import numpy as np

warnings.simplefilter("ignore")
class NewScaler:
    # 평균, 표준편차 생성
    def __init__(self):
        self.mean_num = None
        self.std_num = None

    # 입력받은 배열로 평균, 표준편차 구하기
    def fit(self, arr):
        if arr is None:
            print("fit() missing 1 required positional argument: 'X'")

        total = 0
        n = 0

        
        #type이 numpy.int32 인데 이걸 숫자로 바꿔야함.
        #print(type(maxnum))
        
        for it in range(arr.size):
            num = arr.iat[it, 0]
            if num != 0 :
                total += num
                n += 1
        
        self.mean_num = total / n
        self.std_num = np.std(arr)

    # fit된 모델로 arr을 scale 적용
    def transform(self, arr):
        if arr is None:
            print("fit() missing 1 required positional argument: 'X'")

        return (arr - self.mean_num) / self.std_num      

    # fit + transform
    def fit_transform(self, arr):
        if arr is None:
            print("fit() missing 1 required positional argument: 'X'")

        total = 0
        n = 0
        
        for it in range(arr.size):
            num = arr.iat[it, 0]
            if num != 0 :
                total += num
                n += 1
        
        self.mean_num = total / n
        self.std_num = np.std(arr)

        return (arr - self.mean_num) / self.std_num  

def get_result(v1,v2,v3,v4,v5,v6,v7):
    warnings.simplefilter("ignore")
    os.chdir('C:\oppty')

    s1 = pickle.load(open('scaler1.sav', 'rb'))
    s2 = pickle.load(open('scaler2.sav', 'rb'))
    cf = pickle.load(open('Model1.sav', 'rb'))

    sample_test = pd.DataFrame({
        'BEF_1M_SLNG_AMT'   : 0,
        'CIRCUIT_NUM'       : 0,
        'INVST_STG_CD' : 0,
        'X_OPTY_TYPE' : 0,
        '1차산업' : 0,
        'IT서비스' : 0,
        'Other' : 0,
        'VAN' : 0,
        '가구/목재품' : 0,
        '가전' : 0,
        '가정용품' : 0,
        '개발원' : 0,
        '건물임대' : 0,
        '건설' : 0,
        '건축/공사자재' : 0,
        '게임' : 0,
        '경영컨설팅' : 0,
        '고무/플라스틱' : 0,
        '고용노동부' : 0,
        '골프연습장' : 0,
        '골프장' : 0,
        '공공' : 0,
        '공단' : 0,
        '공연/전시' : 0,
        '관광' : 0,
        '광고' : 0,
        '교육' : 0,
        '교정기관' : 0,
        '교통' : 0,
        '구단운영' : 0,
        '국방' : 0,
        '금속' : 0,
        '금융' : 0,
        '기계' : 0,
        '기술원' : 0,
        '기타' : 0,
        '기타렌탈' : 0,
        '기타오락' : 0,
        '내장공사' : 0,
        '농업' : 0,
        '단체' : 0,
        '대사관/영사관' : 0,
        '도금/도장' : 0,
        '도로/관련시설' : 0,
        '도서관' : 0,
        '도소매및소비자용품수리업' : 0,
        '레저/여행' : 0,
        '리서치' : 0,
        '무역' : 0,
        '문화재단/센터/회관' : 0,
        '물류' : 0,
        '반도체' : 0,
        '방송' : 0,
        '법률' : 0,
        '병원' : 0,
        '보안/경비/경호' : 0,
        '보험' : 0,
        '부동산' : 0,
        '부동산관리' : 0,
        '부동산중개' : 0,
        '사회/복지' : 0,
        '산업용제품' : 0,
        '산학협력단' : 0,
        '상/하수도사업소' : 0,
        '상공회의소' : 0,
        '생활관/기숙사' : 0,
        '서비스' : 0,
        '선거관리위원회' : 0,
        '설계/감리' : 0,
        '섬유직물' : 0,
        '소방서' : 0,
        '손해사정' : 0,
        '수련관' : 0,
        '수리/정비' : 0,
        '수산물' : 0,
        '수협' : 0,
        '숙박' : 0,
        '스키장' : 0,
        '스포츠' : 0,
        '시설물축조공사' : 0,
        '시설유지관리' : 0,
        '시험/검사/분석' : 0,
        '식품' : 0,
        '신문' : 0,
        '신발/구두' : 0,
        '신용정보' : 0,
        '액정디스플레이' : 0,
        '에너지' : 0,
        '엔지니어링' : 0,
        '연구' : 0,
        '연수원' : 0,
        '연합회' : 0,
        '온라인정보제공' : 0,
        '운송' : 0,
        '위원회' : 0,
        '유리/도자기' : 0,
        '유원지/테마파크' : 0,
        '유치원' : 0,
        '은행' : 0,
        '음식점' : 0,
        '의료' : 0,
        '의류' : 0,
        '인력공급' : 0,
        '인쇄' : 0,
        '임대서비스' : 0,
        '자동차' : 0,
        '자료처리업' : 0,
        '잡화' : 0,
        '장례' : 0,
        '전기' : 0,
        '전산/사무기기유지보수' : 0,
        '전자상거래' : 0,
        '정보처리/데이터' : 0,
        '제조' : 0,
        '조명장치' : 0,
        '조합' : 0,
        '종교' : 0,
        '종이류' : 0,
        '주방/욕실용품도매' : 0,
        '주유소/가스충전소' : 0,
        '중개업' : 0,
        '지자체' : 0,
        '진흥원' : 0,
        '창고/보관' : 0,
        '철근콘크리트' : 0,
        '철도' : 0,
        '체육회' : 0,
        '축산' : 0,
        '축협' : 0,
        '출판' : 0,
        '콜센터' : 0,
        '터미널' : 0,
        '통신' : 0,
        '투자' : 0,
        '판매' : 0,
        '프랜차이즈' : 0,
        '학교' : 0,
        '항공' : 0,
        '행정' : 0,
        '협동조합' : 0,
        '협회' : 0,
        '화장품' : 0,
        '화학' : 0,
        '환경' : 0,
        '회로기판' : 0,
        '201' : 0,
        '402' : 0,
        '404' : 0,
        '701' : 0,
        '901' : 0,
        'G01' : 0,
        '10월' : 0,
        '11월' : 0,
        '12월' : 0,
        '1월' : 0,
        '2월' : 0,
        '3월' : 0,
        '4월' : 0,
        '5월' : 0,
        '6월' : 0,
        '7월' : 0,
        '8월' : 0,
        '9월' : 0,
    }, index=[0])

    sample_test['BEF_1M_SLNG_AMT'][0] = int(v1)
    sample_test['CIRCUIT_NUM'][0] = int(v2)
    sample_test['INVST_STG_CD'][0] = int(v3)
    sample_test['X_OPTY_TYPE'][0] = int(v4)
    sample_test[v5][0] = 1
    sample_test[v6][0] = 1
    sample_test[v7][0] = 1

    scaled_data = pd.concat([s1.transform(sample_test.iloc[:, [0]]),
                        s2.transform(sample_test.iloc[:, [1]])],
                        axis=1)
    scaled_data = pd.concat([sample_test.iloc[:, 2:], scaled_data], axis=1)
    
    print(cf.predict_proba(scaled_data)[0][1])

def main(argv):
    get_result(argv[1],argv[2],argv[3],argv[4],argv[5],argv[6],argv[7])

if __name__ == "__main__":
    main(sys.argv)
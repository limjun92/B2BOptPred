import numpy as np
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
import warnings

# warning 무시
warnings.simplefilter("ignore")



# scaler, model 읽기
scaler1 = pickle.load(open('OPTPred_Scaler1.sav', 'rb'))
scaler2 = pickle.load(open('OPTPred_Scaler2.sav', 'rb'))
classifier1 = pickle.load(open('OPTPred_Model1.sav', 'rb'))
classifier2 = pickle.load(open('OPTPred_Model2.sav', 'rb'))

# test data input
sample_test = pd.DataFrame({
    'INVST_STG_CD'          : 1, 
    'X_OPTY_TYPE'           : 1, 
    'BEF_1M_SLNG_AMT'       : 816574,
    'CIRCUIT_NUM'           : 39, 
    'X_TEXT_1차산업'        : 0, 
    'X_TEXT_IT서비스'       : 0, 
    'X_TEXT_Other'          : 0,
    'X_TEXT_VAN'            : 0, 
    'X_TEXT_가구/목재품'    : 0, 
    'X_TEXT_가전'           : 0, 
    'X_TEXT_가정용품'       : 0, 
    'X_TEXT_개발원'         : 0, 
    'X_TEXT_건물임대'       : 0, 
    'X_TEXT_건설'           : 0, 
    'X_TEXT_건축/공사자재'  : 0, 
    'X_TEXT_게임'           : 0, 
    'X_TEXT_경영컨설팅'     : 0, 
    'X_TEXT_고무/플라스틱'  : 0, 
    'X_TEXT_고용노동부'     : 0, 
    'X_TEXT_골프연습장'     : 0, 
    'X_TEXT_골프'           : 0, 
    'X_TEXT_공공'           : 0, 
    'X_TEXT_공단'           : 0, 
    'X_TEXT_공연/전시'      : 0, 
    'X_TEXT_관광'           : 0, 
    'X_TEXT_광고'           : 0, 
    'X_TEXT_교육'           : 0, 
    'X_TEXT_교정기관'       : 0, 
    'X_TEXT_교통'           : 0, 
    'X_TEXT_구단운영'       : 0, 
    'X_TEXT_국방'           : 0, 
    'X_TEXT_금속'           : 0, 
    'X_TEXT_금융'           : 0, 
    'X_TEXT_기계'           : 0, 
    'X_TEXT_기술원'         : 0, 
    'X_TEXT_기타'           : 0, 
    'X_TEXT_기타렌탈'       : 0, 
    'X_TEXT_기타오락'       : 0, 
    'X_TEXT_내장공사'       : 0, 
    'X_TEXT_농업'           : 0, 
    'X_TEXT_단체'           : 0, 
    'X_TEXT_대사관/영사관'  : 0, 
    'X_TEXT_도금/도장'      : 0, 
    'X_TEXT_도서관'         : 0, 
    'X_TEXT_도소매및소비자용품수리업' : 0, 
    'X_TEXT_리서치'         : 0, 
    'X_TEXT_무역'           : 0, 
    'X_TEXT_문화재단/센터/회관' : 0, 
    'X_TEXT_물류'           : 0, 
    'X_TEXT_반도체'         : 0, 
    'X_TEXT_방송'           : 0, 
    'X_TEXT_법률'           : 0, 
    'X_TEXT_병원'           : 0, 
    'X_TEXT_보안/경비/경호' : 0, 
    'X_TEXT_보험'           : 0, 
    'X_TEXT_부동산'         : 0, 
    'X_TEXT_부동산관리'     : 0, 
    'X_TEXT_부동산중개'     : 0, 
    'X_TEXT_사회/복지'      : 0, 
    'X_TEXT_산업용제품'     : 0, 
    'X_TEXT_산학협력단'     : 0, 
    'X_TEXT_상/하수도사업소': 0, 
    'X_TEXT_상공회의소'     : 0, 
    'X_TEXT_생활관/기숙사'  : 0, 
    'X_TEXT_서비스'         : 0, 
    'X_TEXT_선거관리위원회' : 0,
    'X_TEXT_설계/감리'      : 0,     
    'X_TEXT_섬유직물'       : 0,
    'X_TEXT_소방서'         : 0, 
    'X_TEXT_손해사정'       : 0, 
    'X_TEXT_수련관'         : 0, 
    'X_TEXT_수리/정비'      : 0, 
    'X_TEXT_수산물'         : 0, 
    'X_TEXT_수협'           : 0, 
    'X_TEXT_숙박'           : 0, 
    'X_TEXT_스키장'         : 0, 
    'X_TEXT_스포츠'         : 0, 
    'X_TEXT_시설물축조공사' : 0, 
    'X_TEXT_시설유지관리'   : 0, 
    'X_TEXT_시험/검사/분석' : 0, 
    'X_TEXT_식품'           : 0, 
    'X_TEXT_신문'           : 0, 
    'X_TEXT_신발/구두'      : 0, 
    'X_TEXT_신용정보'       : 0, 
    'X_TEXT_액정디스플레이' : 0, 
    'X_TEXT_에너지'         : 0, 
    'X_TEXT_엔지니어링'     : 0, 
    'X_TEXT_연구'           : 0, 
    'X_TEXT_연수원'         : 0, 
    'X_TEXT_연합회'         : 0, 
    'X_TEXT_온라인정보제공' : 0, 
    'X_TEXT_운송'           : 0, 
    'X_TEXT_위원회'         : 0, 
    'X_TEXT_유리/도자기'    : 0, 
    'X_TEXT_유원지/테마파크': 0, 
    'X_TEXT_유치원'         : 0, 
    'X_TEXT_은행'           : 0, 
    'X_TEXT_음식점'         : 0, 
    'X_TEXT_의료'           : 0, 
    'X_TEXT_의류'           : 0, 
    'X_TEXT_인력공급'       : 0, 
    'X_TEXT_인쇄'           : 0, 
    'X_TEXT_임대서비스'     : 0, 
    'X_TEXT_자동차'         : 0, 
    'X_TEXT_자료처리업'     : 0, 
    'X_TEXT_잡화'           : 0, 
    'X_TEXT_장례'           : 0, 
    'X_TEXT_전기'           : 0, 
    'X_TEXT_전산/사무기기유지보수'  : 0, 
    'X_TEXT_전자상거래'     : 0, 
    'X_TEXT_정보처리/데이터': 0, 
    'X_TEXT_제조'           : 1, 
    'X_TEXT_조명장치'       : 0, 
    'X_TEXT_조합'           : 0, 
    'X_TEXT_종교'           : 0, 
    'X_TEXT_종이류'         : 0, 
    'X_TEXT_주방/욕실용품도매'  : 0, 
    'X_TEXT_주유소/가스충전소'  : 0, 
    'X_TEXT_중개업'         : 0, 
    'X_TEXT_지자체'         : 0, 
    'X_TEXT_진흥원'         : 0, 
    'X_TEXT_창고/보관'      : 0, 
    'X_TEXT_철근콘크리트'   : 0, 
    'X_TEXT_철도'           : 0, 
    'X_TEXT_체육회'         : 0, 
    'X_TEXT_축산'           : 0, 
    'X_TEXT_축협'           : 0, 
    'X_TEXT_출판'           : 0, 
    'X_TEXT_콜센터'         : 0, 
    'X_TEXT_터미널'         : 0, 
    'X_TEXT_통신'           : 0, 
    'X_TEXT_투자'           : 0, 
    'X_TEXT_판매'           : 0, 
    'X_TEXT_프랜차이즈'     : 0, 
    'X_TEXT_학교'           : 0, 
    'X_TEXT_항공'           : 0, 
    'X_TEXT_행정'           : 0, 
    'X_TEXT_협동조합'       : 0, 
    'X_TEXT_협회'           : 0, 
    'X_TEXT_화장품'         : 0, 
    'X_TEXT_화학'           : 0, 
    'X_TEXT_환경'           : 0, 
    'X_TEXT_회로기판'       : 0, 
    'MARKET_CLASS_CD_201'   : 0, 
    'MARKET_CLASS_CD_402'   : 0, 
    'MARKET_CLASS_CD_404'   : 0, 
    'MARKET_CLASS_CD_701'   : 1, 
    'MARKET_CLASS_CD_901'   : 0, 
    'MARKET_CLASS_CD_G01'   : 0, 
    'MONTH_10월'            : 0, 
    'MONTH_11월'            : 0, 
    'MONTH_12월'            : 1, 
    'MONTH_1월'             : 0, 
    'MONTH_2월'             : 0, 
    'MONTH_3월'             : 0, 
    'MONTH_4월'             : 0, 
    'MONTH_5월'             : 0, 
    'MONTH_6월'             : 0, 
    'MONTH_7월'             : 0, 
    'MONTH_8월'             : 0, 
    'MONTH_9월'             : 0
}, index=[0])

# 신규 고객
if sample_test.at[0, 'BEF_1M_SLNG_AMT'] == 0 :
    print('고객 유형 : 신규 고객')
    sample_test.drop(['BEF_1M_SLNG_AMT', 'CIRCUIT_NUM'], axis = 1, inplace = True)
    pred = classifier2.predict_proba(sample_test)

# 기존 고객
else :
    print('고객 유형 : 기존 고객')
    scaled_sample = pd.concat([
        scaler1.transform(sample_test.iloc[:, [2]]),
        scaler2.transform(sample_test.iloc[:, [3]])
    ], axis = 1)

    scaled_sample = pd.concat([sample_test.iloc[:, [0,1]], scaled_sample], axis = 1)
    scaled_sample = pd.concat([scaled_sample, sample_test.iloc[:, 4:]], axis = 1)

    pred = classifier1.predict_proba(scaled_sample)

# 결과 출력
print('성공 확률 : ' + str(round((pred[0][1]*100), 2)))
print('실패 확률 : ' + str(round((pred[0][0]*100), 2)))
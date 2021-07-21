
# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
#Scaler
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

# In[1]:


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter("ignore")
os.chdir('C:\oppty')
df = pd.read_csv('oppty.csv', encoding='cp949')
df.head(5)

# In[5]:

# Win loss를 남기고 삭제
mask = df['X_STATUS_CD'].isin(['Open','Drop','Proposal Reject','Wrong','VDC'])
df = df[~mask]

df['X_STATUS_CD'] = df['X_STATUS_CD'].apply(lambda x:  1 if x=='Win' else 0)
df['INVST_STG_CD'] = df['INVST_STG_CD'].apply(lambda x:  1 if x=='A' else 0)
df['X_OPTY_TYPE'] = df['X_OPTY_TYPE'].apply(lambda x:  1 if x=='A' else 0)

df['X_STATUS_CD'].value_counts()

# In[5]:
print(df['X_TEXT'].unique())
print(df['X_TEXT'].unique().size)
print('==============================================')

df['X_TEXT'] = df['X_TEXT'].replace(['제조','제조업','건축용목제품제조-기타'],'제조')
df['X_TEXT'] = df['X_TEXT'].replace(['목재/가구','기타제조', '제조', '제조업', '건축용목제품제조-기타'], '제조')
df['X_TEXT'] = df['X_TEXT'].replace(['소프트웨어','시스템통합/구축','컴퓨터','컴퓨터/사무','글로벌(인터넷)','네트워크통합(NI)','웹하드','IT서비스', 'IT', '금융IT서비스', 'IT/R&D', '글로벌(IT)'] , 'IT서비스')
df['X_TEXT'] = df['X_TEXT'].replace(['자동차/부품','자동차','자동차부품','자동차유지보수'], '자동차')
df['X_TEXT'] = df['X_TEXT'].replace(['생활가전','가전제품/부품'],'가전')
df['X_TEXT'] = df['X_TEXT'].replace(['개발공사','토공사','토목','건설/건축자재','건설','건설/토목','건축/건설','건설(1군)','건설(2군)','건설기타','건설자재','건설장비','건설/공사'],'건설')
df['X_TEXT'] = df['X_TEXT'].replace(['공기업','관공서/정부기관','관리사무소','관리사업소','교통공사','구축물해체공사','국세청/세무서','국토관리사무소','군청','도시개발공사','도시공사','도시군구청','도시철도공사',
'도청','면사무소','소방시설공사','한국공항공사','한국도로공사','한국전력공사','한국토지공사','항만공사','산림청','시청','우체국','통계청','검찰청','경찰청/경찰서','구청','국가기관','국립기관','기상청','기타공기업',
'기타관공서','병무청','해양수산청','공공','금융공공','기타공공기관','공공관리소','공공기관사무소'], '공공')
df['X_TEXT'] = df['X_TEXT'].replace(['협회/단체/공단','공사/공단','공단','시설관리공단','도시관리공단','도로교통공단','한국산업인력관리공단','환경공단'],'공단')
df['X_TEXT'] = df['X_TEXT'].replace(['여행/관광','관광개발공사','관광공사'],'관광')
df['X_TEXT'] = df['X_TEXT'].replace(['학원','일반학원','교육서비스','인터넷 교육','교육','직업교육','유아교육','기타교육','사회교육','교육청','교육정보원'],'교육')
df['X_TEXT'] = df['X_TEXT'].replace(['시계/귀금속','제철/제련/금속처리','금속/광물','금속','귀금속/장신구','비금속광물','금속광물'],'금속')
df['X_TEXT'] = df['X_TEXT'].replace(['기계','기계/장비','기계장치유지보수','기계 및 장비','기계장비설치','차량/기계'],'기계')
df['X_TEXT'] = df['X_TEXT'].replace(['투자','증권/투자','금융/투자'],'투자')
df['X_TEXT'] = df['X_TEXT'].replace(['식품/음료/주류','식품가공','사료/조제식품','소비재_식음료'],'식품')
df['X_TEXT'] = df['X_TEXT'].replace(['비료/농약','농업','농/축/수/임/광업','농협','농촌지도소','농업기술센터','한국농어촌공사'],'농업')
df['X_TEXT'] = df['X_TEXT'].replace(['방송/측정장비','방송/통신/신문','방송관련','방송','언론/방송'],'방송')
df['X_TEXT'] = df['X_TEXT'].replace(['초중고','대학교','고등학교','학교','기타학교','초등학교','중학교'],'학교')
df['X_TEXT'] = df['X_TEXT'].replace(['케이블','전기장비유지보수','전기','전기공사','전기/전자','전기/정보통신','전기용품','전자'],'전기')
df['X_TEXT'] = df['X_TEXT'].replace(['스포츠/취미용품','스포츠/레저/문화','스포츠센터','스포츠/레져','오락/문화/스포츠'],'스포츠')
df['X_TEXT'] = df['X_TEXT'].replace(['제약','보건/환경','보건소/센터','의료/과학','의료/건강','의료재단','의료원','의료기관','의료/복지'],'의료')
df['X_TEXT'] = df['X_TEXT'].replace(['카드','새마을금고','자산운용','기타금융','금융/보험','금융','금융조합','금융기타','증권','회계','법무/회계','캐피탈'],'금융')
df['X_TEXT'] = df['X_TEXT'].replace(['마트/백화점/시장','소비재_기타','소비재_패션','소비재_화장품','제조/판매','생활재 판매','가전/사무/의료기기판매','종합판매','자동차관련 판매','통신판매','통신재판매','방문판매','판매업'],'판매')
df['X_TEXT'] = df['X_TEXT'].replace(['음식점','요식업','식자재 급식','구내식당','외식'],'음식점')
df['X_TEXT'] = df['X_TEXT'].replace(['연구/시험','연구소'],'연구')
df['X_TEXT'] = df['X_TEXT'].replace(['통신장비','글로벌(통신)','부가/별정통신','통신','통신공사','기간통신','통신기기','통신장비유지보수'],'통신')
df['X_TEXT'] = df['X_TEXT'].replace(['병원','대학병원','종합병원','일반병원','요양병원','한방병원'],'병원')
df['X_TEXT'] = df['X_TEXT'].replace(['선박/항공/철도','항공운송','항공'],'항공')
df['X_TEXT'] = df['X_TEXT'].replace(['축산업','1차산업','도축업','수산업','어업','임업/목재'],'1차산업')
df['X_TEXT'] = df['X_TEXT'].replace(['문구/잡화','사무/문구','가방/가죽','가방/신발'],'잡화')
df['X_TEXT'] = df['X_TEXT'].replace(['가전제품/부품','생활가전'],'가전')
df['X_TEXT'] = df['X_TEXT'].replace(['택시','대리운전','버스'],'교통')
df['X_TEXT'] = df['X_TEXT'].replace(['국방','군부대'],'국방')
df['X_TEXT'] = df['X_TEXT'].replace(['레저/여행','렌탈','렌트카'],'레저/여행')
df['X_TEXT'] = df['X_TEXT'].replace(['무역','무역/중개업'],'무역')
df['X_TEXT'] = df['X_TEXT'].replace(['법률서비스','법무','법원/등기소','변리','변호'],'법률')
df['X_TEXT'] = df['X_TEXT'].replace(['청소년복지','복지','노인복지','다문화지원','사회복지','아동복지','여성복지','장애인복지'],'사회/복지')
df['X_TEXT'] = df['X_TEXT'].replace(['PC방','가사서비스','미용','미용/건강','기타생활서비스','사업서비스업','서비스','서비스 기타','서비스센터'],'서비스')
df['X_TEXT'] = df['X_TEXT'].replace(['콘도/리조트','펜션','호텔','모텔','숙박','여행/숙박'],'숙박')
df['X_TEXT'] = df['X_TEXT'].replace(['신문','신문/잡지'],'신문')
df['X_TEXT'] = df['X_TEXT'].replace(['택배','운송/물류','운송기타','운송장비','운수/운송/터미널','해상운송'],'운송')
df['X_TEXT'] = df['X_TEXT'].replace(['태양광발전','풍력발전','화력발전','환경/에너지','에너지','에너지기타'],'에너지')
df['X_TEXT'] = df['X_TEXT'].replace(['기독교','불교','종교','천주교','기타종교'],'종교')
df['X_TEXT'] = df['X_TEXT'].replace(['편의점','휴게소'],'편의시설')
df['X_TEXT'] = df['X_TEXT'].replace(['화학','화합물/화학제품'],'화학')
df['X_TEXT'] = df['X_TEXT'].replace(['청소업','폐기물관리','하수처리','환경사업소','환경컨설팅'],'환경')
df['MARKET_CLASS_CD'] = df['MARKET_CLASS_CD'].replace(201,'201')
df['MARKET_CLASS_CD'] = df['MARKET_CLASS_CD'].replace(402,'402')
df['MARKET_CLASS_CD'] = df['MARKET_CLASS_CD'].replace(404,'404')
df['MARKET_CLASS_CD'] = df['MARKET_CLASS_CD'].replace(701,'701')
df['MARKET_CLASS_CD'] = df['MARKET_CLASS_CD'].replace(901,'901')

print(df['X_TEXT'].unique())
print(df['X_TEXT'].unique().size)
print(list(df))
# In[5]:

x_text_count = df['X_TEXT'].value_counts()
x_text_list = x_text_count[x_text_count < 20].index.tolist()
df.loc[df['X_TEXT'].isin(x_text_list), 'X_TEXT'] = 'Other'

# mask = df['X_TEXT'].isin(['Other'])
# df = df[~mask]

# %%

dummie = pd.get_dummies(df['X_TEXT'])
df = df.join(dummie)
dummie = pd.get_dummies(df['MARKET_CLASS_CD'])
df = df.join(dummie)
list(df)

# %%

df.loc[df['CREATED']<=20200131, 'MONTH'] = "1월"
df.loc[(df['CREATED']>20200131) & (df['CREATED']<=20200231), 'MONTH'] = "2월"
df.loc[(df['CREATED']>20200231) & (df['CREATED']<=20200331), 'MONTH'] = "3월"
df.loc[(df['CREATED']>20200331) & (df['CREATED']<=20200431), 'MONTH'] = "4월"
df.loc[(df['CREATED']>20200431) & (df['CREATED']<=20200531), 'MONTH'] = "5월"
df.loc[(df['CREATED']>20200531) & (df['CREATED']<=20200631), 'MONTH'] = "6월"
df.loc[(df['CREATED']>20200631) & (df['CREATED']<=20200731), 'MONTH'] = "7월"
df.loc[(df['CREATED']>20200731) & (df['CREATED']<=20200831), 'MONTH'] = "8월"
df.loc[(df['CREATED']>20200831) & (df['CREATED']<=20200931), 'MONTH'] = "9월"
df.loc[(df['CREATED']>20200931) & (df['CREATED']<=20201031), 'MONTH'] = "10월"
df.loc[(df['CREATED']>20201031) & (df['CREATED']<=20201131), 'MONTH'] = "11월"
df.loc[df['CREATED']>20201131, 'MONTH'] = "12월"
df['MONTH'].value_counts()

# %%

list(df)


# %%

# df.loc[df['CREATED']<=20200331, 'QUARTER'] = '1분기'
# df.loc[(df['CREATED']>20200331) & (df['CREATED']<=20200631), 'QUARTER'] = '2분기'
# df.loc[(df['CREATED']>20200631) & (df['CREATED']<=20200931), 'QUARTER'] = '3분기'
# df.loc[df['CREATED']>20200931, 'QUARTER'] = '4분기'
# df['QUARTER'].value_counts()

# %%
dummie = pd.get_dummies(df['MONTH'])
df = df.join(dummie)

#dummie = pd.get_dummies(df['QUARTER'])
#df = df.join(dummie)


# %%
#데이터 확인 

print(df[['MONTH','X_STATUS_CD']].groupby('MONTH', as_index=False).mean())
#print(df[['QUARTER','X_STATUS_CD']].groupby('QUARTER', as_index=False).mean())
print(df[['X_TEXT','X_STATUS_CD']].groupby('X_TEXT', as_index=False).mean())

# %%
df.drop(['SLNG_AMT','CREATED','PURE_PRFIT_AMT','X_CODE','NAME','CLOSE_DT','SUM_WIN_PROB','MIN_CH_DT','MAX_CH_DT','MARKET_CLASS_CD','X_TEXT'], axis = 1, inplace = True)

print(list(df))
# In[5]:
df.drop(['MONTH'], axis = 1, inplace = True)
df.head()

print(list(df))

# In[5]:
df = df.dropna(axis=0)
df.head()
df



# In[5]:
y = df['X_STATUS_CD']
x = df.drop(['X_STATUS_CD'], axis = 1)
# %%
from sklearn.model_selection import train_test_split



# shuffle = False

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=1004)

print('X_train shape:', X_train.shape)

print('X_test shape:', X_test.shape)

print('y_train shape:', y_train.shape)

print('y_test shape:', y_test.shape)


# In[41]:
X_train

# In[41]:


scaler1 = NewScaler()
scaler1.fit(X_train.iloc[:, [2]])
scaler2 = NewScaler()
scaler2.fit(X_train.iloc[:, [3]])

scaled_X_train = pd.concat([scaler1.transform(X_train.iloc[:,[2]]),
                            scaler2.transform(X_train.iloc[:, [3]])], axis=1)


X_train.drop(columns=['BEF_1M_SLNG_AMT','CIRCUIT_NUM'], inplace=True)
scaled_X_train

# %%

scaled_X_test = pd.concat([scaler1.transform(X_test.iloc[:,[2]]),
                            scaler2.transform(X_test.iloc[:, [3]])], axis=1)


X_test.drop(columns=['BEF_1M_SLNG_AMT','CIRCUIT_NUM'], inplace=True)

scaled_X_test

# In[41]:
X_train = X_train.join(scaled_X_train)
X_test = X_test.join(scaled_X_test)

# In[41]:
X_train.head(3)

# In[29]:

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=500)

classifier.fit(X_train, y_train)

score = classifier.score(X_test, y_test)
print(score)

# In[49]:

plt.rcParams['figure.figsize'] = (20,40)
plt.barh(X_test.columns, classifier.feature_importances_)



# In[49]:

plt.rcParams['figure.figsize'] = (20,40)
plt.barh(X_test.columns, classifier.feature_importances_)


# In[49]:
list(X_test)


# %%

import pickle

pickle.dump(classifier, open('Model1.sav', 'wb'))
pickle.dump(scaler1, open('scaler1.sav', 'wb'))
pickle.dump(scaler2, open('scaler2.sav', 'wb'))

# %%
import pickle
s1 = pickle.load(open('scaler1.sav', 'rb'))
s2 = pickle.load(open('scaler2.sav', 'rb'))
cf = pickle.load(open('Model1.sav', 'rb'))

#%%
plt.rcParams['figure.figsize'] = (20,40)
plt.barh(X_test.columns, cf.feature_importances_)

# %%
list(X_test)


# %%
sample_test = pd.DataFrame({
'BEF_1M_SLNG_AMT'   : 816574,
'CIRCUIT_NUM'       : 40,
'INVST_STG_CD' : 1,
'X_OPTY_TYPE' : 1,
'1차산업' : 1,
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
'201' : 1,
'402' : 0,
'404' : 0,
'701' : 0,
'901' : 0,
'G01' : 0,
'10월' : 0,
'11월' : 0,
'12월' : 0,
'1월' : 1,
'2월' : 0,
'3월' : 0,
'4월' : 0,
'5월' : 0,
'6월' : 0,
'7월' : 0,
'8월' : 0,
'9월' : 0,
    }, index=[0])

# %%
scaled_data = pd.concat([s1.transform(sample_test.iloc[:, [0]]),
                        s2.transform(sample_test.iloc[:, [1]])],
                        axis=1)
# %%
scaled_data = pd.concat([sample_test.iloc[:, 2:], scaled_data], axis=1)

# %%
print(scaled_data)


# %%
print(cf.predict_proba(scaled_data))
# %%
list(scaled_data)
# %%
list(X_train)
# %%
print(classifier.predict_proba(scaled_data))
# %%

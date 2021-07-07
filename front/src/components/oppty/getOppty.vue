<template>
  <div>
      <h1>getOppty</h1>
      <div>관리고객 최근 매출액</div>
      <div><input v-model = 'p_bef1mSlngAmt' type="text"/></div>
      <div>관리고객 회선수</div>
      <div><input v-model = 'p_circuitNum' type="text"/></div>
      <div>투자유형</div>
      <input type="radio" id="one" value="1" v-model='p_invstStgCd'>
      <label for="one">A</label>
      <input type="radio" id="one" value="0" v-model='p_invstStgCd'>
      <label for="one">B</label>
      <!-- <div><input v-model = 'p_invstStgCd' type="text"/></div> -->
      <div>기회유형</div>
      <input type="radio" id="one" value="1" v-model='p_xoptyType'>
      <label for="one">A</label>
      <input type="radio" id="one" value="0" v-model='p_xoptyType'>
      <label for="one">B</label>
      <!-- <div><input v-model = 'p_xoptyType' type="text"/></div> -->
      <!-- <div><input v-model = 'p_xtext' type="text"/>{{p_xtext}}</div> -->
      <div>
        <div>업종분류</div>
      <select v-model='p_xtext'>
        <option disabled value="">Please select t_text</option>
        <option>1차산업</option>
        <option>IT서비스</option>
        <option>Other</option>
        <option>VAN</option>
        <option>가구/목재품</option>
        <option>가전</option>
        <option>가정용품</option>
        <option>개발원</option>
        <option>건물임대</option>
        <option>건설</option>
        <option>건축/공사자재</option>
        <option>게임</option>
        <option>경영컨설팅</option>
        <option>고무/플라스틱</option>
        <option>고용노동부</option>
        <option>골프연습장</option>
        <option>골프장</option>
        <option>공공</option>
        <option>공단</option>
        <option>공연/전시</option>
        <option>관광</option>
        <option>광고</option>
        <option>교육</option>
        <option>교정기관</option>
        <option>교통</option>
        <option>구단운영</option>
        <option>국방</option>
        <option>금속</option>
        <option>금융</option>
        <option>기계</option>
        <option>기술원</option>
        <option>기타</option>
        <option>기타렌탈</option>
        <option>기타오락</option>
        <option>내장공사</option>
        <option>농업</option>
        <option>단체</option>
        <option>대사관/영사관</option>
        <option>도금/도장</option>
        <option>도로/관련시설</option>
        <option>도서관</option>
        <option>도소매및소비자용품수리업</option>
        <option>레저/여행</option>
        <option>리서치</option>
        <option>무역</option>
        <option>문화재단/센터/회관</option>
        <option>물류</option>
        <option>반도체</option>
        <option>방송</option>
        <option>법률</option>
        <option>병원</option>
        <option>보안/경비/경호</option>
        <option>보험</option>
        <option>부동산</option>
        <option>부동산관리</option>
        <option>부동산중개</option>
        <option>사회/복지</option>
        <option>산업용제품</option>
        <option>산학협력단</option>
        <option>상/하수도사업소</option>
        <option>상공회의소</option>
        <option>생활관/기숙사</option>
        <option>서비스</option>
        <option>선거관리위원회</option>
        <option>설계/감리</option>
        <option>섬유직물</option>
        <option>소방서</option>
        <option>손해사정</option>
        <option>수련관</option>
        <option>수리/정비</option>
        <option>수산물</option>
        <option>수협</option>
        <option>숙박</option>
        <option>스키장</option>
        <option>스포츠</option>
        <option>시설물축조공사</option>
        <option>시설유지관리</option>
        <option>시험/검사/분석</option>
        <option>식품</option>
        <option>신문</option>
        <option>신발/구두</option>
        <option>신용정보</option>
        <option>액정디스플레이</option>
        <option>에너지</option>
        <option>엔지니어링</option>
        <option>연구</option>
        <option>연수원</option>
        <option>연합회</option>
        <option>온라인정보제공</option>
        <option>운송</option>
        <option>위원회</option>
        <option>유리/도자기</option>
        <option>유원지/테마파크</option>
        <option>유치원</option>
        <option>은행</option>
        <option>음식점</option>
        <option>의료</option>
        <option>의류</option>
        <option>인력공급</option>
        <option>인쇄</option>
        <option>임대서비스</option>
        <option>자동차</option>
        <option>자료처리업</option>
        <option>잡화</option>
        <option>장례</option>
        <option>전기</option>
        <option>전산/사무기기유지보수</option>
        <option>전자상거래</option>
        <option>정보처리/데이터</option>
        <option>제조</option>
        <option>조명장치</option>
        <option>조합</option>
        <option>종교</option>
        <option>종이류</option>
        <option>주방/욕실용품도매</option>
        <option>주유소/가스충전소</option>
        <option>중개업</option>
        <option>지자체</option>
        <option>진흥원</option>
        <option>창고/보관</option>
        <option>철근콘크리트</option>
        <option>철도</option>
        <option>체육회</option>
        <option>축산</option>
        <option>축협</option>
        <option>출판</option>
        <option>콜센터</option>
        <option>터미널</option>
        <option>통신</option>
        <option>투자</option>
        <option>판매</option>
        <option>프랜차이즈</option>
        <option>학교</option>
        <option>항공</option>
        <option>행정</option>
        <option>협동조합</option>
        <option>협회</option>
        <option>화장품</option>
        <option>화학</option>
        <option>환경</option>
        <option>회로기판</option>
      </select>
      </div>
      <div>고객분류</div>
      <div>
      <select v-model='p_marketClassCd'>
        <option disabled value="">Please select 고객분류</option>
        <option>201</option>
        <option>402</option>
        <option>404</option>
        <option>701</option>
        <option>901</option>
        <option>G01</option>
      </select>
      </div>
      <div>시작 월</div>
      <div>
      <select v-model='p_createMonth'>
        <option disabled value="">Please select p_createMonth</option>
        <option>1월</option>
        <option>2월</option>
        <option>3월</option>
        <option>4월</option>
        <option>5월</option>
        <option>6월</option>
        <option>7월</option>
        <option>8월</option>
        <option>9월</option>
      </select>
      </div>
      <div><button v-on:click = "sendData">제출</button></div>
      <div><h1>수주율 : {{getData}} %</h1></div>
      <div>-------------------------------------------</div>
      <table border = "1">
      <th v-for="(la,index) in label" :key="index" >
              {{la}}
      </th>
      <tr v-for="(oppty, index) in getOppty" :key = "'A' + index">
        <td v-for="(o,index) in oppty" :key="'B'+index" >
            {{o}}
          </td>
      </tr>

      </table>

  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
    data(){
        return {
            p_bef1mSlngAmt: "",
            p_circuitNum: "",
            p_invstStgCd: "",
            p_xoptyType: "",
            p_xtext: "",
            p_marketClassCd: "",
            p_createMonth: "",
            label : ['id','수주율','USER','NEW_OR_OLD','관리고객최근매출액','관리고객 회선수','투자유형','기회유형','업종분류','고객분류','시작월','생성일자']
        }
    },
    computed: {
        ...mapGetters(["getData"]),
        ...mapGetters(["getOppty"]),
    },

    methods:{
        sendData(){
            if(this.p_bef1mSlngAmt == ''|| this.p_circuitNum == '' ||this.p_invstStgCd == ''  || this.p_xoptyType == '' || this.p_xtext == '' || this.p_marketClassCd == '' || this.p_createMonth == ''){
              alert("값을 모두 입력하세요")
              return
            }
            const datas = {
                bef1mSlngAmt: this.p_bef1mSlngAmt,
                circuitNum: this.p_circuitNum,
                invstStgCd: this.p_invstStgCd,
                xoptyType: this.p_xoptyType,
                xtext: this.p_xtext,
                marketClassCd: this.p_marketClassCd,
                createMonth: this.p_createMonth,
            } 
            this.$store.dispatch("loadData", datas);
            this.p_bef1mSlngAmt = "";
            this.p_circuitNum = "";
            this.p_invstStgCd = "";
            this.p_xoptyType = "";
            this.p_xtext = "";
            this.p_marketClassCd = "";
            this.p_createMonth = "";
        }
    },
    watch:{
      getData:function(){
          this.$store.dispatch("loadOpptyList");
      },
    },
}
</script>

<style>

</style>
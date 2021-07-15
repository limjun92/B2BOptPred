<template>
  <div class="row">
    <div class="col-md-12">
      <card>
        <template slot="header">
          <h4 class="card-title">B2B 영업정보</h4>
        </template>
        <div>
          <form method="get" action="/" class="form-horizontal">
            <div class="row">
              <label class="col-sm-2 col-form-label">영업정보ID</label>
              <div class="col-sm-10">
                <base-input v-model="datas.bef1mSlngAmt" placeholder="예측할 정보의 영업정보ID 입력 ex) 1-2435574975">
                  <span slot="helpBlock" class="form-text"
                    >A block of help text that breaks onto a new line.
                  </span>
                </base-input>
              </div>
            </div>

            <div class="row">
              <label class="col-sm-2 col-form-label">영업정보ID</label>
              <div class="col-sm-10">
                <base-input v-model="datas.circuitNum" placeholder="예측할 정보의 영업정보ID 입력 ex) 1-2435574975">
                  <span slot="helpBlock" class="form-text"
                    >A block of help text that breaks onto a new line.
                  </span>
                </base-input>
              </div>
            </div>

            <!-- <div class="row">
              <label class="col-sm-2 col-form-label">Password</label>
              <div class="col-sm-10">
                <base-input type="password" value="password"> </base-input>
              </div>
            </div> -->

            <!-- <div class="row">
              <label class="col-sm-2 col-form-label">Placeholder</label>
              <div class="col-sm-10">
                <base-input placeholder="Placeholder"> </base-input>
              </div>
            </div>

            <div class="row">
              <label class="col-sm-2 col-form-label">Disabled</label>
              <div class="col-sm-10">
                <base-input value="Disabled input here.." disabled>
                </base-input>
              </div>
            </div> -->

            <div class="row">
              <label class="col-sm-2 col-form-label">영업기회 생성일자</label>
              <div class="col-sm-10">
                <base-input>
                  <el-date-picker
                    type="date"
                    placeholder="Date Picker"
                    v-model="datas.createMonth"
                  >
                  </el-date-picker>
                </base-input>
              </div>
            </div>

            <!-- <div class="row">
              <label class="col-sm-2 col-form-label">사용자</label>
              <div class="col-sm-10">
                <base-input>
                  <p class="form-control-static">USERID</p>
                </base-input>
              </div>
            </div>

            <div class="row">
              <label class="col-sm-2 col-form-label">고객명</label>
              <div class="col-sm-10">
                <base-input v-model="accntName"> </base-input>
              </div>
            </div> -->
            <div class="row">
              <label class="col-sm-2 col-form-label">투자유형</label>
              <div class="col-sm-10">
                <base-radio name="1" v-model="datas.invstStgCd" inline>A</base-radio>
                <base-radio name="0" v-model="datas.invstStgCd" inline>B</base-radio>
              </div>
            </div>

            <div class="row">
              <label class="col-sm-2 col-form-label">기회유형</label>
              <div class="col-sm-10">
                <base-radio name="1" v-model="datas.optyType" inline>A</base-radio>
                <base-radio name="0" v-model="datas.optyType" inline>B</base-radio>
              </div>
            </div>
            <div class="row">
              <label class="col-sm-2 col-form-label"
                >업종 분류</label
              >
              <div class="col-sm-10 checkbox-radios">

                <base-radio name="1차산업" v-model="datas.text" inline> 1차산업 </base-radio>
                <base-radio name="가전" v-model="datas.text" inline> 가전 </base-radio>
                <base-radio name="건설" v-model="datas.text" inline> 건설 </base-radio>
                <base-radio name="공공" v-model="datas.text" inline> 공공 </base-radio>
                <base-radio name="공단" v-model="datas.text" inline> 공단 </base-radio>
                <base-radio name="관광" v-model="datas.text" inline> 관광 </base-radio>
                <base-radio name="교육" v-model="datas.text" inline> 교육 </base-radio>
                <base-radio name="교통" v-model="datas.text" inline> 교통 </base-radio>
                <base-radio name="국방" v-model="datas.text" inline> 국방 </base-radio>
                <base-radio name="금속" v-model="datas.text" inline> 금속 </base-radio>
                <br>
                <base-radio name="금융" v-model="datas.text" inline> 금융 </base-radio>
                <base-radio name="기계" v-model="datas.text" inline> 기계 </base-radio>
                <base-radio name="농업" v-model="datas.text" inline> 농업 </base-radio>
                <base-radio name="레저/여행" v-model="datas.text" inline> 레저/여행 </base-radio>
                <base-radio name="무역" v-model="datas.text" inline> 무역 </base-radio>
                <base-radio name="방송" v-model="datas.text" inline> 방송 </base-radio>
                <base-radio name="법률" v-model="datas.text" inline> 법률 </base-radio>
                <base-radio name="병원" v-model="datas.text" inline> 병원 </base-radio>
                <base-radio name="부동산" v-model="datas.text" inline> 부동산 </base-radio>
                <base-radio name="기타" v-model="datas.text" inline> 기타 </base-radio>

              </div>
            </div>

            <div class="row">
              <label class="col-sm-2 col-form-label" >고객 분류</label>
              <div class="col-sm-10 checkbox-radios">
                <base-radio name="201" v-model="datas.marketClassCd" inline> 201 </base-radio>
                <base-radio name="402" v-model="datas.marketClassCd" inline> 402 </base-radio>
                <base-radio name="404" v-model="datas.marketClassCd" inline> 404 </base-radio>
                <base-radio name="701" v-model="datas.marketClassCd" inline> 701 </base-radio>
                <base-radio name="901" v-model="datas.marketClassCd" inline> 901 </base-radio>
                <base-radio name="G01" v-model="datas.marketClassCd" inline> G01 </base-radio>
              </div>
            </div>
            {{datas}}
            <!-- <div class="row">
              <label class="col-sm-2 col-form-label">최근 매출액</label>
              <div class="col-sm-10">
                <base-input
                  name="bef1mSlngAmt"
                  v-validate="modelValidations.number"
                  v-model="bef1mSlngAmt"
                  :error="getError('bef1mSlngAmt')"
                >
                </base-input>
              </div>
            </div>
            <div class="row">
              <label class="col-sm-2 col-form-label">회선수</label>
              <div class="col-sm-10">
                <base-input
                  name="circuitNum"
                  v-validate="modelValidations.number"
                  v-model="circuitNum"
                  :error="getError('circuitNum')"
                >
                </base-input>
              </div>
            </div> -->

            
            
          </form>
        </div>
        
      </card>
      <!-- end card -->
    </div>
    <br>
    <div class="col-md-12">
      <div class="text-center">
          <base-button v-on:click = "sendData" type="info">
            Predict!
          </base-button>
      </div>
        <br>
    </div>
    <!-- <div class="col-md-6">
      <card>
        예측확률
      </card>
    </div>
    <div class="col-md-6">
      <card>예측</card>
    </div> -->
    <div class="col-md-12">
        <card class="card-chart card-chart-pie">
          <h5 slot="header" class="card-category">  수주 성공률 예측 결과</h5>

          <div class="row">
            <div class="col-6">
              <div class="chart-area">
                <pie-chart
                  :chart-data="pieChart1.chartData"
                  :extra-options="pieChart1.extraOptions"
                  :height="120"
                >
                </pie-chart>
              </div>
            </div>
            <div class="col-6">
              <h1 class="card-title">
                <i class="tim-icons  icon-trophy text-success "></i> <span>{{getData}}</span>
              </h1>
              <br>
              <h3>SUCCESS!</h3>
              {{this.pieChart1.datasets}}
            </div>
          </div>
        </card>
      </div>
  </div>
</template>
<script>
import { BaseCheckbox, BaseRadio } from 'src/components/index';
import { DatePicker, Select } from 'element-ui';
import PieChart from 'src/components/Charts/PieChart';
import * as chartConfigs from '@/components/Charts/config';
import { mapGetters } from "vuex";

export default {
  components: {
    BaseCheckbox,
    BaseRadio,
    [DatePicker.name]: DatePicker,
    [Select.name]: Select,
    PieChart,
  },
  data() {
    return {
      getresult : 0,
      datas: {
        name:'',
        bef1mSlngAmt: '',
        circuitNum: '',
        createMonth: '',
        invstStgCd: '',
        optyType: '',
        text: '',
        marketClassCd: '',
      },
      radios: {
        radio1: '1',
        radio2: '2',
        radio3: '2',
        radioOn: '2',
        radioOff: '2'
      },
      checkboxes: {
        first: false,
        second: false,
        a: false,
        b: false,
        unchecked: false,
        checked: true,
        disabledUnchecked: false,
        disabledChecked: true
      },
      selects: {
      },
      datePicker: '',
      // model: {
      //   bef1mSlngAmt: this.bef1mSlngAmt,
      //   circuitNum: this.circuitNum,
      //   number: '',
      //   accntName:this.accntName,
      // },
      modelValidations: {
        required: {
          required: true
        },
        number: {
          numeric: true
        }
      },
      pieChart1: {
        chartData: {
          labels: ['success', 'fail'],
          datasets: [
            {
              label: 'Emails',
              pointRadius: 0,
              pointHoverRadius: 0,
              backgroundColor: ['#00c09d', '#e2e2e2'],
              borderWidth: 0,
              data: [100 - this.getData,this.getData]
            }
          ]
        },
        extraOptions: chartConfigs.pieChartOptions
      },
      pieChart2: {
        chartData: {
          labels: [1, 2, 3],
          datasets: [
            {
              label: 'Emails',
              pointRadius: 0,
              pointHoverRadius: 0,
              backgroundColor: ['#ff8779', '#2a84e9', '#e2e2e2'],
              borderWidth: 0,
              data: [60, 40, 20]
            }
          ]
        },
        extraOptions: chartConfigs.pieChartOptions
      }
    };
  },
  computed: {
    ...mapGetters(["getData"]),
  },
  methods: {
    getError(fieldName) {
      return this.errors.first(fieldName);
    },
    sendData(){
      console.log(this.pieChart1.chartData.datasets[0].data[0])
      if(this.datas.bef1mSlngAmt == ''|| this.datas.circuitNum == '' ||this.datas.invstStgCd == ''  || this.datas.optyType == '' || this.datas.text == '' || this.datas.marketClassCd == '' || this.datas.createMonth == ''){
        alert("값을 모두 입력하세요")
        return
      }
      // this.datas.createMonth = "" + this.datas.createMonth;
      // console.log(this.datas.createMonth)
      this.datas.createMonth = this.datas.createMonth.getMonth() + "월"
      
      console.log(this.datas)

      this.$store.dispatch("loadData", this.datas);
    }
  },
    watch:{
      getData:function(){
          this.pieChart1.chartData.datasets[0].data[0] = this.getData;
          this.pieChart1.chartData.datasets[0].data[1] = 100 - this.getData;
      },
    },
};
</script>
<style></style>

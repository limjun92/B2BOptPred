<template>
  <div>
    <h1>fileUploadTest</h1>
      <input type="file" id="files" ref="files" v-on:change="handleFileUpload()" multiple />
      <button v-on:click="submitFile()">제출</button>
      <!-- 데이터 수 -->
      <div>
      총 데이터 수 : {{allDataNum}} || 보이는 데이터 수 : <input v-model="wantDataNum"> <button v-on:click="changeDataNum()">변경</button>
      </div>
      <!-- 번호 -->
      <div>
      <button v-on:click="move(i-1)" v-for="(i,index) in (idx+1)" :key="index">{{i}}</button>
      </div>
      <!-- 테이블 -->
      <div v-if = "tables.length>0">
      {{tables[idx][0].length}}
      <table border = "1">
        <th class ="table_td" v-for="(label,index) in tables[idx][0]" :key="index" >
        {{label}} <button v-on:click="delcolumn(index, true)">del</button>
        </th>
        <tr class ="table_tr" v-for="(data,index) in paginatedData" :key="'A'+index" >
          <td class ="table_td" v-for="(d,index) in data" :key="'B'+index" >
            {{d}}
          </td>
        </tr>
      </table>
      <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
        이전
      </button>
      <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
      
      <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">
        다음
      </button>
      <input v-model="onePageDataNum"  v-on:change="initPageNum()" placeholder="한페이지에 몇개씩">
      </div>
  </div>
</template>

<script>

export default {
  data(){
    return {
      saveRule : [],
      allData : [],
      allDataNum : 0,
      wantDataNum : 100,
      onePageDataNum : 10,
      pageNum : 0,
      idx : 0,
      tables : [],
    };
  },
  computed:{
    pageCount () {
        let listLeng = this.tables[this.idx][1].length,
            listSize = Number(this.onePageDataNum),
            page = Math.floor(listLeng / listSize);
        if (listLeng % listSize > 0) page += 1;
        return page;
      },
      paginatedData () {
      const start = this.pageNum * Number(this.onePageDataNum),
            end = start + Number(this.onePageDataNum);
      return this.tables[this.idx][1].slice(start, end);
    }
  },
  methods: {
    //페이징관련
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    },
    initPageNum(){
      if (this.pageCount <= this.pageNum)
        this.pageNum = this.pageCount -1;
    },
    ////////////////////////////////////////////////////////////////////////////////
    //DB에 데이터 저장(csv back단으로 전달)
    submitFile() {
      for (var i = 0; i < this.files.length; i++) {
          let formData = new FormData();
          formData.append('title', this.title);
          formData.append('files', this.files[i]);
          this.$store.dispatch("loadUpload", formData);
      }
    },
    //csv파일을 화면에 바로 보여주는 함수
    handleFileUpload() {
      this.files = this.$refs.files.files;
      const reader = new FileReader();
      reader.onload = e => {
        this.allData = e.target.result.split("\n");
        this.allDataNum = this.allData.length - 1;

        var labels = this.allData[0].split(",");
        var datas = [];
        for(var i = 1;i<this.wantDataNum + 1;i++){
          datas.push(this.allData[i].split(","));
        }
        this.tables.push([labels, datas])
      };
      reader.readAsText(this.files[0],"euc-kr");
    },
    ///////////////////////////////////////////////////
    //전체데이터중에서 원하는 수의 데이터만 확인히켜주는 함수
    changeDataNum(){
      var labels = this.allData[0].split(",");
      var datas = [];
        for(var i = 1;i<Number(this.wantDataNum) + 1;i++){
          datas.push(this.allData[i].split(","));
        }
      var saveIdx = this.idx;
      this.idx = 0;
      this.tables.length = 0;
      this.tables.push([labels, datas]);
      
      this.initPageNum()

      this.activateRule(saveIdx)
    },
    //원하는 데이터에 적용했던 룰을 다시 적용하는 함수
    activateRule(saveIdx){
      for(var i = 0;i<saveIdx;i++){
        switch(this.saveRule[i][0]){
          case "delColumn":
            this.delcolumn(this.saveRule[i][1], false);
        }
      }
    },
    ///////////////////////////////////////////////////////////
    //수정 함수
    delcolumn(index, flag){
      var tmp_labels = this.tables[this.idx][0].slice();
      tmp_labels.splice(index,1);

      var tmp_datas = this.tables[this.idx][1].slice();
      var save_datas = []
      
      for(var i = 0;i<tmp_datas.length;i++){
        var tmp_tmp_data = tmp_datas[i].slice();
        tmp_tmp_data.splice(index,1)
        save_datas.push(tmp_tmp_data)
      }
      //this.idx++;
      this.tables.push([tmp_labels, save_datas])
      this.idx = this.idx + 1;
      //console.log(tmp_labels)
      // this.tables.push([tmp_labels, tmp_datas])
      //데이터 수를 변경할 경우에는 들어가지 않는다.
      if(flag){
        this.saveRule.push(["delColumn",index])
        // for(var j = 0 ;j<this.saveRule.length;j++){
        //   console.log(this.saveRule[j][0],this.saveRule[j][1]);
        // }
        // console.log('========')
      }
    },
    ////////////////////////////////////////////////////////////
    //이동 함수
    move(index){
      this.idx = index
      this.tables.length = index+1
      this.saveRule.length = index
    }
  }
}
</script>

<style scoped>

table{
  table-layout: fixed;
}

.table_tr{
  height: 20px;
  color: red;
}
.table_td{
  width:100px;
}

</style>
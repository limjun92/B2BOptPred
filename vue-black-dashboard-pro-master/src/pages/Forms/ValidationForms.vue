<template>
  <div class="row">

    <div class="col-md-12">
      <card>
        
        <div class="row">
          <label class="col-sm-2 col-form-label">ID</label>
          <div class="col-sm-10">
            <base-input placeholder="예측할 정보의 영업정보ID 입력 ex) 1-2435574975">
              <span slot="helpBlock" class="form-text"
                >A block of help text that breaks onto a new line.
              </span>
            </base-input>
          </div>
          <div>
          <base-button type="success" class="animation-on-hover">Success</base-button>
              </div>
              
        </div>
      </card>
      
    </div>
    <div class="col-md-12">
        <card>
          <div
              class="col-12 d-flex justify-content-center justify-content-sm-between flex-wrap"
            >
              <el-select
                class="select-primary mb-3 pagination-select"
                v-model="pagination.perPage"
                placeholder="Per page"
              >
                <el-option
                  class="select-primary"
                  v-for="item in pagination.perPageOptions"
                  :key="item"
                  :label="item"
                  :value="item"
                >
                </el-option>
              </el-select>

              <base-input>
                <el-input
                  type="search"
                  class="mb-3 search-input"
                  clearable
                  prefix-icon="el-icon-search"
                  placeholder="Search records"
                  v-model="searchQuery"
                  aria-controls="datatables"
                >
                </el-input>
              </base-input>
            </div>
          <el-table :data="queriedData">
            <el-table-column
              fixed="left"
              label="Operations"
              width="120">
              <template slot-scope="scope">
                <Button
                  v-on:click="deleteRows(scope.$index, tableData)"
                  type="text"
                  size="small">
                  Remove
                </Button>
              </template>
            </el-table-column>
              <el-table-column
                v-for="column in tableColumns"
                :key="column.label"
                :min-width="column.minWidth"
                :prop="column.prop"
                :label="column.label"
              >
              </el-table-column>
            </el-table>
        </card>
      </div>
      <div class="col-md-12">
        <card class="card-chart card-chart-pie">
          <h5 slot="header" class="card-category">  수주 성공률 예측 결과</h5>
          <div class="row">
            <div class="col-6">
              <h1 class="card-title">
                <i class="tim-icons  icon-trophy text-success "></i> <span>{{getData}}</span>
              </h1>
              <br>
              <h3>SUCCESS!</h3>
            </div>
          </div>
        </card>
      </div>
  </div>
</template>
<script>

import { Table, TableColumn, Select, Option } from 'element-ui';
import { BasePagination } from 'src/components';
import Fuse from 'fuse.js';
import swal from 'sweetalert2';
import { mapGetters } from "vuex";

export default {
  components: {
    BasePagination,
    [Select.name]: Select,
    [Option.name]: Option,
    [Table.name]: Table,
    [TableColumn.name]: TableColumn
  },
  data() {
    return {
      click_on : {
        name : ''
      },
      lowerlabel:['name','xstatusCd','sumWinProb' ,'invstStgCd' ,'optyType' , 'marketClassCd',
      'created' , 'closeDt','bef1mSlgnAmt','circuitNum','code','text','slngAmt' ,'purePrfit','minChDt' ,'maxChDt'],
      tables:[],
      pagination: {
        perPage: 5,
        currentPage: 1,
        perPageOptions: [5, 10, 25, 50],
        total: 0
      },
      searchQuery: '',
      tableData: [],
      searchedData: [],
      fuseSearch: null,
      tableColumns: [
        {
          prop: 'name',
          label: 'Name',
          minWidth: 200
        },
        {
          prop: 'xstatusCd',
          label: 'X_STATUS_CD',
          minWidth: 200
        },
        {
          prop: 'sumWinProb',
          label: 'SUM_WIN_PROB',
          minWidth: 200
        },
        {
          prop: 'invstStgCd',
          label: 'INVST_STG_CD',
          minWidth: 200
        },
        {
          prop: 'optyType',
          label: 'X_OPTY_TYPE',
          minWidth: 200
        },
        {
          prop: 'marketClassCd',
          label: 'MARKET_CLASS_CD',
          minWidth: 200
        },
        {
          prop: 'created',
          label: 'CREATED',
          minWidth: 200
        },
        {
          prop: 'closeDt',
          label: 'CLOSE_DT',
          minWidth: 200
        },
        {
          prop: 'bef1mSlgnAmt',
          label: 'BEF_1M_SLNG_AMT',
          minWidth: 200
        },
        {
          prop: 'circuitNum',
          label: 'CIRCUIT_NUM',
          minWidth: 200
        },
        {
          prop: 'code',
          label: 'X_CODE',
          minWidth: 200
        },
        {
          prop: 'text',
          label: 'X_TEXT',
          minWidth: 200
        },
        {
          prop: 'slngAmt',
          label: 'SLNG_AMT',
          minWidth: 200
        },
        {
          prop: 'purePrfit',
          label: 'PURE_PRFIT_AMT',
          minWidth: 200
        },
        {
          prop: 'minChDt',
          label: 'MIN_CH_DT',
          minWidth: 200
        },
        {
          prop: 'maxChDt',
          label: 'MAX_CH_DT',
          minWidth: 200
        },
      ],
    };
  },
    computed: {
    /***
     * Returns a page from the searched data or the whole data. Search is performed in the watch section below
     */
    ...mapGetters(["getAllDate"]),

    queriedData() {
      let result = this.tableData;
      if (this.searchedData.length > 0) {
        result = this.searchedData;
      }
      return result.slice(this.from, this.to);
    },
    to() {
      let highBound = this.from + this.pagination.perPage;
      if (this.total < highBound) {
        highBound = this.total;
      }
      return highBound;
    },
    from() {
      return this.pagination.perPage * (this.pagination.currentPage - 1);
    },
    total() {
      return this.searchedData.length > 0
        ? this.searchedData.length
        : this.tableData.length;
    }
  },
  methods: {
    deleteRows(idx, data){
      console.log(idx)
      console.log(data[idx])
    },
    clickData(){
      console.log("??")
    },
    InsertData(){
      for(var i = 0;i<this.tables.length;i++){
        this.$store.dispatch("insertData", this.tables[i]);
      }
    },
    handleFileUpload() {
      this.files = this.$refs.files.files;
      const reader = new FileReader();
      reader.onload = e => {
        this.allData = e.target.result.split("\n");
        this.allDataNum = this.allData.length - 1;

        //var labels = this.allData[0].split(",");
        //var datas = [];
        for(var i = 1;i<100;i++){
          var obj = {};
          obj['userId'] = '준형'
          var row = this.allData[i].split(",");
          for(let j = 0;j<this.lowerlabel.length;j++){
            obj[this.lowerlabel[j]] = row[j];
          }
          this.tables.push(obj);
        }
        this.tableData = this.tables;
      };
      reader.readAsText(this.files[0],"euc-kr");
    },
    handleLike(index, row) {
      swal({
        title: `You liked ${row.name}`,
        buttonsStyling: false,
        type: 'success',
        confirmButtonClass: 'btn btn-success btn-fill'
      });
    },
    handleEdit(index, row) {
      swal({
        title: `You want to edit ${row.name}`,
        buttonsStyling: false,
        confirmButtonClass: 'btn btn-info btn-fill'
      });
    },
    handleDelete(index, row) {
      swal({
        title: 'Are you sure?',
        text: `You won't be able to revert this!`,
        type: 'warning',
        showCancelButton: true,
        confirmButtonClass: 'btn btn-success btn-fill',
        cancelButtonClass: 'btn btn-danger btn-fill',
        confirmButtonText: 'Yes, delete it!',
        buttonsStyling: false
      }).then(result => {
        if (result.value) {
          this.deleteRow(row);
          swal({
            title: 'Deleted!',
            text: `You deleted ${row.name}`,
            type: 'success',
            confirmButtonClass: 'btn btn-success btn-fill',
            buttonsStyling: false
          });
        }
      });
    },
    deleteRow(row) {
      let indexToDelete = this.tableData.findIndex(
        tableRow => tableRow.id === row.id
      );
      if (indexToDelete >= 0) {
        this.tableData.splice(indexToDelete, 1);
      }
    }
  },
  mounted() {
    // Fuse search initialization.
    this.fuseSearch = new Fuse(this.tableData, {
      keys: ['name', 'email'],
      threshold: 0.3
    });

    this.$store.dispatch("loadAllData");
  },
  watch: {
    /**
     * Searches through the table data by a given query.
     * NOTE: If you have a lot of data, it's recommended to do the search on the Server Side and only display the results here.
     * @param value of the query
     */
    searchQuery(value) {
      let result = this.tableData;
      if (value !== '') {
        result = this.fuseSearch.search(this.searchQuery);
      }
      this.searchedData = result;
    },
    getAllDate(){
      this.tableData = this.getAllDate
    }
  }
};
</script>
<style>
.pagination-select,
.search-input {
  width: 200px;
}</style>

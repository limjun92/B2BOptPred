<template>
  <div class="content">
    <input type="file" id="files" ref="files" v-on:change="handleFileUpload()" multiple />
    <div class="col-md-8 ml-auto mr-auto">
      <h2 class="text-center">Paginated Tables</h2>
      <p class="text-center">
        With a selection of custom components & and Element UI components, you
        can built beautiful data tables. For more info check
        <a
          href="http://element.eleme.io/#/en-US/component/table"
          target="_blank"
          >Element UI Table</a
        >
      </p>
    </div>
    <div class="row mt-5">
      <div class="col-12">
        <card card-body-classes="table-full-width">
          <h4 slot="header" class="card-title">Paginated Tables</h4>
          <div>
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
            <!-- -->
            <el-table :data="queriedData">
              <el-table-column
                v-for="column in tableColumns"
                :key="column.label"
                :min-width="column.minWidth"
                :prop="column.prop"
                :label="column.label"
              >
              </el-table-column>
              <el-table-column :min-width="135" align="right" label="Actions">
                <div slot-scope="props">
                  <base-button
                    @click.native="handleLike(props.$index, props.row)"
                    class="like btn-link"
                    type="info"
                    size="sm"
                    icon
                  >
                    <i class="tim-icons icon-heart-2"></i>
                  </base-button>
                  <base-button
                    @click.native="handleEdit(props.$index, props.row)"
                    class="edit btn-link"
                    type="warning"
                    size="sm"
                    icon
                  >
                    <i class="tim-icons icon-pencil"></i>
                  </base-button>
                  <base-button
                    @click.native="handleDelete(props.$index, props.row)"
                    class="remove btn-link"
                    type="danger"
                    size="sm"
                    icon
                  >
                    <i class="tim-icons icon-simple-remove"></i>
                  </base-button>
                </div>
              </el-table-column>
            </el-table>
          </div>
          <div
            slot="footer"
            class="col-12 d-flex justify-content-center justify-content-sm-between flex-wrap"
          >
            <div class="">
              <p class="card-category">
                Showing {{ from + 1 }} to {{ to }} of {{ total }} entries
              </p>
            </div>
            <base-pagination
              class="pagination-no-border"
              v-model="pagination.currentPage"
              :per-page="pagination.perPage"
              :total="total"
            >
            </base-pagination>
          </div>
        </card>
        <div v-on:click = 'InsertData'>제출</div>
      </div>
    </div>
    </div>
    </template>
<script>
import { Table, TableColumn, Select, Option } from 'element-ui';
import { BasePagination } from 'src/components';
import Fuse from 'fuse.js';
import swal from 'sweetalert2';

export default {
  components: {
    BasePagination,
    [Select.name]: Select,
    [Option.name]: Option,
    [Table.name]: Table,
    [TableColumn.name]: TableColumn
  },
  computed: {
    /***
     * Returns a page from the searched data or the whole data. Search is performed in the watch section below
     */
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
  data() {
    return {
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
      propsToSearch: ['name', 'email', 'age'],
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
      tableData: [],
      searchedData: [],
      fuseSearch: null
    };
  },
  methods: {
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

        var labels = this.allData[0].split(",");
        var datas = [];
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
    }
  }
};
</script>
<style>
.pagination-select,
.search-input {
  width: 200px;
}
</style>

import Vue from 'vue';
import Vuex from "vuex";
import axios from 'axios';
import VueAxios from 'vue-axios';

import userlist from './modules/userlist';
import table from './modules/table';
import useData from './modules/useData';

Vue.use(Vuex);
Vue.use(VueAxios, axios);

export const store = new Vuex.Store({
    modules: {
        userlist,
        table,
        useData,
    },
});
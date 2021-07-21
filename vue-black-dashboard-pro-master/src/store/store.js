import Vue from 'vue';
import Vuex from "vuex";
import axios from 'axios';
import VueAxios from 'vue-axios';

import user from './modules/user';
import oppty from './modules/oppty';
import datas from './modules/datas';


Vue.use(Vuex);
Vue.use(VueAxios, axios);

export const store = new Vuex.Store({
    modules: {
        user,
        oppty,
        datas,
    },
});
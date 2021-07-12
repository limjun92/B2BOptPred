import axios from 'axios';

let api_url = process.env.VUE_APP_APIURL + "/oppty";

const state = {
    data:0,
    allData:[],
}; 

const actions = {
    insertData(context, payload){
        axios.post(`${api_url}/insertData`, payload)
            .then(res => res.data)
            .then(item => (context.commit('setInsertResultData',item)))
            .catch(error => console.error(error));
    },
    loadAllData(context){
        axios.get(`${api_url}/loadAllData`)
            .then(res => res.data)
            .then(item => (context.commit('setLoadAllData',item)))
            .catch(error => console.error(error));
    }
};

const getters = {
    getInsertResultData(state){
        return state.data;
    },
    getAllDate(state){
        return state.allData;
    }
}; //getters

const mutations = {
    setInsertResultData(state, items){
        console.log(items)
        state.data = items;
    },
    setLoadAllData(state, items){
        console.log(items)
        state.allData = items;
    }
};

export default {
    state, actions, getters, mutations
}
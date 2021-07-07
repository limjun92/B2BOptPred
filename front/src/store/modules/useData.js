import axios from 'axios';

let api_url = process.env.VUE_APP_APIURL + "/oppty";

const state = {
    data: '',
    opptyList: [],
}; 

const actions = {
    loadData(context, payload){
        console.log(payload)
        axios.post(`${api_url}/getData`, payload)
            .then(res => res.data)
            .then(item => (context.commit('setData',item)))
            .catch(error => console.error(error));
    },
    loadOpptyList(context){
        axios.get(`${api_url}/getAll`)
            .then(res => res.data)
            .then(items => (context.commit('setOpptyList',items)))
            .catch(error => console.error(error));
    },
};

const getters = {
    getData(state){
        return state.data;
    },
    getOppty(state){
        return state.opptyList;
    }
}; //getters

const mutations = {
    setData(state, items){
        state.data = items;
    },
    setOpptyList(state, items){
        state.opptyList = items;
    }
};

export default {
    state, actions, getters, mutations
}
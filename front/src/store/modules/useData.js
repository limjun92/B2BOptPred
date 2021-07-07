import axios from 'axios';

let api_url = process.env.VUE_APP_APIURL + "/oppty";

const state = {
    data: [],
}; 

const actions = {
    loadData(context, payload){
        console.log(payload)
        axios.post(`${api_url}/getData`, payload)
            .then(res => res.data)
            .then(item => (context.commit('setData',item)))
            .catch(error => console.error(error));
    },
};

const getters = {
    getData(state){
        return state.data;
    },
}; //getters

const mutations = {
    setData(state, items){
        state.data = items;
    },
};

export default {
    state, actions, getters, mutations
}
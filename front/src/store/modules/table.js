import axios from 'axios';

let api_url = process.env.VUE_APP_APIURL + "/file";

const state = {
    label: [],
}; 

const actions = {
    loadUpload(context, payload){
        axios.post(`${api_url}/upload`, payload,{
            headers:{
                'Content-Type': 'multipart/form-data'
            }
        })
        .then(res => res.data)
        .then(items => (context.commit('setUpload',items)))
        .catch(error => console.error(error));
    },
};

const getters = {
    getUpload(state){
        return state.label;
    },
}; //getters

const mutations = {
    setUpload(state, items){
        state.label = items;
    },
};

export default {
    state, actions, getters, mutations
}
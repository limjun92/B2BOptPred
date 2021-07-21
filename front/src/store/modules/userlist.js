import axios from 'axios';

let api_url = process.env.VUE_APP_APIURL + "/getuser";
// api_url = `http://localhost:8888/devpro/ktsports`;
//let api_url = `/getuser`;

const state = {
    userlist: [],
}; 

const actions = {
    loadUserList(context){
        axios.get(`${api_url}/get`)
            .then(res => res.data)
            .then(items => (context.commit('setUserList',items)))
            .catch(error => console.error(error));
    },
};

const getters = {
    getUserList(state){
        return state.userlist;
    },
}; //getters

const mutations = {
    setUserList(state, items){
        state.userlist = items;
    },
};

export default {
    state, actions, getters, mutations
}
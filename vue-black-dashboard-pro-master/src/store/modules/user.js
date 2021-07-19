import axios from 'axios';

let api_url = `http://localhost:8888/devpro/getuser`;

const state = {
    registerCheck : 0,
    regiModal : false,
    loginModal : false,
}; 

const actions = {

    register(context, payload){
        axios.post(`${api_url}/register`, payload)
            .then(res => res.data)
            .then(items => (context.commit('setRegister',items)))
            .catch(error => console.error(error));
    },
};

const getters = {

    getRegisterCheck(state){
        return state.registerCheck;
    },
    getRegiModal(state){
        return state.regiModal;
    },
    getLoginModal(state){
        return state.loginModal;
    }
}; //getters

const mutations = {

    setRegister(state, items){
        state.registerCheck = items;
    },
    openRegiModal(state, items){
        state.regiModal = items;
    },
    openLoginModal(state, items){
        state.loginModal = items;
    }
};

export default {
    state, actions, getters, mutations
}
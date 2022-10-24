import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// 导入 Vuex
const store = new Vuex.Store({
    state: {
        kols: [],
        // kolFavs:[],
        // noteFavs:[],
        notes: [],
        user: {},
        noteDetail: {},
        kolDetail: {}
    },
    mutations: { // 与 state 同步执行；可以改变 state 对应的值的方法
        INIT_KOLS(state, resp) {
            state.kols = resp.data.results
        },
        INIT_KOLFAVS(state, resp) {
            state.kols = resp.data
        },
        INIT_NOTEFAVS(state, resp) {
            state.notes = resp.data
        },
        INIT_NOTES(state, resp) {
            state.notes = resp.data.results
        },
        INIT_USER(state, resp) {
            state.user = resp.data
        },
        INIT_NOTESDETAIL(state, resp) {
            state.noteDetail = resp.data
        },
        INIT_KOLSDETAIL(state, resp) {
            state.kolDetail = resp.data
        }
    },
    // 异步执行
    actions: {
        
    }
})

export default store;

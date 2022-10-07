import Vue from 'vue'
import VueRouter from 'vue-router'
import UserLogin from "@/pages/UserLogin";
import UserInfo from "@/pages/UserInfo";
import UserHome from "@/pages/UserHome";
import UserFav from "@/pages/UserFav";
import KolIndex from "@/pages/KolIndex";
import KolDetail from "@/pages/KolDetail";
import NoteIndex from "@/pages/NoteIndex";
import NoteDetail from "@/pages/NoteDetail";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'UserLogin',
        component:UserLogin ,
    },
    {
        path: '/UserInfo',
        name: 'UserInfo',
        component: UserInfo,
    },
    {
        path: '/UserHome',
        name: 'UserHome',
        component: UserHome,
    },
    {
        path: '/UserFav',
        name: 'UserFav',
        component: UserFav,
    },
    {
        path: '/KolIndex',
        name: 'KolIndex',
        component: KolIndex,
    },
    {
        path: '/KolDetail',
        name: 'KolDetail',
        component: KolDetail,
    },
    {
        path: '/NoteIndex',
        name: 'NoteIndex',
        component: NoteIndex,
    },
    {
        path: '/NoteDetail',
        name: 'NoteDetail',
        component: NoteDetail,
    }

]

const router = new VueRouter({
    routes
})

export default router

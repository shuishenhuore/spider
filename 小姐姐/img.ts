// import axios from "axios";

export const heisiapi = ()=>{
    return axios({
        url:'https://v2.xxapi.cn/api/heisi',
        method:'get',
    })
}

export const baisiapi = ()=>{
    return axios({
        url:'https://v2.xxapi.cn/api/baisi',
        method:'get',
    })
}

export const jkapi = ()=>{
    return axios({
        url:'https://v2.xxapi.cn/api/jk',
        method:'get',
    })
}

export const xiaojiejieapi = ()=>{
    return axios({
        url:'https://v2.xxapi.cn/api/meinvpic',
        method:'get',
    })
}
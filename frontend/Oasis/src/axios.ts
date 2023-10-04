import axios from 'axios'
import { ElLoading } from 'element-plus'


let loading : any;
const startLoading = () =>{
    interface Options  {
        lock: boolean;
        text: string;
        background: string
    };

    const options:Options = {
        lock: true,
        text: 'Loading',
        background: 'rgba(0, 0, 0, 0.7)'
    }
    loading = ElLoading.service(options)
}

const enloading = () =>{
    loading.close()
}



// request interceptor
axios.interceptors.request.use(function(config) {
    // do something before request is sent
    startLoading()
    return config
}, function(error) {
    // do something with request error

    return Promise.reject(error)
}
)




// response interceptor

axios.interceptors.response.use(function(response) {
    // do something with response data
    enloading()
    return response
}
, function(error) {
    // do something with response error
    enloading()
    return Promise.reject(error)
}
)

import axios from 'axios';

import { GET_STORES, DELETE_STORE, ADD_STORE } from './types';

// GET STORES
export const getStores = () => dispatch => {
    axios.get('/api/stores/')
        .then(res => {
            dispatch({
                type: GET_STORES,
                payload: res.data
            });
        })
        .catch(err => console.log(err));
}

// DELETE LEAD
export const deleteStore = (id) => dispatch => {
    axios
        .delete(`/api/stores/${id}/`)
        .then(res => {
            dispatch({
                type: DELETE_STORE,
                payload: id
            });
        })
        .catch(err => console.log(err));
}
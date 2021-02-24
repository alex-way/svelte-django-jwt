import {
    writable,
} from 'svelte/store';

export const loggedOutUser = {
    loggedIn: false,
    username: null,
    name: null
}
export const user = writable(loggedOutUser);

import axios from "axios";
import {
    goto
} from "@sapper/app";
import {
    user,
    loggedOutUser
} from "../stores/auth";
import {
    get
} from 'svelte/store';

const logout_cookie_key = "logout";


const successfulLogin = async (access_token) => {
    console.log("Logged in Successfully");
    axios.defaults.headers.common = {
        "Authorization": `Bearer ${access_token}`
    };
    if (!get(user).loggedIn) {
        await axios.get("/api/profile/").then(response => {
            return response.data;
        }).then(data => {
            user.set({
                loggedIn: true,
                username: data.username,
                name: data.name
            })
        });
    }
    setTimeout(async () => {
        await refreshToken();
    }, 60000 * 5);
    return true
}

export const login = async (username, password) => {
    console.log("Logging in...");
    return await axios.post("/api/token/", {
        username,
        password,
    }).then(response => {
        return response.data;
    }).then(async data => {
        window.localStorage.removeItem(logout_cookie_key);
        return successfulLogin(data.access);
    });
}

export const logout = async () => {
    if (get(user).loggedIn) {
        console.log("Logging out...");
        await axios.delete("/api/token/clear/").then(response => {
            return response.data;
        }).then(data => {
            axios.defaults.headers.common = {};
            user.set(loggedOutUser);
            window.localStorage.setItem(logout_cookie_key, Date.now());
        });
    }
    goto('/login/');
}

export const refreshToken = async () => {
    if (window.localStorage.getItem(logout_cookie_key)) {
        await logout();
    } else {
        console.log("Refreshing Token...");
        return await axios.post("/api/token/refresh/").then(response => {
            return response.data;
        }).then(data => {
            return successfulLogin(data.access);
        });
    }
}

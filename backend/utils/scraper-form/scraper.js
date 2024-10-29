const axios = require('axios');
const cheerio = require('cheerio');
require('dotenv').config();

const base_url = "https://bva.cargotrack.net/default.asp";

async function login(user, password, axiosInstance) {
    const data = {
        user: user,
        password: password,
        Submit: "Log In",
        action: "login"
    };
    await axiosInstance.post(base_url, data, { headers: axiosInstance.defaults.headers });
}

async function sendtToCargo(axiosInstance, formData) {
    console.log("ESTAMOS MANDANDO LOS DATOS");
    const user = process.env.USER;
    const password = process.env.PASSWORD;
    login(user, password, axios)

    console.log('Data to send:', data);

    axiosInstance.post(base_url, data)
        .then(response => {
            console.log('Data sent successfully:', response.data);
        })
        .catch(error => {
            console.error('Error sending data:', error);
        });
}

module.exports = { login, sendUserData: sendtToCargo };

// server.js
const express = require('express');
const cors = require('cors');
const axios = require('axios');
const cheerio = require('cheerio');
require('dotenv').config();
const { login, sendUserData } = require('./scraper-form/scraper');
const path = require('path');

const app = express();
const port = process.env.PORT || 3001;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const base_url = "https://bva.cargotrack.net/default.asp";

app.post('/send-data', async (req, res) => {
    try {
        const user = process.env.USER;
        const password = process.env.PASSWORD;

        // Create an axios instance with default headers
        const axiosInstance = axios.create({
            headers: {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
                "Origin": "https://bva.cargotrack.net"
            }
        });

        // Perform login
        await login(user, password, axiosInstance);

        // Send user data
        const formData = req.body;
        // const response = await axiosInstance.post(base_url, formData);

        res.status(200).json({
            message: 'Data sent successfully',
            data: response.data
        });
    } catch (error) {
        console.error('Error sending data:', error);
        res.status(500).json({
            message: 'Error sending data',
            error: error.message
        });
    }
});

app.get('/registro', (req, res) => {
    res.sendFile(path.join(__dirname, 'registro.html'));
});

app.use(cors({origin: `*`}));

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
const express = require('express');
const bodyParser = require('body-parser');
const webhookController = require('./controllers/webhookController');

const app = express();

// Middleware
app.use(bodyParser.json());

// Ruta principal para verificar que el microservicio está corriendo
app.get('/', (req, res) => {
    res.send('🚀 Microservicio de Notificaciones está activo.');
});

// Rutas
app.post('/webhook/notify', webhookController.sendNotification);

module.exports = app;

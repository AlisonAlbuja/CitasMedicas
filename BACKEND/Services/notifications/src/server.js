const app = require('./app');

const PORT = process.env.PORT || 8050;  // Se cambia el puerto a 8050

app.listen(PORT, () => {
    console.log(`Microservicio de notificaciones ejecutándose en http://localhost:${PORT}`);
});

const redis = require('redis');

const client = redis.createClient({
    socket: {
        host: process.env.REDIS_HOST || 'localhost',
        port: process.env.REDIS_PORT || 6379
    }
});

client.connect()
    .then(() => console.log("✅ Conectado a Redis"))
    .catch(err => console.error("❌ Error al conectar con Redis:", err));

module.exports = client;

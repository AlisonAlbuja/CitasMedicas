require('dotenv').config();
const emailService = require('./src/services/emailService');

(async () => {
    try {
        console.log("🚀 Enviando email de prueba...");
        await emailService.sendEmail("paciente@email.com", "Dr. Juan Pérez", "2025-02-10 14:00:00", "Clínica SaludMedica");
        console.log("✅ Email enviado correctamente.");
    } catch (error) {
        console.error("❌ Error enviando el email:", error);
    }
})();

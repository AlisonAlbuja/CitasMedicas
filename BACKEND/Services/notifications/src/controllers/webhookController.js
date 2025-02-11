const emailService = require('../services/emailService');

exports.sendNotification = async (req, res) => {
    try {
        const { user_email, appointment_date, doctor, location } = req.body;

        if (!user_email) {
            return res.status(400).json({ error: "Se necesita un email para enviar la notificación" });
        }

        await emailService.sendEmail(user_email, doctor, appointment_date, location);

        res.status(200).json({ message: "Correo enviado correctamente" });
    } catch (error) {
        console.error("Error en el webhook:", error);
        res.status(500).json({ error: "Error al procesar la notificación" });
    }
};

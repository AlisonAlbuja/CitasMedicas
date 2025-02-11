require('dotenv').config();
const nodemailer = require('nodemailer');

const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: process.env.EMAIL_USER,  // Tu correo
        pass: process.env.EMAIL_PASS   // La App Password de Gmail
    }
});

exports.sendEmail = async (to, doctor, date, location) => {
    const mailOptions = {
        from: `"Clínica SaludMedica" <${process.env.EMAIL_USER}>`,
        to: to,
        subject: "📅 Recordatorio de Cita Médica",
        html: `
            <h2>📅 Tienes una Cita Médica</h2>
            <p><strong>Doctor:</strong> ${doctor}</p>
            <p><strong>Fecha:</strong> ${date}</p>
            <p><strong>Ubicación:</strong> ${location}</p>
            <br>
            <p>Por favor, confirma tu asistencia respondiendo a este correo.</p>
            <p>Saludos, <br> Clínica SaludMedica</p>
        `
    };

    await transporter.sendMail(mailOptions);
    console.log(`✅ Correo enviado a ${to}`);
};

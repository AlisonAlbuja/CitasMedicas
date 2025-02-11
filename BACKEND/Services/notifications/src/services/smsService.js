const twilio = require('twilio');

const client = new twilio(process.env.TWILIO_SID, process.env.TWILIO_AUTH_TOKEN);

exports.sendSMS = async (phone, doctor, date, location) => {
    await client.messages.create({
        body: `Tienes una cita con ${doctor} en ${location} el ${date}.`,
        from: process.env.TWILIO_PHONE_NUMBER,
        to: phone
    });

    console.log(`SMS enviado a ${phone}`);
};

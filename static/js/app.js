const express = require('express');
const nodemailer = require('nodemailer');
const path = require('path');

const app = express();

// Serve the entire static directory
app.use('/static', express.static(path.join(__dirname, 'static')));

// Enable form data parsing
app.use(express.urlencoded({ extended: true }));

const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: 'u2022120@gmail.com',
        pass: 'sqbe lqfu hovy msja'
    }
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'templates', 'index.html'));
});

app.post('/send', (req, res) => {
    const { first_name, last_name, email, message, phone } = req.body;
    const mailOptions = {
        from: 'u2022120@gmail.com',
        to: 'u2022120@gmail.com',
        subject: 'Query From the Portfolio',
        html: `
            <h3>Query From ${email}</h3>
            <ul>
                <li><b>First Name:</b> ${first_name}</li>
                <li><b>Last Name:</b> ${last_name}</li>
                <li><b>Email:</b> ${email}</li>
                <li><b>Phone Number:</b> ${phone}</li>
                <li><b>Message:</b><br>${message}</li>
            </ul>
        `
    };

    transporter.sendMail(mailOptions, (error, info) => {
        res.redirect('/#contact');
    });
});

const PORT = process.env.PORT || 4000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['SECRET_KEY'] = "tsfyguaistyatuis589566875623568956"
app.config['MAIL_SERVER'] = "smtp.googlemail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "u2022120@gmail.com"      # <-- your gmail address
app.config['MAIL_PASSWORD'] = "sqbe lqfu hovy msja"         # <-- your gmail app password

mail = Mail(app)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    message = request.form.get("message")
    phone_number = request.form.get("phone")
    msg_title = "Query From the Portfolio"
    sender = app.config['MAIL_USERNAME']
    recipient = "u2022120@gmail.com"

    msg_body = f"""
    <h3>Query From {email}</h3>
    <ul>
        <li><b>First Name:</b> {first_name}</li>
        <li><b>Last Name:</b> {last_name}</li>
        <li><b>Email:</b> {email}</li>
        <li><b>Phone Number:</b> {phone_number}</li>
        <li><b>Message:</b><br>{message}</li>
    </ul>
    """

    msg = Message(msg_title, sender=sender, recipients=[recipient])
    msg.html = msg_body

    try:
        mail.send(msg)
        flash("Message sent successfully!", "success")
    except Exception as e:
        print(e)
        flash("Failed to send message.", "danger")

    return redirect("/#contact")

if __name__ == "__main__":
    app.run(debug=True)
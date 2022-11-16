from flask import Flask, render_template, request
import requests
from datetime import datetime
import smtplib

app = Flask(__name__)
blog_api = "https://api.npoint.io/6052e8f71d69369f8bb7"

blog_response = requests.get(url=blog_api)
blog_data = blog_response.json()

today_date = datetime.now().year


@app.route('/')
def home():
    return render_template("index.html", post=blog_data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    pop_up = None
    if request.method == 'POST':
        data = request.form
        # print(data['username'])
        # print(data['user_email'])
        # print(data['phone_no'])
        # print(data['message_text'])
        pop_up = "Message Sent!"
        send = f"Name: {data['username']}\nEmail: {data['user_email']}\nPhone: {data['phone_no']}\nMessage: {data['message_text']}"
        with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
            connection.starttls()
            connection.login(user="louiedeon@yahoo.com", password="lyxahfengkbkkmgp")
            connection.sendmail(from_addr=f"louiedeon@yahoo.com",
                                to_addrs="louiedeon@yahoo.com",
                                msg=f"Subject:Clean Blog Contact\n\n{send}")
    return render_template("contact.html", feedback=pop_up)


@app.route('/post.html/<int:pid>')
def post(pid):
    return render_template("post.html", num=pid, post=blog_data)


if __name__ == "__main__":
    app.run(debug=True)

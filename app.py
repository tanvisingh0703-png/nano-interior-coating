from flask import Flask, render_template, request, redirect, url_for
from urllib.parse import quote

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():

    name = request.form.get("name", "")
    phone = request.form.get("phone", "")
    service = request.form.get("service", "")
    message = request.form.get("message", "")

    print("\n--- NEW ENQUIRY ---")
    print("Name:", name)
    print("Phone:", phone)
    print("Service:", service)
    print("Message:", message)
    print("-------------------")

    whatsapp_message = f"""Hello Nano Interior Coating,

I would like to enquire about your services.

Name: {name}
Phone: {phone}
Service: {service}
Requirement: {message}
"""

    whatsapp_url = "https://wa.me/919702377189?text=" + quote(whatsapp_message)

    return redirect(whatsapp_url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

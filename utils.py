from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import openai
import smtplib
from email.mime.text import MIMEText
import config

client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)
openai.api_key = config.OPENAI_API_KEY

def make_twiml(prompt):
    resp = VoiceResponse()
    resp.say(prompt, language="de-DE")
    resp.gather(input="speech", timeout=5, action="/gather")
    return str(resp)

def gpt_response(history):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=history
    )
    return response.choices[0].message.content

def send_email(summary):
    msg = MIMEText(summary)
    msg["Subject"] = "Neue Kundenanfrage"
    msg["From"] = config.EMAIL_USER
    msg["To"] = config.EMAIL_TO
    with smtplib.SMTP(config.EMAIL_SMTP_SERVER, config.EMAIL_SMTP_PORT) as server:
        server.starttls()
        server.login(config.EMAIL_USER, config.EMAIL_PASS)
        server.send_message(msg)

def send_whatsapp(to_number, summary):
    client.messages.create(
        body=summary,
        from_=config.WHATSAPP_FROM,
        to=f"whatsapp:{to_number}"
    )

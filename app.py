from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
import config, utils
import datetime

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    return utils.make_twiml("Hallo! Was kann ich für Sie tun?")

@app.route("/gather", methods=["POST"])
def gather():
    speech_text = request.form.get("SpeechResult", "")
    history = [
        {"role":"system","content":"Du bist Kundenagent für Bennis Haushelden."},
        {"role":"user","content":speech_text}
    ]
    answer = utils.gpt_response(history)
    resp = VoiceResponse()
    resp.say(answer, language="de-DE")
    resp.say("Möchten Sie mir noch etwas sagen? Wenn nein, legen Sie bitte auf.", language="de-DE")
    resp.gather(input="speech", timeout=5, action="/gather2")
    return str(resp)

@app.route("/gather2", methods=["POST"])
def gather2():
    followup = request.form.get("SpeechResult","")
    summary = f"Anliegen: {followup}\n\nGesprächszusammenfassung um {datetime.datetime.now():%Y-%m-%d %H:%M}"
    utils.send_email(summary)
    caller = request.form.get("From","")
    utils.send_whatsapp(caller, summary)
    resp = VoiceResponse()
    resp.say("Vielen Dank, wir melden uns zeitnah. Auf Wiederhören!", language="de-DE")
    resp.hangup()
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

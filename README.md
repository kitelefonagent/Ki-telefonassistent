# KI-Telefonassistent für Bennis Haushelden

Ein digitaler Telefonassistent, der Anrufe entgegennimmt, Anliegen aufnimmt, Rückfragen stellt und eine Zusammenfassung per E-Mail und WhatsApp versendet. Alles auf Deutsch.

## Anforderungen

- Twilio-Account mit Telefonnummer und WhatsApp Sandbox
- OpenAI API-Key
- SMTP-Zugang (z. B. Gmail)
- Hosting (z. B. Render.com)

## Startbefehle (für Render)

- **Start command:** `gunicorn app:app`
- **Python version:** 3.10 oder neuer

## Wichtige Umgebungsvariablen (.env)

- TWILIO_ACCOUNT_SID
- TWILIO_AUTH_TOKEN
- TWILIO_PHONE_NUMBER
- WHATSAPP_FROM
- EMAIL_SMTP_SERVER
- EMAIL_SMTP_PORT
- EMAIL_USER
- EMAIL_PASS
- EMAIL_TO
- OPENAI_API_KEY

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_email = "mmaqsad004@gmail.com"
from_password = "spfd vubt yvgs odoj"
to_email = "azizegamov64@gmail.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = 'Parolni tiklash'
msg['From'] = 'Onlayn Kutubxona'
msg['To'] = to_email
user = "admin"

html = f"""\
    <div style="color: black !important;">
        <h2>Salom {user}</h2>
        <p>Siz saytda parolingizni o'zgartirish uchun so'rov yubordingiz, parolni o'zgartirish uchun pastdagi tugma orqali saytda kiring.</p>
        <a href="https://google.com" target="_blank" style="display: inline-block; width: 150px; height: 50px; background-color: aqua; text-align: center; line-height: 50px; text-decoration: none; color: black;">Kirish</a>
    </div>
"""

part2 = MIMEText(html, 'html')

msg.attach(part2)

smtp_server = 'smtp.gmail.com'
smtp_port = 587

try:
    s = smtplib.SMTP(smtp_server, smtp_port)
    s.starttls()
    s.login(from_email, from_password)
    s.sendmail(from_email, to_email, msg.as_string())
    print("Email muvaffaqiyatli yuborildi")
except Exception as e:
    print(f"Email yuborishda xato: {e}")
finally:
    s.quit()

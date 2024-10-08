import os
import smtplib


from dotenv import load_dotenv
load_dotenv()

recipients_email = input("input recipients email: ")
recipients_name = input("input recipients name: ")
senders_email = input("input your email adress: ")
senders_name = input("input your name: ")
title = input("input the title of your letter: ")
url = "https://dvmn.org/referrals/QSRDMwTyHx3x7oBaTQww14M3dV7niodGMhKv9r6s/"

letter = f"""From: {senders_email}
To: {recipients_email}
Subject: {title}
Content-Type: text/plain; charset="UTF-8";
          
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

letter = letter.replace("%friend_name%", recipients_name)
letter = letter.replace("%my_name%", senders_name)
letter = letter.replace("%website%", url)
letter = letter.encode("UTF-8")

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

server = smtplib.SMTP_SSL('smtp.mail.ru:465')
server.login(login, password)
server.sendmail(senders_email, recipients_email, letter)
server.quit()
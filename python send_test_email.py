import yagmail

try:
    yag = yagmail.SMTP(
        user='dkzhs0405@nate.com',
        password='anjfdksqhk132!',
        host='smtp.mail.nate.com',
        port=587,
        smtp_starttls=True,
        smtp_ssl=False
    )

    yag.send(
        to='dkzhs0405@nate.com',
        subject='테스트 제목',
        contents='이것은 테스트 메일입니다.'
    )

    print("메일 전송 성공!")

except Exception as e:
    print("메일 전송 실패:", e)

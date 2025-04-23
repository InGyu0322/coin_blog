import openai
import datetime
import markdown2
import yagmail
import os

# 날짜 설정
now = datetime.datetime.now()
date_str = now.strftime('%Y-%m-%d')
filename = f"post_{date_str}.md"

# ChatGPT로 시장분석 생성
openai.api_key = os.getenv("OPENAI_API_KEY")
prompt = f"""
너는 완벽한 시장분석가야. 오늘의 날짜는 {date_str}야. 오늘의 암호화폐 시장 상황을 1200자~1500자 분량으로 분석해줘.
각 단락 끝에는 관련 이미지를 하나 포함한다고 가정하고, 주요 키포인트는 볼드 처리해줘.
"""

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a crypto market analyst."},
        {"role": "user", "content": prompt}
    ]
)

content = response['choices'][0]['message']['content']

# 마크다운 파일로 저장
with open(filename, 'w', encoding='utf-8') as f:
    f.write(f"# {date_str} 암호화폐 시장분석\n\n")
    f.write(content)

# 이메일 발송
email_user = os.getenv("SMIP_USER")
email_pass = os.getenv("SMIP_PASS")
receiver = "dkzhs0405@nate.com"

subject = f"[CoinWriter] {date_str} 암호화폐 시장분석"
html_content = markdown2.markdown(content)

yag = yagmail.SMTP(user=email_user, password=email_pass)
yag.send(to=receiver, subject=subject, contents=[html_content, filename])

print(f"✅ {filename} 생성 및 이메일 전송 완료")

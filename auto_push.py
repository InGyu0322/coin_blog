from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# 환경 변수 불러오기
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
REPO_NAME = os.getenv('REPO_NAME')

# 환경변수 설정되지 않으면 에러 발생
if not all([GITHUB_TOKEN, GITHUB_USERNAME, REPO_NAME]):
    raise EnvironmentError("GITHUB_TOKEN, GITHUB_USERNAME, REPO_NAME 환경변수를 설정하세요. :)")

print(f"Token: {GITHUB_TOKEN}")

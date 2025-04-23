from dotenv import load_dotenv
import os

load_dotenv()  # .env 파일에서 환경변수 로드

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")

if not all([GITHUB_USERNAME, GITHUB_TOKEN, REPO_NAME]):
    raise EnvironmentError("GITHUB_USERNAME, GITHUB_TOKEN, REPO_NAME 환경변수를 설정하세요. :)")
print(f"GITHUB_USERNAME: {GITHUB_USERNAME}")
print(f"GITHUB_TOKEN: {GITHUB_TOKEN}")
print(f"REPO_NAME: {REPO_NAME}")

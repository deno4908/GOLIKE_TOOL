import requests
import os
import json
from services.color import Color
from tqdm import tqdm
import sys
GITHUB_TOKEN  =  "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"
OWNER = "deno4908"
REPO = "GOLIKE_TOOL"
BRANCH = "main"
LOCAL_CONFIG_PATH = "config/config.json"
CONFIG_PATH_IN_REPO = "config/config.json"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3.raw"
}

def list_all_files_from_repo():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/git/trees/{BRANCH}?recursive=1"
    response = requests.get(url, headers={"Authorization": f"token {GITHUB_TOKEN}"})
    files = []
    if response.status_code == 200:
        data = response.json()
        for item in data['tree']:
            if item['type'] == 'blob':
                path = item['path']
                if path != CONFIG_PATH_IN_REPO:  
                    files.append(path)
        return files
    else:
        print(f"{Color.RED} Không thể duyệt repo.{Color.END}")
        return []
def fetch_file_content(path):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{path}?ref={BRANCH}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.text
    else:
        print(f"{Color.RED} Không thể tải file: {path}{Color.END}")
        return None
def load_version_from_text(text):
    try:
        data = json.loads(text)
        return data["data"]["VERSION"]
    except Exception as e:
        print(f"{Color.RED} Lỗi đọc VERSION: {e}{Color.END}")
        return None
def load_version_from_text(text):
    try:
        data = json.loads(text)
        return data["data"]["VERSION"]
    except Exception as e:
        print(f"{Color.RED} Lỗi đọc VERSION: {e}{Color.END}")
        return None

def read_local_version():
    with open(LOCAL_CONFIG_PATH, "r", encoding="utf-8") as f:
        return load_version_from_text(f.read())

def read_remote_version():
    content = fetch_file_content(CONFIG_PATH_IN_REPO)
    if content:
        return load_version_from_text(content)
    return None

def compare_versions(v1, v2):
    def parse(v): return list(map(int, v.lstrip("v").split(".")))
    return parse(v1) < parse(v2)

def download_and_replace_all():
    files = list_all_files_from_repo()
    print(f"📦 Đang cập nhật {len(files)} file...\n")
    for file in tqdm(files, desc="Cập nhật", unit="file"):
        content = fetch_file_content(file)
        if content:
            dir_path = os.path.dirname(file)
            if dir_path:
                os.makedirs(dir_path, exist_ok=True)
            with open(file, "w", encoding="utf-8") as f:
                f.write(content)
    print(f"\n{Color.LIGHT_GREEN}Đã cập nhật tất cả file.{Color.END}")

def update_version_in_config(new_version):
    with open(LOCAL_CONFIG_PATH, "r+", encoding="utf-8") as f:
        data = json.load(f)
        data["data"]["VERSION"] = new_version
        f.seek(0)
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.truncate()
def check_and_update():
    local_ver = read_local_version()
    remote_ver = read_remote_version()
    if local_ver and remote_ver and compare_versions(local_ver, remote_ver):
        
        while True:
            try:
                chp = input(f"{Color.LIGHT_BLUE}Có bản cập nhật mới: {remote_ver} (hiện tại: {local_ver}) (Y/N) : ")
                if chp.lower()=="y" or chp.lower()=="n":
                    break
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                pass
        if chp.lower() == "y":
            download_and_replace_all()
            update_version_in_config(remote_ver)
            print(f"{Color.LIGHT_GREEN}Cập nhật xong.")
            sys.exit(0)
        else :
            pass
    else:
        print(f"{Color.LIGHT_GREEN}Phiên bản hiện tại là mới nhất.")


# TOOL Auto Golike

TOOL Auto Làm nhiệm vụ golike với requests và ADB


![Logo](https://i.postimg.cc/8Ppstqv5/download.jpg)


## Ngôn Ngữ Lập Trình 

**TOOL:** Python


## 🚀 Hướng Dẫn Chạy TOOL
**Lưu Ý** : Python 3.12.10 và 64bit

**Windows**

- Cài ADB : [ADB](https://developer.android.com/tools/releases/platform-tools)
- Cài packages :  ```pip install -r requirements.txt```
- Run TOOL :  ```python main.py```


**Ubuntu - amd64/x86**

- Cập nhật hệ thống : ```sudo apt update && sudo apt upgrade -y```
- Cài Python : ```sudo apt install python3 python3-pip -y```
- Cài ADB :  ```sudo apt install android-tools-adb ```
- Cài GIT :  ```sudo apt install git -y ```
- clone TOOL : ```git clone https://github.com/deno4908/GOLIKE_TOOL```
- cd :  ```cd GOLIKE_TOOL```
- Cài packages : ```pip install -r requirements.txt --break-system-packages --force-reinstall --ignore-installed```
- Run TOOL :  ```python3 main.py```

**proot-distro(termux)**
- Cập nhật hệ thống pkg :  ```pkg update && pkg upgrade```
- Cho phép truy cập file trong máy : ```termux-setup-storage```
- cài proot-distro :  ```pkg install proot-distro```
- cài Ubuntu :  ```proot-distro install ubuntu```
- Login ubuntu local : ```proot-distro login ubuntu```
- Cập nhật hệ thống : ```apt update && apt upgrade -y```
- Cài Python : ```apt install python3 python3-pip -y```
- Cài ADB :  ```apt install android-tools-adb ```
- Cài GIT :  ```apt install git -y ```
- clone TOOL : ```git clone https://github.com/deno4908/GOLIKE_TOOL```
- cd :  ```cd GOLIKE_TOOL```
- Cài packages : ```pip install -r requirements.txt --break-system-packages --force-reinstall --ignore-installed```
- Run TOOL :  ```python3 main.py```

**ADB(wireless)**
- pair(ghép đôi) : ```adb pair {IP}:{PORT}``` sau đó nhập mã ghép đôi là được
- connect(kết nối) : ```adb connect {IP}:{PORT}```

## TOOL
![GIAO DIỆN](https://i.postimg.cc/Dz2CZf4h/image.png)

## Authors

- [@Deno9099](https://github.com/deno4908)


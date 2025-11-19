# app.py - แอปพลิเคชัน Python/Flask ตัวอย่าง
from flask import Flask
import os

app = Flask(__name__)

# ดึงชื่อ Container App จาก Environment Variable (ถ้ามี)
CONTAINER_APP_NAME = os.environ.get('CONTAINER_APP_NAME', 'Azure Container App Default')

@app.route('/')
def hello():
    # แสดงข้อความต้อนรับและชื่อแอปพลิเคชัน
    return f"<h1>Hello from {CONTAINER_APP_NAME}!</h1><p>This application was deployed using Azure DevOps Pipeline.</p>"

if __name__ == '__main__':
    # รันแอปพลิเคชันบนพอร์ต 8080 ซึ่งเป็นพอร์ตมาตรฐานสำหรับ Container Apps
    app.run(debug=True, host='0.0.0.0', port=8080)

# ใช้ Base Image ของ Python
FROM python:3.9-slim

# ตั้งค่า Environment Variable สำหรับพอร์ตที่แอปจะรัน
ENV PORT 8080

# ตั้งค่า Work Directory ภายใน Container
WORKDIR /app

# คัดลอกไฟล์ Dependencies และติดตั้ง
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกโค้ดแอปพลิเคชัน
COPY app.py .

# เปิดพอร์ต
EXPOSE ${PORT}

# คำสั่งสำหรับรันแอปพลิเคชัน
CMD ["python", "app.py"]

# ---- Base Image ----
    FROM python:3.11-slim

    # ---- Environment Setup ----
    ENV PYTHONUNBUFFERED=1 \
        PYTHONDONTWRITEBYTECODE=1
    
    # ---- Working Directory ----
    WORKDIR /app
    
    # ---- Install Dependencies ----
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    
    # ---- Copy App Code ----
    COPY . .
    
    # ---- Expose Port ----
    EXPOSE 8000
    
    # ---- Run the Application ----
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
    
# Dockerfile

# 1. Use an official Python runtime as a parent image
# We use a 'slim' version for a smaller image size
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file into the container
COPY requirements.txt .

# 4. Install any needed packages specified in requirements.txt
# --no-cache-dir makes the image smaller
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application's code into the container
# This includes main.py and the artifacts/ folder
COPY . .

# 6. Expose the port the app runs on
# This informs Docker that the container listens on port 8000
EXPOSE 8000

# 7. Define the command to run the application
# This is the command that will be executed when the container starts
# We use --host 0.0.0.0 to make it accessible from outside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
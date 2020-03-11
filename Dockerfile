FROM python:3.6

# Add sample application
ADD application.py /tmp/application.py

EXPOSE 8000

# Run it
ENTRYPOINT ["python", "/app/application.py"]

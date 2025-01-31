# Payment

Payment with payme and click with python django.

## Features

- List key features
- Describe functionality

## Technologies Used

- Django
- Python

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Nazimjonovna/Payment.git

2. Install libs
    ```bash
    pip install -r requirements.txt

3. Create .env file and write all params like .env.example file

4. NGROK configuration
    Visit to ngrok.com and sign_up 
    Enter to dashboard and get your ngrok_token
    Open cmd(terminal) and paste this:
    ```bash 
    ngrok config add-authtoken YOUR_AUTHTOKEN 
    after then run your project:
    ```bash(vs code)
    python manage.py runserver
    back to bash(cmd)
    ```bash
    ngrok http 8000

    ![Alt text](image.png)
    take this link and paste to ALLOWED_HOSTS which is located in settings.py in Payment folder




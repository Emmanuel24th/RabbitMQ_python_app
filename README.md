 since homebrew is my packager, I had to create a virtual environment on my 
MacOS.
Create a virtual environment for your Python project using `python3 -m venv 
my_v_environs` 

2. Activate the virtual environment using `source 
my_v_environs/bin/activate`

3.  Install Celery using `pip install celery`. This will install Celery in 
your virtual environment, without interfering with the system packages 
managed by Homebrew. 
4. pip install flask   pip install flask mail :  
5. Set up the Python application:  mkdir my_mailapp cd my_mailapp/ nano 
my_mailfile: add all dependencies 
6. pip install flask emails: installing python app requirements. 
7. Nginx Configuration Install Nginx: brew install nginx Create a new 
configuration file: touch my_mailapp.conf nano my_mailapp.conf: add all 
dependencies 
8. brew services start rabbitmq 
9. celery -A tasks worker
10. flask run -p 5000 : to run the flask app 
11. End point access, EXPOSING ENDPOINT USING NGROK brew install ngrok:
12. Sign up for an account: https://dashboard.ngrok.com/signup 
13. Install your authtoken: 
https://dashboard.ngrok.com/get-started/your-authtoken 
14. ngrok config add-authtoken (token)
15. ngrok http http://localhost:5000

# 
RabbitMQ_python_app

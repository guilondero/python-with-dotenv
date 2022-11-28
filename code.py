import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())     #your file need to be ".env" and stay in the same folder of your code.py, for more infos read the library
#in a real project your .env never goes to your repositori, this is a "secret" file with yours credencial


userName = os.getenv("account")

password = os.getenv("pass")

print(userName, password)

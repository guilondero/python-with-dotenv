import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())     #your file need to be ".env" and stay in the same folder of your code.py, for more infos lead the librerary 

userName = os.getenv("account")

password = os.getenv("pass")

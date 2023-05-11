from datetime import datetime


def log_message(message, log_level="INFO"):
    with open("logs.txt", "a+") as file:
        now = datetime.now()
        file.writelines(
            f"{now.strftime('%d.%m.%Y, %H:%M:%S')} - {log_level} - {message}\n"
        )

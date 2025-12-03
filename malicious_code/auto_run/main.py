# main.py for auto_run technique
from function4_send_email import main as send_email_main
from function5_startup_shortcut import main as startup_shortcut_main
from function6_registry_key import main as registry_key_main


def main():
    print("Running auto_run technique...")
    send_email_main()
    startup_shortcut_main()
    registry_key_main()


if __name__ == "__main__":
    main()

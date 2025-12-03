# main.py for delivery technique
from function1_gui import main as gui_main
from function2_hidden_folder import main as hidden_folder_main
from function3_copy_file import main as copy_file_main


def main():
    print("Running delivery technique...")
    gui_main()
    hidden_folder_main()
    copy_file_main()


if __name__ == "__main__":
    main()

# main.py for spreading technique
from function7_scan_shares import main as scan_shares_main
from function8_replicate import main as replicate_main
from function9_log import main as log_main


def main():
    print("Running spreading technique...")
    scan_shares_main()
    replicate_main()
    log_main()


if __name__ == "__main__":
    main()

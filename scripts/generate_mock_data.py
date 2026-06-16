import pandas as pd
import os

# Define data path relative to this script's location
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

# 1. Map the OmniCare Digital Cross-Framework Failure (The TLS 1.0/1.1 Flaw)
crosswalk_fields = {
    "ControlID": ["HI-164.312-E1", "NIST-SC-8", "HITRUST-09.M", "SOC2-CC6.7"],
    "Framework": ["HIPAA Security Rule", "NIST 800-53 Rev 5", "HITRUST CSF v11", "SOC 2 TSC"],
    "ControlName": ["Transmission Security", "Transmission Confidentiality", "Transmission Security", "Transmission Integrity"],
    "AssetTarget": ["clinical-db.omnicare.local"] * 4,
    "Status": ["Non-Compliant"] * 4  # The single technical flaw compromises all four
}

# 2. Establish the OmniCare Multi-Cloud Risk Register Entry
risk_fields = {
    "RiskID": ["RSK-2026-001"],
    "RiskTitle": ["Insecure ePHI Transit via Legacy TLS 1.0"],
    "CloudEnvironment": ["GCP-Analytics-Cluster / AWS-API-Gateway"],
    "InherentRiskScore": [16],  # High Risk on a standard 5x5 healthcare risk matrix
    "MappedControls": ["HI-164.312-E1, NIST-SC-8, HITRUST-09.M, SOC2-CC6.7"],
    "RemediationSLA": ["14 Days"]
}

# Ensure data directory exists
os.makedirs(data_dir, exist_ok=True)

# Generate and save the data structures to CSV
pd.DataFrame(crosswalk_fields).to_csv(os.path.join(data_dir, "master_hipaa_crosswalk.csv"), index=False)
pd.DataFrame(risk_fields).to_csv(os.path.join(data_dir, "risk_register.csv"), index=False)

print("🚀 OmniCare Digital local data files successfully generated in /data/!")
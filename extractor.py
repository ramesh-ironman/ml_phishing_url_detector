import re
import pandas as pd
import numpy as np

FEATURE_COLS = ['having_ip_address', 'url_length', 'shortining_service', 'having_at_symbol', 
    'double_slash_redirecting', 'prefix_suffix', 'having_sub_domain', 
    'sslfinal_state', 'domain_registeration_length', 'favicon', 
    'port', 'https_token', 'request_url', 'url_of_anchor', 'links_in_tags', 
    'sfh', 'submitting_to_email', 'abnormal_url', 'redirect', 'on_mouseover', 
    'rightclick', 'popupwidnow', 'iframe', 'age_of_domain', 'dnsrecord', 
    'web_traffic', 'page_rank', 'google_index', 'links_pointing_to_page', 
    'statistical_report']

def extract_features(url):
    # Simplified: for demo, generate dummy numeric feats matching dataset (improve later)
    feats = np.zeros(len(FEATURE_COLS))
       # Key phishing detectors (match UCI logic):
    feats[0] = 1 if re.match(r'\d+\.\d+\.\d+\.\d+', url) else 0  # IP address
    feats[1] = 1 if len(url) > 54 else 0 if len(url) < 18 else -1  # URL length
    feats[2] = 1 if any(s in url.lower() for s in ['bit.ly', 'tinyurl']) else 0  # Shortener
    feats[3] = 1 if '@' in url else 0  # @ symbol
    feats[4] = 1 if url.count('//') > 1 else 0  # Double slash
    feats[5] = 1 if '-' in url.split('://')[1].split('/')[0] else 0  # Prefix/suffix (-)
    feats[6] = 1 if url.count('.') > 2 else 0  # Subdomains
    feats[7] = 0 if url.startswith('https') else -1  # SSL (simplified)
    
    # Suspicious keywords (triggers phishing):
    suspicious = ['paypal', 'login', 'bank', 'account', 'update', 'verify']
    feats[17] = 1 if any(word in url.lower() for word in suspicious) else 0  # Abnormal_URL
    return pd.DataFrame([feats], columns=FEATURE_COLS)

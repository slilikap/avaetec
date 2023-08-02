import json
import requests
import urllib

# You may need to install Requests pip
# python -m pip install requests

class IPQS:
    key = 'sXCNJk2mg1vH4Uiukj6ogk3lHPdmLY8Y'
    def malicious_url_scanner_api(self, url: str, vars: dict = {}) -> dict:
        url = 'https://www.ipqualityscore.com/api/json/url/%s/%s' % (self.key, urllib.parse.quote_plus(url))
        x = requests.get(url, params = vars)
        print(x.text)
        return (json.loads(x.text))

if __name__ == "__main__":
    """
    URL to scan - URL Encoded in cURL function below.
    """
    URL = 'https://www.goodbom.com.br'

    #Adjustable strictness level from 0 to 2. 0 is the least strict and recommended for most use cases. Higher strictness levels can increase false-positives.
    strictness = 0

    #custom feilds
    additional_params = {
        'strictness' : strictness
    }

    ipqs = IPQS()
    result = ipqs.malicious_url_scanner_api(URL, additional_params)

    if 'success' in result and result['success'] == True:
        print(result)
        """
        NOTICE: If you want to use one of the examples below, remove
        any lines containing /*, */ and *-, then remove * from any of the
        the remaining lines.
        """
        """
        - Example 1: Identify suspicious URLs regardless of Risk Score
        if result['suspicious'] == True:
        # flag suspicious URL
        }
        """
        
        """
        - Example 2: We'd like to block all malicious URLs suspected of being used for phishing or malware
        
        if result['phishing'] == True or result['malware'] === True or result['risk_score'] > 85):
            # flag high risk URLs likely to be malicious
        }
        """
        
        """
        - Example 3: We'd like to block all links on parked domains
        
        if result['parking'] == True:
        	# flag parked domains
        }
        """

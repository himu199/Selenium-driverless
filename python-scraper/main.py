import tls_client
from tls-client import exceptions
from extruct.jsonld import JsonLdExtractor
from dataclasses import dataclass

def create_session() -> tls_client.Session:
    if os.getenv("mobileproxy") is None:
        print("no proxy found, quitting")
        quit()
    else:
        proxies = {"http": os.getenv("mobileproxy")}




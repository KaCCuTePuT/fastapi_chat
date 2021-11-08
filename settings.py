from main import app


# JWT settings
ALGORITHM = "HS256"
ACCESS_TOKEN_JWT_SUBJECT = "access"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
SECRET_KEY = "Sdasdad3w#RmF34ef43%E5&*6DV%$5DSvBF*fY9V(y*&VNFdfBU(t8DnfDS"

# Test settings
BASE_URL = 'http://127.0.0.1:8000/'
DATA_FOR_GETTING_TOKEN1 = {
    "phone": "79991234567",
    "verification_code1": "string",
    "verification_code2": "string"
}
DATA_FOR_GETTING_TOKEN2 = {
    "phone": "70009998877",
    "verification_code1": "string",
    "verification_code2": "string"
}
HTTPX_CLIENT_SETTINGS = {
    'app': app,
    'base_url': BASE_URL,
    'follow_redirects': True
}

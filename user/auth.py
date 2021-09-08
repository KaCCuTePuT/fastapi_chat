from fastapi_users.authentication import JWTAuthentication


SECRET = '3430897fdsldhfd;l@!#@%%^&fggfgfg56676567'

auth_backends = []

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

auth_backends.append(jwt_authentication)

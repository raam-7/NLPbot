from core.security import create_access_token

token = create_access_token(
    {
        "sub": "raam@gmail.com"
    }
)

print("\nJWT Token:\n")
print(token)
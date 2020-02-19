curl -X POST \
-H "Content-Type: application/json" \
-d '{
        "password": "$leafnoise%",
        "type": "normal",
        "username": "brian.lobo@moorea.io"
    }' \
-s https://taiga.leafnoise.io/api/v1/auth > token.json
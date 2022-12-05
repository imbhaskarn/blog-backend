def authenticate_token():
    def decorator(request: object):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token: # throw error if no token provided
           return {"message": "A valid token is missing!"}
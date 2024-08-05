async def app(scope, receive, send):

    breakpoint()

    # Ensure the request is an HTTP request
    assert scope['type'] == 'http'

    # Extract the request path
    path = scope['path']

    # Determine the response body based on the request path
    if path == '/':
        response_body = b'Hello, world!'
    elif path.startswith('/items/'):
        item_id = path.split('/')[-1]
        response_body = f'Item ID: {item_id}'.encode()
    else:
        response_body = b'Not Found'

    # Define the response headers
    headers = [(b'content-type', b'text/plain')]

    # Send the HTTP response start event
    await send({
        'type': 'http.response.start',
        'status': 200 if path in ['/', '/items/'] else 404,
        'headers': headers,
    })

    # Send the HTTP response body event
    await send({
        'type': 'http.response.body',
        'body': response_body,
    })

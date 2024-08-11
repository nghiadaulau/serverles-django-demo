import traceback

handler = None
error = ''
try:
    from serverless_django_demo.asgi import handler
except Exception as e:
    exc_obj = e
    a = traceback.format_exception(None, exc_obj, exc_obj.__traceback__)
    for i in a:
        print(i)
    error = "".join(a)


def _handler(event, context):
    if not handler:
        return {"error": error}
    response = handler(event, context)

    return response

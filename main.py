from bottle import route, run, request, HTTPResponse


@route('/<p:re:.*>')
def index(p):
    host = request.get_header("Host", "unknown")
    if host == "unknown":
        return "OK"
    segments = host.split(".")
    if len(segments) < 2:
        return HTTPResponse(body="need more Host", status=400)

    try:
        code = int(segments[0])
    except ValueError:
        return HTTPResponse(body="bad Host", status=400)

    return HTTPResponse(status=code)


if __name__ == "__main__":
    run(host='localhost', port=8080)

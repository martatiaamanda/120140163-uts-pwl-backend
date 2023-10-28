from pyramid.view import view_config
from pyramid.response import Response


@view_config(route_name="home", renderer="json")
def my_view(request):
    return Response(status=200, json_body={"status": True, "message": "OK"})

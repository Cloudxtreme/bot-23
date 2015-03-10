from pyramid.response import Response
from pyramid.view import view_config
from pyramid.security import (
    remember,
    forget,
)
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
)
from .models import (
    DBSession,
    )


@view_config(route_name='home', renderer='templates/home.pt')
def home(request):
    return {}

@view_config(route_name='login', renderer='templates/login.pt')
def login(request):
    return {}

@view_config(route_name='logout')
def logout(request):
    '''
    view to logout from bot
    '''
    return HTTPFound(location = request.route_url('home'),
                        headers = forget(request))

@view_config(route_name='dashboard', renderer='templates/dashboard.pt')
def dashboard(request):
    return {}




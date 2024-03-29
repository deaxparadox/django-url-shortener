from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import (
    render, 
    get_object_or_404, 
    redirect
)
from django.urls import path
from django.views.generic import ListView

from .models import URL

def index_view(request):
    return render(
        request,
        "shortener/index.html"
    )


class IndexView(ListView):
    model = URL
    template_name = "shortener/index_generic.html"


def root(request, url_hash: str|None = None):
    """
    This receives an argument called `url_hash` from the `URL` requested by a user. Inside the function, the first line tries to get the URL from the database using the `url_hash` argument. If not found, it returns the HTTP 404 error to the client, which means that the resource is missing. Afterwards, it increments the `clicked` property of the URL   entry, making sure to track how many times the URL is accessed. At the end, it redirects the client to the requested URL.

    The `root` View will be accessible in the `/` path of your server, accepting a `url_hash` as a string parameter.
    """
    url_hash = request.GET.get("q", None)
    if not url_hash:
        return redirect(reversed("shortener:index"))
    url = get_object_or_404(URL, url_hash=url_hash)
    url.clicked()

    return redirect(url.full_url)
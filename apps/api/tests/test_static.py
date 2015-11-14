import os


def test_static(client, settings):
    """
    Make sure that we will receive index page on all requests except /api and /admin
    """
    filename = os.path.join(settings.BASE_DIR, 'static', 'index.html')
    with open(filename) as fd:
        index = fd.read()

    def check_url(url):
        resp = client.get(url)
        assert resp.status_code == 200
        assert resp['Content-Type'] == 'text/html; charset=utf-8'
        assert resp.content == index

    check_url('/')
    check_url('/login')
    check_url('/dashboard')
    check_url('/asdf/asdf')

    resp = client.get('/admin')
    assert resp.content != index

    resp = client.get('/api')
    assert resp.content != index


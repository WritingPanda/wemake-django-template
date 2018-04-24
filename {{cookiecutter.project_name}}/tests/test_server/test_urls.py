# -*- coding: utf-8 -*-


def test_admin_unauthorized(client):
    """This test ensures that admin panel requires auth."""
    response = client.get('/admin/')

    assert response.status_code == 302


def test_admin_authorized(admin_client):
    """This test ensures that admin panel is accessible."""
    response = admin_client.get('/admin/')

    assert response.status_code == 200


def test_robots_txt(client):
    """This test ensures that `robots.txt` is accessible."""
    response = client.get('/robots.txt')

    assert response.status_code == 200
    assert response.get('Content-Type') == 'text/plain'


def test_humans_txt(client):
    """This test ensures that `humans.txt` is accessible."""
    response = client.get('/humans.txt')

    assert response.status_code == 200
    assert response.get('Content-Type') == 'text/plain'

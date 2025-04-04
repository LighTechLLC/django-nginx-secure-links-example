### Into

This is a simple Django project which shows how to use django-nginx-secure-links: https://github.com/lightechllc/django-nginx-secure-links/

### Quick Setup

```bash
docker compose up -d
```

### Important notes

1. Admin access:
   - URL: http://127.0.0.1:8000/admin/
   - Username: admin
   - Password: 1234
2. Django views [examples](src/django_project/views.py):
   - http://127.0.0.1:8000/private-doc/1/
   - http://127.0.0.1:8000/public-doc/1/
3. We set up `MEDIA_URL = 'http://127.0.0.1:8090/media/'` using nginx absolute url, it allows us to be directly connected to nginx container by copy and pasting URL to browser.
4. For emulating Nginx local setup we described steps using ubuntu image there: [Dockerfile.nginx](etc/Dockerfile.nginx). The Dockerfile should not be used on production, it's just a simple example how to set up nginx-extras.
5. Nginx site config example file described there: [default.site.conf](etc/default.site.conf).

### Optional

You can also generate Nginx locations config blocks for media files by running command:
```bash
docker  compose exec backend python manage.py secure_links_nginx_location
```

### Clean up resources

```bash
docker compose down
```
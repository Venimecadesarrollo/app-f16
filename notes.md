## Esto es para ocultar una view detrás del login
```python
from django.contrib.auth.decorators import login_required

@login_required
def protected_view(request):
    return render(request, 'protected_page.html')
```

-----------------------------------------------------------------

### Esto es para crear un postgresql en DOCKER
```shell
docker run --name django-postgres -e POSTGRES_USER=test_user -e POSTGRES_PASSWORD=test_password -p 5432:5432 -d postgres
```

Luego se debe ejecutar esto desde docker:
```shell
psql -U test_user # Para acceder a la consola de la DB

CREATE DATABASE f16_database OWNER test_user;
GRANT ALL PRIVILEGES ON DATABASE f16_database TO test_user;
```

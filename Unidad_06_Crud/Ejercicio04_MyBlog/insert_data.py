import django, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Ejercicio04_MyBlog.settings")
django.setup()

from blog.models import Author, Post, Comment

# Create authors
authors = [
    Author(name="Ana", email="ana@example.com"),
    Author(name="Eva", email="eva@example.com"),
    Author(name="Sara", email="sara@example.com"),
    Author(name="carlos", email="carlos@example.com"),
    Author(name="jose", email="jose@example.com")
]

for author in authors:
    author.save()
    
# Create posts
posts = [
    Post(title="Cocina de verano", text="Recetas frescas para el verano", author=authors[0], date="2024-07-01 10:00:00"),
    Post(title="Decoración de interiores", text="Ideas para decorar tu casa", author=authors[1], date="2024-07-02 10:00:00"),
    Post(title="Viajes por el mundo", text="Experiencias de viajes por todo el mundo", author=authors[2], date="2024-07-03 10:00:00"),
    Post(title="Música en directo", text="Conciertos y festivales de música", author=authors[3], date="2025-01-10 10:00:00"),
    Post(title="Deporte y salud", text="Consejos para mantenerse en forma", author=authors[4], date="2025-01-11 10:00:00"),
    Post(title="Tecnología y gadgets", text="Últimas novedades en tecnología", author=authors[0], date="2025-01-12 10:00:00"),
    Post(title="Cine y series", text="Reseñas de películas y series", author=authors[1], date="2025-01-13 10:00:00"),
    Post(title="Literatura clásica", text="Análisis de obras literarias clásicas", author=authors[2], date="2025-01-14 10:00:00"),    
]

for post in posts:
    post.save()
    
# Create comments

comments = [
    Comment(post=posts[0], author=authors[1], text="Me encantan las recetas!"),
    Comment(post=posts[0], author=authors[2], text="Qué buena pinta!"),
    Comment(post=posts[1], author=authors[2], text="Me gustan mucho las ideas"),
    Comment(post=posts[2], author=authors[0], text="Qué envidia!"),
    Comment(post=posts[3], author=authors[1], text="Me encanta la música en directo"),
    Comment(post=posts[4], author=authors[2], text="Muy buenos consejos"),
    Comment(post=posts[5], author=authors[3], text="Me encantan los gadgets"),
]

for comment in comments:
    comment.save()    
import django, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Ejercicio04_Formacion.settings")
django.setup()

from cursos.models import Estudiante, Curso

# Insertar datos en la tabla Estudiante
estudiantes = [
    Estudiante(nombre='María', apellidos='López', correo = 'marialopez@gmail,com', telefono='987654321', fecha_nacimiento='2000-01-01'),
    Estudiante(nombre='Juan', apellidos='Pérez', correo='juanperez@gmail.com', telefono='123456789', fecha_nacimiento='1999-02-02'),
    Estudiante(nombre='Ana', apellidos='García', correo='anagarcia@gmail.com', telefono='234567890', fecha_nacimiento='2001-03-03'),
    Estudiante(nombre='Luis', apellidos='Martínez', correo='luismartinez@gmail.com', telefono='345678901', fecha_nacimiento='1998-04-04'),
    Estudiante(nombre='Carmen', apellidos='Rodríguez', correo='carmenrodriguez@gmail.com', telefono='456789012', fecha_nacimiento='2002-05-05'),
    Estudiante(nombre='Pedro', apellidos='Gómez', correo='pedrogomez@gmail.com', telefono='567890123', fecha_nacimiento='1997-06-06'),
    Estudiante(nombre='Laura', apellidos='Fernández', correo='laurafernandez@gmail.com', telefono='678901234', fecha_nacimiento='2003-07-07'),
    Estudiante(nombre='Jorge', apellidos='Sánchez', correo='jorgesanchez@gmail.com', telefono='789012345', fecha_nacimiento='1996-08-08'),
    Estudiante(nombre='Elena', apellidos='Díaz', correo='elenadiaz@gmail.com', telefono='890123456', fecha_nacimiento='2004-09-09'),
    Estudiante(nombre='Raúl', apellidos='Moreno', correo='raulmoreno@gmail.com', telefono='901234567', fecha_nacimiento='1995-10-10'),
    Estudiante(nombre='Sofía', apellidos='Romero', correo='sofiaromero@gmail.com', telefono='012345678', fecha_nacimiento='2005-11-11')
]

for e in estudiantes:
    e.save()
    

cursos = [
    Curso(nombre='Python', descripcion='Curso de Python', fecha_inicio='2025-01-01', fecha_fin='2025-02-01', tematica='Python'),
    Curso(nombre='Django', descripcion='Curso de Django', fecha_inicio='2025-02-02', fecha_fin='2025-03-02', tematica='Django'),
    Curso(nombre='JavaScript', descripcion='Curso de JavaScript', fecha_inicio='2025-03-03', fecha_fin='2025-04-03', tematica='JS'),
    Curso(nombre='HTML', descripcion='Curso de HTML', fecha_inicio='2025-04-04', fecha_fin='2025-05-04', tematica='HTML'),
    Curso(nombre='CSS', descripcion='Curso de CSS', fecha_inicio='2025-05-05', fecha_fin='2025-06-05', tematica='CSS'),
    Curso(nombre='React', descripcion='Curso de React', fecha_inicio='2025-06-06', fecha_fin='2025-07-06', tematica='Otros'),
    Curso(nombre='Angular', descripcion='Curso de Angular', fecha_inicio='2025-07-07', fecha_fin='2025-08-07', tematica='Otros'),
    Curso(nombre='Vue', descripcion='Curso de Vue', fecha_inicio='2025-08-08', fecha_fin='2025-09-08', tematica='Otros'),
    Curso(nombre='Node.js', descripcion='Curso de Node.js', fecha_inicio='2025-09-09', fecha_fin='2025-10-09', tematica='Otros'),
    Curso(nombre='Express', descripcion='Curso de Express', fecha_inicio='2025-10-10', fecha_fin='2025-11-10', tematica='Otros'),
    Curso(nombre='MongoDB', descripcion='Curso de MongoDB', fecha_inicio='2025-11-11', fecha_fin='2025-12-11', tematica='Otros'),
    Curso(nombre='SQL', descripcion='Curso de SQL', fecha_inicio='2025-12-12', fecha_fin='2026-01-12', tematica='BD'),
    Curso(nombre='Java', descripcion='Curso de Java', fecha_inicio='2026-01-13', fecha_fin='2026-02-13', tematica='Otros'),
    Curso(nombre='Spring', descripcion='Curso de Spring', fecha_inicio='2026-02-14', fecha_fin='2026-03-14', tematica='Otros'),
    Curso(nombre='Hibernate', descripcion='Curso de Hibernate', fecha_inicio='2026-03-15', fecha_fin='2026-04-15', tematica='Otros'),
    Curso(nombre='C#', descripcion='Curso de C#', fecha_inicio='2026-04-16', fecha_fin='2026-05-16', tematica='Otros'),
    Curso(nombre='ASP.NET', descripcion='Curso de ASP.NET', fecha_inicio='2026-05-17', fecha_fin='2026-06-17', tematica='Otros'),
    Curso(nombre='PHP', descripcion='Curso de PHP', fecha_inicio='2026-06-18', fecha_fin='2026-07-18', tematica='Otros'),
    Curso(nombre='Laravel', descripcion='Curso de Laravel', fecha_inicio='2026-07-19', fecha_fin='2026-08-19', tematica='Otros'),
    Curso(nombre='Ruby', descripcion='Curso de Ruby', fecha_inicio='2026-08-20', fecha_fin='2026-09-20', tematica='Otros'),
    Curso(nombre='Rails', descripcion='Curso de Rails', fecha_inicio='2026-09-21', fecha_fin='2026-10-21', tematica='Otros'),
    Curso(nombre='Go', descripcion='Curso de Go', fecha_inicio='2026-10-22', fecha_fin='2026-11-22', tematica='Otros')
]
    
for c in cursos:
    c.save()


    
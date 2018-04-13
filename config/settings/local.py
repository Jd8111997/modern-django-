from .base import *
SECRET_KEY = env('DJANGO_SECRET_KEY', default='-4%p918aklnn6wo&sq7_1kg2atbu=i!*c+lqztqy+-i#1h40cv')
DEBUG = env.bool('DJANGO_DEBUG', default=True)

Сервис для сокращения ссылок.
Содержит:
1. страница регистрации path('register/', register, name='register'),
2. страница авторизации path('login/', user_login, name='login'),
3. страница сокращения ссылок авторизованного пользователя path('create/', create, name='create'),
4. страница просмотра ссылок авторизованного пользователя path('show/', show, name='show').
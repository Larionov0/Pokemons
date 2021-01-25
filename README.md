# Pokemons

Технические задания - pokeapi

Для запуска:
```
git clone https://github.com/Larionov0/Pokemons/
cd Pokemons

docker-compose up --build
```
Затем переходим http://127.0.0.1:8000/ , и попадаем на страницу авторизации.

---
! в случае запуска на Windows возможна ошибка /usr/src/app/entrypoint.sh: line 17: syntax error: unexpected end of file (expecting "do")

[Тут](https://stackoverflow.com/questions/16239551/eol-conversion-in-notepad#:~:text=From%20the%20%22Edit%22%20menu%2C,%22UNIX%2FOSX%20Format%22.&text=You%20can%20also%20set%20the,OSX%22%20under%20the%20Format%20box.&text=In%20Notepad%2B%2B%2C%20use%20replace%20all%20with%20regular%20expression.) простое решение с помощью Notepad++

---

На сайте доступна регистрация/авторизация,
выбор и удаление покемонов для игры.

Покемоны подтягиваются с сайта https://pokeapi.co/, сохраняясь в базу данных динамично.

Так же доступна API по url http://127.0.0.1:8000/api/v1/get_users/
Возвращает массив всех пользователей и их покемонов.
Доступ к API не ограничен (то есть, не обязательно регистрировать юзера).

Сейчас каждый покемон имеет только id и имя.
По надобности могу добавить умения, или другую информацию, подтянув с ApokeAPI.

---

Проект оставлен в DEBUG режиме для удобной отладки возможных ошибок.

---

Тестами покрыл пока только регистрацию

from aengine_flask.local import settings

if settings.writeGreetingOnImport:
    print("Спасибо за использование AEngine-Flask!")
    print("Фреймворк написан на основе flask")


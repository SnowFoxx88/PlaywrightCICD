##################### Powershell commands#######################
Debugmode:
$env:PWDEBUG=1; pytest -s .\tests\test_ui.py::test_add_task (neue powershell session aufmachen für debug exit)

##################### Run Tests commands#######################
Run all:
uv run pytest -m api; uv run pytest -m ui -n 4 --headed
-n <any number or auto> = starting workers for parallel execution

Run certain tests:
uv run pytest .\tests\test_ui.py::test_add_task


##################### conftext.py#######################

Fixture Injection
1. Die "Suche" (Top-Down)
    a) Test: "Ich brauche pm!"
    b) pm-Fixture: "Ich brauche page, um den PageManager zu erstellen."
    c) page-Fixture: "Ich brauche browser, um einen neuen Context/Page zu öffnen."
    d) browser-Fixture: "Ich brauche sync_playwright, um den Browser zu starten."

2. Der "Aufbau" (Bottom-Up)
 Sobald pytest weiß, was alles nötig ist, wird der Code bis zum jeweiligen yield ausgeführt:
    a) Browser-Ebene: Der Chromium-Browser startet -> Springt zum yield browser.
    b) Page-Ebene: Nutzt den fertigen browser, erstellt context und page -> Springt zum yield page.
    c) PM-Ebene: Nutzt die fertige page, erstellt PageManager(page) -> Springt zum yield PageManager(page).
    d) Test-Ebene: Dein Test erhält das fertige pm-Objekt und fängt an zu laufen.

3. Der "Rückweg" (Teardown)
Nachdem der Test beendet ist (egal ob bestanden oder fehlgeschlagen), geht pytest den Weg rückwärts wieder zurück, um aufzuräumen (alles, was nach den yield-Befehlen steht):
    a) PM-Fixture: (Hier steht nichts nach dem yield, also fertig).
    b)Page-Fixture: Führt context.close() aus (schließt das Tab/den Kontext).
    d)Browser-Fixture: Führt browser.close() aus (beendet den gesamten Browser-Prozess).
\# Отчёт о переписывании истории (задание №5)



\## Команда

git rebase -i HEAD\~2



\## Где выполнялась операция

Операция выполнена в ветке `feature` — перед слиянием в `master`.



\## Операция

\*\*squash\*\* — объединение двух коммитов в один.



Объединены коммиты:

\- "feat: добавлен feature\_module с функцией multiply" (ad5d3e7)

\- "feat: добавлена функция divide в feature\_module" (ce1b1d2)



Новое сообщение: "feat: добавлен feature\_module с функциями multiply и divide" (0dbe8dc)



\## git log --oneline ДО rebase (в ветке feature)

ce1b1d2 (HEAD -> feature) feat: добавлена функция divide в feature\_module

ad5d3e7 feat: добавлен feature\_module с функцией multiply

70b3653 chore: добавлен .gitignore для Python-проекта

aeb4122 feat: добавлены utils.py, test.py, README.md, report.txt

fd1d281 feat: добавлена вторая строка в main.py (второй коммит)

e75ded2 feat: добавлен main.py с приветствием



\## git log --oneline ПОСЛЕ rebase (в ветке feature)

0dbe8dc (HEAD -> feature) feat: добавлен feature\_module с функциями multiply и divide

70b3653 chore: добавлен .gitignore для Python-проекта

aeb4122 feat: добавлены utils.py, test.py, README.md, report.txt

fd1d281 feat: добавлена вторая строка в main.py (второй коммит)

e75ded2 feat: добавлен main.py с приветствием



\## Вывод

Хэши коммитов изменились — старые хэши `ad5d3e7` и `ce1b1d2` пропали,

появился новый коммит `0dbe8dc`. Количество коммитов уменьшилось на 1.

История в ветке `feature` осталась линейной.



Результат операции влит в `master` через merge-коммит (задание №6).

Это позволяет выполнить оба задания: и переписать историю в отдельной ветке,

и сохранить явный merge-коммит в основной ветке.


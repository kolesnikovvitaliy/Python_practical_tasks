from itertools import groupby, chain


tasks = [('Отдых', 'поспать днем', 3),
         ('Ответы на вопросы', 'ответить на вопросы в дискорде', 1),
         ('ЕГЭ Математика', 'доделать курс по параметрам', 1),
         ('Ответы на вопросы', 'ответить на вопросы в курсах', 2),
         ('Отдых', 'погулять вечером', 4),
         ('Курс по ооп', 'обсудить темы', 1),
         ('Урок по groupby', 'добавить задачи на программирование', 3),
         ('Урок по groupby', 'написать конспект', 1),
         ('Отдых', 'погулять днем', 2),
         ('Урок по groupby', 'добавить тестовые задачи', 2),
         ('Уборка', 'убраться в ванной', 2),
         ('Уборка', 'убраться в комнате', 1),
         ('Уборка', 'убраться на кухне', 3),
         ('Отдых', 'погулять утром', 1),
         ('Курс по ооп', 'обсудить задачи', 2)]


key_sort = lambda x: x[0]
tasks.sort(key=key_sort)
groups = groupby(tasks, key=key_sort)
for key, iter_tasks in groups:
    print(f'{key}:\n   ',
          '\n    '.join([f'{i[2]}. {i[1]}' for i in
                         sorted(iter_tasks, key=lambda x: x[2])]))
    print()

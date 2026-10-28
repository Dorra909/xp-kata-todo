# Itération 1 — code "classique" : pas de tests, pas de séparation des responsabilités.
# Volontairement imparfait pour mesurer la dette technique.

tasks = []

def add_task(title, priority="normal", done=False, tags=None):
    # TODO: gérer les titres vides
    # FIXME: pas de validation
    if tags is None:
        tags = []
    tasks.append({"title": title, "priority": priority, "done": done, "tags": tags})
    return True

def list_tasks():
    return tasks

def delete_task(index):
    # FIXME: pas de gestion d'index hors borne
    del tasks[index]

def mark_done(index):
    tasks[index]["done"] = True

def search(keyword):
    # TODO: recherche insensible à la casse
    result = []
    for t in tasks:
        if keyword in t["title"]:
            result.append(t)
    return result

def stats():
    # TODO: calcul de stats
    total = len(tasks)
    done = 0
    for t in tasks:
        if t["done"]:
            done += 1
    return {"total": total, "done": done}
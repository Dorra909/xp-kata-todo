"""Itération 2 — version XP : TDD, refactoring, séparation des responsabilités."""
import unicodedata
from dataclasses import dataclass
from typing import List

MAX_TITLE_LENGTH = 100


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


def _normalize(text: str) -> str:
    """Minuscules + suppression des accents ('cafe' trouve 'Café')."""
    decomposed = unicodedata.normalize("NFD", text)
    without_accents = "".join(c for c in decomposed if not unicodedata.combining(c))
    return without_accents.casefold()


def _validate_title(title: str) -> str:
    if not title or not title.strip():
        raise ValueError("Le titre ne peut pas être vide.")
    title = title.strip()
    if len(title) > MAX_TITLE_LENGTH:
        raise ValueError(
            f"Le titre ne peut pas dépasser {MAX_TITLE_LENGTH} caractères."
        )
    return title


class TodoList:
    """Gestionnaire de tâches avec invariants clairs (testés)."""

    def __init__(self) -> None:
        self._tasks: List[Task] = []
        self._next_id: int = 1  # jamais réutilisé, même après un delete

    def add(self, title: str) -> Task:
        task = Task(id=self._next_id, title=_validate_title(title))
        self._tasks.append(task)
        self._next_id += 1
        return task

    def list(self) -> List[Task]:
        return list(self._tasks)

    def _find(self, task_id: int) -> Task:
        for task in self._tasks:
            if task.id == task_id:
                return task
        raise KeyError(f"Tâche {task_id} introuvable.")

    def delete(self, task_id: int) -> None:
        task = self._find(task_id)
        self._tasks.remove(task)

    def mark_done(self, task_id: int) -> None:
        self._find(task_id).done = True

    def search(self, keyword: str) -> List[Task]:
        kw = _normalize(keyword)
        return [t for t in self._tasks if kw in _normalize(t.title)]

    def stats(self) -> dict:
        total = len(self._tasks)
        done = sum(1 for t in self._tasks if t.done)
        return {"total": total, "done": done}

    # --- Lot B ---
    def filter_by_status(self, done: bool) -> List[Task]:
        return [t for t in self._tasks if t.done is done]

    def edit(self, task_id: int, new_title: str) -> Task:
        task = self._find(task_id)
        task.title = _validate_title(new_title)
        return task

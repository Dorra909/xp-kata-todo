"""Itération 2 — version XP : TDD, refactoring, séparation des responsabilités."""
from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


class TodoList:
    """Gestionnaire de tâches avec invariants clairs (testés)."""

    def __init__(self) -> None:
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add(self, title: str) -> Task:
        if not title or not title.strip():
            raise ValueError("Le titre ne peut pas être vide.")
        task = Task(id=self._next_id, title=title.strip())
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
        kw = keyword.lower()
        return [t for t in self._tasks if kw in t.title.lower()]

    def stats(self) -> dict:
        total = len(self._tasks)
        done = sum(1 for t in self._tasks if t.done)
        return {"total": total, "done": done}
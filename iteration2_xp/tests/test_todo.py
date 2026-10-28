import pytest
from src.todo import TodoList

def test_add_task_returns_task_with_id():
    todo = TodoList()
    task = todo.add("Acheter du pain")
    assert task.id == 1
    assert task.title == "Acheter du pain"
    assert task.done is False

def test_add_empty_title_raises():
    todo = TodoList()
    with pytest.raises(ValueError):
        todo.add("   ")

def test_list_returns_all_tasks():
    todo = TodoList()
    todo.add("A")
    todo.add("B")
    assert len(todo.list()) == 2

def test_delete_removes_task():
    todo = TodoList()
    t = todo.add("A")
    todo.delete(t.id)
    assert len(todo.list()) == 0

def test_delete_unknown_id_raises():
    todo = TodoList()
    with pytest.raises(KeyError):
        todo.delete(999)

def test_mark_done_changes_status():
    todo = TodoList()
    t = todo.add("A")
    todo.mark_done(t.id)
    assert todo.list()[0].done is True

def test_search_case_insensitive():
    todo = TodoList()
    todo.add("Acheter du Pain")
    results = todo.search("pain")
    assert len(results) == 1

def test_stats_counts():
    todo = TodoList()
    t1 = todo.add("A")
    todo.add("B")
    todo.mark_done(t1.id)
    stats = todo.stats()
    assert stats["total"] == 2
    assert stats["done"] == 1
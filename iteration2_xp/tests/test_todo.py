import pytest
from src.todo import TodoList, MAX_TITLE_LENGTH

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

# --- Cas limites ---
def test_add_title_too_long_raises():
    todo = TodoList()
    with pytest.raises(ValueError):
        todo.add("x" * (MAX_TITLE_LENGTH + 1))

def test_add_title_at_limit_is_accepted():
    todo = TodoList()
    assert todo.add("x" * MAX_TITLE_LENGTH).id == 1

def test_mark_done_unknown_id_raises():
    todo = TodoList()
    with pytest.raises(KeyError):
        todo.mark_done(999)

def test_search_on_empty_list_returns_empty():
    assert TodoList().search("anything") == []

def test_stats_on_empty_list():
    assert TodoList().stats() == {"total": 0, "done": 0}

def test_add_duplicate_titles_get_different_ids():
    todo = TodoList()
    a = todo.add("Same")
    b = todo.add("Same")
    assert (a.id, b.id) == (1, 2)

def test_search_ignores_accents():
    todo = TodoList()
    todo.add("Café")
    assert len(todo.search("cafe")) == 1


# --- Lot B ---
def test_filter_by_status_on_empty_list():
    assert TodoList().filter_by_status(done=True) == []

def test_filter_by_status_returns_matching_tasks():
    todo = TodoList()
    a = todo.add("A")
    todo.add("B")
    todo.mark_done(a.id)
    assert [t.title for t in todo.filter_by_status(done=True)] == ["A"]
    assert [t.title for t in todo.filter_by_status(done=False)] == ["B"]

def test_edit_unknown_id_raises():
    todo = TodoList()
    with pytest.raises(KeyError):
        todo.edit(999, "New title")

def test_edit_changes_title():
    todo = TodoList()
    t = todo.add("Old")
    todo.edit(t.id, "  New  ")
    assert todo.list()[0].title == "New"

def test_edit_with_empty_title_raises():
    todo = TodoList()
    t = todo.add("Old")
    with pytest.raises(ValueError):
        todo.edit(t.id, "   ")

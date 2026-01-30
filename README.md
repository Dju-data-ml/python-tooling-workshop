# Step 03: Implémentation des classes

## Objectif

Implémenter les classes `Task` et `TaskManager` en appliquant les principes de la POO.

## Installation des dépendances

```bash
# Avec UV (recommandé)
uv sync

# Ou méthode classique
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

## Architecture

```
src/
├── models/
│   └── task.py          # Modèle de données Task
└── services/
    └── task_manager.py  # Logique métier TaskManager
```

## 📦 Classe Task (models/task.py)

### Utilisation de dataclass

```python
from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    description: str
    status: TaskStatus
    created_at: datetime
```

**Pourquoi `@dataclass` ?**

Imaginez que vous voulez créer une classe pour représenter une personne :

**Sans `@dataclass` (la longue méthode) :**
```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
    
    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age
```

**Avec `@dataclass` (la méthode simple) :**
```python
@dataclass
class Person:
    name: str
    age: int
```

**Ce que `@dataclass` fait automatiquement :**
- Crée le constructeur `__init__` pour vous
- Crée une représentation lisible `__repr__` 
- Crée la comparaison `__eq__` (pour savoir si deux objets sont identiques)
- Ajoute les types pour aider l'éditeur de code
- Évite d'écrire du code répétitif
- Optionnel : peut rendre l'objet non-modifiable avec `frozen=True`

**Résultat :** Moins de code à écrire, moins d'erreurs, et plus facile à lire !

### Utilisation d'Enum

```python
class TaskStatus(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"
```

**Pourquoi une Enum ?**
- Valeurs prédéfinies (pas de "typo" possible)
- Autocomplétion dans l'IDE
- Comparaison type-safe
- Itération sur toutes les valeurs possibles

**Mauvaise approche :**
```python
# ❌ Utiliser des strings directement
status = "in_progress"  # Typo possible : "in_progres"
```

**Bonne approche :**
```python
# ✅ Utiliser l'Enum
status = TaskStatus.IN_PROGRESS  # Autocomplétion + validation
```

### Méthodes métier

```python
def mark_done(self) -> None:
    """Mark the task as completed."""
    self.status = TaskStatus.DONE
```

**Principe :** Encapsuler la logique métier dans la classe.

**Avantages :**
- Le code qui utilise `Task` n'a pas besoin de connaître `TaskStatus`
- On peut ajouter de la validation ou des effets de bord
- API plus claire : `task.mark_done()` vs `task.status = TaskStatus.DONE`

## 🔧 Classe TaskManager (services/task_manager.py)

### Responsabilité unique

Le `TaskManager` gère **une collection de tasks**.

**Ce qu'il fait :**
- CRUD sur les tasks (Create, Read, Update, Delete)
- Génération d'IDs uniques
- Filtrage par statut

**Ce qu'il ne fait PAS :**
- ❌ Affichage (rôle de la CLI)
- ❌ Persistance fichier/BDD (rôle d'un Repository)
- ❌ Validation complexe (rôle de la classe Task)

### Gestion de la liste de tasks

```python
def __init__(self) -> None:
    self._tasks: List[Task] = []  # Attribut privé
    self._next_id: int = 1
```

**Pourquoi `_tasks` avec underscore ?**
- Convention Python : attribut "privé" (pas réellement privé, mais signal)
- Évite l'accès direct depuis l'extérieur
- Force à passer par les méthodes publiques

**Exemple d'utilisation correcte :**
```python
# ✅ Bon
manager = TaskManager()
tasks = manager.list_tasks()

# ❌ Mauvais (mais techniquement possible)
tasks = manager._tasks  # Brise l'encapsulation
```

### Type hints et Optional

```python
def get_task(self, task_id: int) -> Optional[Task]:
    ...
    return None  # Si pas trouvé
```

**`Optional[Task]` signifie :** "Retourne soit un `Task`, soit `None`"

Équivalent à : `Task | None` (Python 3.10+)

**Pourquoi c'est important ?**
```python
task = manager.get_task(999)
if task is not None:
    print(task.title)  # ✅ Safe, on a vérifié
else:
    print("Task not found")
```

Sans le type hint, l'IDE ne peut pas nous aider à détecter ce cas.

### Méthodes de filtrage

```python
def list_tasks(self, status: Optional[TaskStatus] = None) -> List[Task]:
    if status is None:
        return self._tasks.copy()  # Toutes les tasks
    
    return [task for task in self._tasks if task.status == status]
```

**List comprehension :** Syntaxe Python concise pour filtrer/transformer.

**Équivalent avec boucle classique :**
```python
result = []
for task in self._tasks:
    if task.status == status:
        result.append(task)
return result
```

## 🧪 Tester le code

### En Python REPL

```python
# Lancer Python depuis la racine du projet
python

>>> from src.models.task import Task, TaskStatus
>>> from src.services.task_manager import TaskManager
>>> from datetime import datetime

# Créer un manager
>>> manager = TaskManager()

# Ajouter des tasks
>>> task1 = manager.add_task("Learn Python", "Complete the workshop")
>>> task2 = manager.add_task("Build API", "Create FastAPI service")

# Lister les tasks
>>> tasks = manager.list_tasks()
>>> for task in tasks:
...     print(task)
Task #1: Learn Python [todo]
Task #2: Build API [todo]

# Changer un statut
>>> task1.mark_in_progress()
>>> print(task1)
Task #1: Learn Python [in_progress]

# Filtrer par statut
>>> in_progress = manager.list_tasks(TaskStatus.IN_PROGRESS)
>>> print(len(in_progress))
1

# Supprimer une task
>>> manager.delete_task(2)
True
>>> print(manager.count_tasks())
1
```

### Script de test manuel

Créez `test_manual.py` à la racine :

```python
from src.models.task import TaskStatus
from src.services.task_manager import TaskManager

# Créer un manager
manager = TaskManager()

# Ajouter quelques tasks
print("📝 Adding tasks...")
t1 = manager.add_task("Learn Python", "Complete tooling workshop")
t2 = manager.add_task("Build API", "Create FastAPI service")
t3 = manager.add_task("Deploy", "Deploy to production")

print(f"✅ {manager.count_tasks()} tasks created")

# Afficher toutes les tasks
print("\n📋 All tasks:")
for task in manager.list_tasks():
    print(f"  - {task}")

# Changer des statuts
print("\n🔄 Updating statuses...")
t1.mark_in_progress()
t2.mark_done()

# Afficher par statut
print(f"\n✅ Done: {manager.count_by_status(TaskStatus.DONE)}")
print(f"🚧 In Progress: {manager.count_by_status(TaskStatus.IN_PROGRESS)}")
print(f"📌 Todo: {manager.count_by_status(TaskStatus.TODO)}")
```

Lancez-le :
```bash
python test_manual.py
```

## 💡 Concepts POO appliqués

### Encapsulation
- Données (`_tasks`) cachées derrière une API publique
- Pas d'accès direct à la liste

### Abstraction
- Les utilisateurs du `TaskManager` ne voient que les méthodes publiques
- L'implémentation interne (liste, dict, BDD...) peut changer

### Cohésion
- `Task` : Représenter une tâche
- `TaskManager` : Gérer un ensemble de tâches
- Chaque classe a une responsabilité claire

### Composition
- `TaskManager` **contient** des `Task` (relation has-a)
- Pas d'héritage (relation is-a) car pas nécessaire ici

## Points de validation

- [ ] `task.py` créé avec `Task` et `TaskStatus`
- [ ] `task_manager.py` créé avec `TaskManager`
- [ ] Le code s'importe sans erreur
- [ ] Test manuel dans REPL fonctionne
- [ ] Vous comprenez le rôle de chaque classe

## 📚 Pour aller plus loin

### Type hints avancés

```python
from typing import Dict, Set, Tuple

# Dict avec types pour clés et valeurs
tasks_by_id: Dict[int, Task] = {}

# Set d'IDs uniques
completed_ids: Set[int] = {1, 3, 5}

# Tuple de taille fixe
stats: Tuple[int, int, int] = (5, 3, 2)  # (total, done, in_progress)
```

### Dataclass avancé

```python
from dataclasses import dataclass, field

@dataclass
class Task:
    id: int
    title: str
    tags: List[str] = field(default_factory=list)  # Valeur par défaut mutable
    frozen: bool = field(default=False, repr=False)  # Exclu du __repr__
```

### Property decorator

```python
class TaskManager:
    @property
    def total_tasks(self) -> int:
        """Expose count as a read-only property."""
        return len(self._tasks)

# Utilisation
manager = TaskManager()
print(manager.total_tasks)  # Comme un attribut, mais c'est une méthode
```

## 💾 Commit

```bash
git add src/
git commit -m "feat: implement Task and TaskManager classes"
```

## Prochaine étape

→ **Step 04: Linting avec Ruff**

Vous allez configurer Ruff pour détecter automatiquement les problèmes dans le code.

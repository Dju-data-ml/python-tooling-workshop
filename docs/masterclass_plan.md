# Masterclass: Toolings & Python Best Practices
## Formation ML Engineer - Sprint 1, Jour 7

**Format:** Workshop interactif avec live coding  
**Objectif:** Donner aux apprenants les outils et pratiques pour écrire du code Python production-ready

## Objectifs pédagogiques

À la fin de cette masterclass, les apprenants doivent pouvoir:
1. Structurer un projet Python modulaire et maintenable
2. Utiliser les outils modernes de qualité de code (linting, formatting)
3. Gérer proprement les dépendances et environnements virtuels
4. Appliquer un workflow Git professionnel avec branches et PRs
5. Comprendre la différence entre du code "exploration" et du code "production"

## Prérequis

- Compte GitHub créé
- Notions de base Python (Sprint 1 complété)
- Accès à GitHub Codespaces

## Programme détaillé

### Phase 0: Introduction

**Contenu:**
- Présentation du contexte: "Pourquoi on ne code pas en production comme dans un notebook?"
- Vue d'ensemble du projet fil rouge: un Task Manager CLI
- Démonstration du résultat final (branche `main`)
- Explication du format workshop: branches progressives qu'ils vont reproduire

**Action:**
- Les apprenants forkent le repo template
- Lancent leur Codespace
- Vérifient que l'environnement fonctionne

### Phase 1: Structure de projet Python

**Objectif:** Comprendre comment organiser du code Python modulaire

**Démonstration live:**
```
project/
├── README.md
├── .gitignore
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_manager.py
│   └── cli/
│       ├── __init__.py
│       └── main.py
└── tests/
    └── __init__.py
```

**Concepts clés:**
- `src/` pour le code source
- Séparation models / services / cli (architecture en couches)
- `__init__.py` et le concept de package Python
- `if __name__ == "__main__":` vs code importable
- `.gitignore` adapté à Python

**Pratique:**
- Checkout de `step-01-structure`
- Les apprenants reproduisent la structure
- Créent les fichiers vides
- Premier commit: "feat: initial project structure"

**Points d'attention:**
- Expliquer pourquoi on sépare les responsabilités
- Montrer comment importer depuis `src.models.task`
- Insister sur le fait que cette structure sera réutilisée dans Docker, FastAPI, etc.

### Phase 2: Environnements virtuels et dépendances

**Objectif:** Gérer proprement les dépendances Python

**Démonstration live:**

1. **Création d'un venv:**
```bash
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate sur Windows
```

2. **Installation et freeze:**
```bash
pip install rich click
pip freeze > requirements.txt
```

3. **Pourquoi c'est important:**
   - Isolation des dépendances
   - Reproductibilité
   - Préparation à Docker

**Pratique:**
- Checkout de `step-02-dependencies`
- Création de leur venv
- Installation des dépendances du projet (rich pour CLI stylé, click pour arguments)
- Commit: "feat: add project dependencies"

**Concepts clés:**
- `requirements.txt` vs `pyproject.toml` (mention rapide)
- Pourquoi le venv n'est pas commité (`.gitignore`)
- Comment quelqu'un d'autre reproduit l'environnement

### Phase 3: Code fonctionnel

**Objectif:** Implémenter les classes de base avec la POO

**Démonstration live:**

**`src/models/task.py`:**
```python
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class TaskStatus(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

@dataclass
class Task:
    id: int
    title: str
    description: str
    status: TaskStatus
    created_at: datetime
    
    def mark_done(self):
        self.status = TaskStatus.DONE
```

**`src/services/task_manager.py`:**
```python
from typing import List
from src.models.task import Task, TaskStatus

class TaskManager:
    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id = 1
    
    def add_task(self, title: str, description: str) -> Task:
        # Implémentation
        pass
    
    def list_tasks(self, status: TaskStatus = None) -> List[Task]:
        # Implémentation
        pass
```

**Pratique:**
- Checkout de `step-03-implementation`
- Implémentation des méthodes
- Test manuel dans Python REPL
- Commit: "feat: implement Task and TaskManager"

### PAUSE

### Phase 4: Linting et qualité de code

**Objectif:** Détecter automatiquement les problèmes de code

**Démonstration live:**

1. **Installation de Ruff:**
```bash
pip install ruff
```

2. **Configuration `pyproject.toml`:**
```toml
[tool.ruff]
line-length = 100
select = ["E", "F", "I", "N", "W"]
ignore = []

[tool.ruff.lint]
fixable = ["ALL"]
```

3. **Utilisation:**
```bash
ruff check src/
ruff check --fix src/  # Auto-fix
```

**Concepts clés:**
- Qu'est-ce que le linting? (analyse statique)
- Types d'erreurs détectées: imports inutilisés, variables non utilisées, complexité, etc.
- Auto-fix vs erreurs à corriger manuellement
- Configuration de projet vs configuration personnelle

**Pratique:**
- Checkout de `step-04-linting`
- Ajout du fichier `pyproject.toml`
- Lancement du linter sur leur code
- Correction des erreurs détectées
- Commit: "chore: add ruff linting configuration"

**Démo bonus:**
- Montrer VSCode extension Ruff (linting en temps réel)
- Shortcuts pour auto-fix

### Phase 5: Formatage automatique

**Objectif:** Uniformiser le style de code automatiquement

**Démonstration live:**

1. **Ruff comme formatteur:**
```bash
ruff format src/
```

2. **Configuration dans `pyproject.toml`:**
```toml
[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

3. **Avant/Après:**
   - Montrer du code mal formaté
   - Lancer `ruff format`
   - Constater les changements automatiques

**Pratique:**
- Checkout de `step-05-formatting`
- Désorganiser volontairement le formatage de leur code
- Lancer le formatteur
- Observer les changements
- Commit: "style: apply ruff formatting"

**Concepts clés:**
- Séparation linting (logique) vs formatting (style)
- Pourquoi le formatage auto évite les débats stériles
- Intégration dans l'éditeur (format on save)

### Phase 6: Git workflow professionnel

**Objectif:** Appliquer un workflow Git réaliste avec branches et PR

**Démonstration live:**

1. **Workflow de feature branch:**
```bash
git checkout -b feature/add-delete-task
# ... modifications ...
git add .
git commit -m "feat: add delete task functionality"
git push origin feature/add-delete-task
```

2. **Création d'une Pull Request sur GitHub:**
   - Title clair
   - Description du changement
   - Review du diff
   - Merge dans main

3. **Convention de commits:**
   - `feat:` pour nouvelle fonctionnalité
   - `fix:` pour correction de bug
   - `chore:` pour tâches techniques
   - `docs:` pour documentation
   - `style:` pour formatage

**Pratique:**
- Checkout de `step-06-git-workflow`
- Créer une branche pour une nouvelle feature (ex: filtrer par statut)
- Implémenter la feature
- Commit avec convention
- Push et création de PR
- Review et merge

**Concepts clés:**
- Pourquoi ne jamais commiter directement sur main
- Comment organiser ses commits (atomiques et logiques)
- L'importance des messages de commit clairs
- Préparation au GitFlow (Sprint 6)

### Phase 7: CLI et point d'entrée

**Objectif:** Créer une interface utilisateur en ligne de commande

**Démonstration live:**

**`src/cli/main.py`:**
```python
import click
from rich.console import Console
from rich.table import Table
from src.services.task_manager import TaskManager

console = Console()
manager = TaskManager()

@click.group()
def cli():
    """Task Manager CLI"""
    pass

@cli.command()
@click.argument('title')
@click.argument('description')
def add(title: str, description: str):
    """Add a new task"""
    task = manager.add_task(title, description)
    console.print(f"[green]Task created:[/green] {task.title}")

@cli.command()
def list():
    """List all tasks"""
    tasks = manager.list_tasks()
    
    table = Table(title="Tasks")
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="magenta")
    table.add_column("Status", style="green")
    
    for task in tasks:
        table.add_row(str(task.id), task.title, task.status.value)
    
    console.print(table)

if __name__ == "__main__":
    cli()
```

**Pratique:**
- Checkout de `step-07-cli`
- Implémentation du CLI
- Test: `python -m src.cli.main add "Learn Python" "Complete masterclass"`
- Commit: "feat: add CLI interface"

### Phase 8: Tests unitaires (optionnel si temps)

**Objectif:** Introduire pytest pour valider le code

**Démonstration live:**

**`tests/test_task_manager.py`:**
```python
import pytest
from src.models.task import Task, TaskStatus
from src.services.task_manager import TaskManager

def test_add_task():
    manager = TaskManager()
    task = manager.add_task("Test", "Description")
    
    assert task.id == 1
    assert task.title == "Test"
    assert task.status == TaskStatus.TODO

def test_list_tasks():
    manager = TaskManager()
    manager.add_task("Task 1", "Desc 1")
    manager.add_task("Task 2", "Desc 2")
    
    tasks = manager.list_tasks()
    assert len(tasks) == 2
```

**Lancement:**
```bash
pip install pytest
pytest tests/ -v
```

**Pratique:**
- Checkout de `step-08-tests`
- Écrire 2-3 tests simples
- Lancer pytest
- Commit: "test: add unit tests for TaskManager"

### Conclusion et ressources

**Récapitulatif:**
- Ce qu'on a vu: structure, dépendances, qualité, Git, CLI, tests
- Comment ces pratiques vont servir dans les sprints suivants:
  - Sprint 2 (SQL): structure de projet pour accès BDD
  - Sprint 4 (API): FastAPI avec cette même structure
  - Sprint 5 (Docker): Dockerfile qui utilise requirements.txt
  - Sprint 6 (Git): GitFlow et CI/CD
  - Sprint 7+ (LLM/Agents): code production-ready pour agents

**Ressources:**
- Documentation Ruff: https://docs.astral.sh/ruff/
- Guide pytest: https://docs.pytest.org/
- Conventional Commits: https://www.conventionalcommits.org/
- Real Python - Project Structure: https://realpython.com/python-application-layouts/

**Next steps:**
- Garder ces pratiques pour tous leurs projets
- Le repo template est disponible pour leurs futurs projets
- Questions/Réponses

## Livrables

**Pour les apprenants:**
- Repo GitHub forké avec toutes les branches
- Projet fonctionnel sur leur Codespace
- Au moins 1 PR créée et mergée
- Environnement configuré (linting + formatting)

## Points d'attention formateur

**Pièges classiques:**
- Oublier d'activer le venv, ce qui fait échouer les imports
- Confondre `src.models` et `models` dans les imports
- Faire des commits trop gros ou avec des messages vagues
- Ne pas tester le code avant de commiter

**Adaptations possibles:**
- Si le groupe est rapide: ajouter la phase sur les tests
- Si le groupe est lent: sauter le CLI et rester sur le REPL
- En cas de problèmes techniques: avoir un Codespace de secours déjà configuré

**Énergie de la séance:**
- Alterner démos et pratique pour maintenir l'attention
- Faire des pauses de 2-3 minutes entre chaque phase si nécessaire
- Encourager l'entraide entre les apprenants
- Débugger en direct quand c'est nécessaire - c'est formateur

## Liens utiles

- Repo du workshop: `https://github.com/[username]/python-tooling-workshop`
- Documentation du projet: voir README.md du repo
- Support Slack/Discord pour questions post-masterclass

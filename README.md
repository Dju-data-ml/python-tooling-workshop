# Step 07: CLI avec Rich et Click

## Objectif

Créer une interface en ligne de commande interactive et professionnelle pour notre Task Manager.

## Installation des dépendances

```bash
# Avec UV (recommandé)
uv sync

# Ou méthode classique
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```


## Architecture finale

```
src/
├── models/
│   └── task.py          # Modèle Task et TaskStatus
├── services/
│   └── task_manager.py  # Logique métier TaskManager
└── cli/
    └── main.py          # Interface CLI avec Rich/Click
```

## Rich vs Click

| Composant | Rôle | Exemple |
|-----------|------|---------|
| **Rich** | Affichage stylé | Tableaux, couleurs, progress bars |
| **Click** | Structure CLI | Commandes, arguments, options |

Les deux travaillent ensemble :
- Click structure la commande (`add`, `list`, etc.)
- Rich rend l'affichage beau et lisible

## Commandes de la CLI

```bash
# Ajouter une tâche
uv run python -m src.cli.main add "Apprendre Python" "Compléter le workshop"

# Lister toutes les tâches
uv run python -m src.cli.main list

# Marquer une tâche comme terminée
uv run python -m src.cli.main done 1

# Supprimer une tâche
uv run python -m src.cli.main delete 1
```

### Structure du code (cli/main.py)

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

## À reproduire

### 1. Créer le fichier CLI

```bash
touch src/cli/main.py
```

### 2. Implémenter les commandes de base

- `add` : Ajouter une tâche
- `list` : Lister les tâches avec un tableau Rich
- `done` : Marquer comme terminée
- `delete` : Supprimer une tâche

### 3. Persistance automatique

**Les tâches sont sauvegardées automatiquement dans `tasks.json` !**

Vos tâches persistent entre les exécutions grâce à la sauvegarde JSON.

### 4. Tester l'interface

```bash
# Ajouter une tâche
uv run python -m src.cli.main add "Apprendre Python" "Compléter le workshop"

# Lister - la tâche est toujours là !
uv run python -m src.cli.main list

# Ajouter une autre tâche
uv run python -m src.cli.main add "Build API" "Créer une API REST"

# Lister à nouveau - les deux tâches sont là
uv run python -m src.cli.main list
```

### 5. Améliorations optionnelles

- Filtrage par statut
- Recherche dans les titres
- Export vers JSON/CSV
- Commandes d'aide détaillées
- Mode interactif

## Points de validation

- [ ] `src/cli/main.py` créé avec structure Click
- [ ] Commandes `add` et `list` fonctionnelles
- [ ] Tableau Rich s'affiche correctement
- [ ] CLI peut être lancée avec `python -m src.cli.main`
- [ ] Messages d'erreur clairs

## Commit

```bash
git add src/cli/main.py
git commit -m "feat: add CLI interface with Rich and Click"
```

## Prochaine étape

→ **Step 08: Tests unitaires avec pytest**

Vous allez écrire des tests pour valider le fonctionnement de votre Task Manager.

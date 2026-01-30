# Step 05: Formatage automatique avec Ruff

## Objectif

Uniformiser automatiquement le style de code avec le formatteur Ruff.

## Installation des dépendances

```bash
# Avec UV (recommandé)
uv sync

# Ou méthode classique
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

## Utilisation de Ruff Format

```bash
# Avec UV
uv run ruff format .
uv run ruff format src/

# Ou si venv activé
ruff format .
ruff format src/
```

## Linting vs Formatting

| Aspect | Linting | Formatting |
|--------|---------|------------|
| **Objectif** | Détecter les erreurs logiques | Uniformiser le style visuel |
| **Exemples** | Variables non utilisées, imports manquants | Espaces, indentation, quotes |
| **Action** | Signale des problèmes | Modifie le code automatiquement |
| **Impact** | Peut affecter le comportement | N'affecte jamais le comportement |

**En résumé :**
- **Linting** : "Ton code a des problèmes" 🐛
- **Formatting** : "Ton code est moche" ✨

## 🚀 Utilisation de Ruff Format

### Formater du code

```bash
# Formater tout le projet
ruff format .

# Formater un dossier spécifique
ruff format src/

# Voir ce qui serait modifié sans changer
ruff format --check src/

# Afficher les différences
ruff format --diff src/
```

### Différence avec Black

Ruff Format est compatible avec Black :
- Même résultat de formatage
- Mais 10-100x plus rapide
- Configuration dans `pyproject.toml` (déjà fait au step 04)

## 📐 Règles de formatage

### 1. Longueur de ligne

```python
# ❌ Avant (> 100 caractères)
def create_task(title, description, status, priority, tags, assignee, due_date, created_at, updated_at):
    pass

# ✅ Après
def create_task(
    title,
    description,
    status,
    priority,
    tags,
    assignee,
    due_date,
    created_at,
    updated_at,
):
    pass
```

### 2. Guillemets (quotes)

Configuration dans `pyproject.toml` :
```toml
[tool.ruff.format]
quote-style = "double"  # " au lieu de '
```

```python
# ❌ Avant
task = 'Learn Python'
status = 'todo'

# ✅ Après
task = "Learn Python"
status = "todo"
```

**Pourquoi double quotes ?**
- Convention majoritaire en Python moderne
- Évite les conflits avec apostrophes : `"don't"` vs `'don\'t'`
- Cohérence avec JSON

### 3. Trailing commas

```python
# ❌ Avant
tasks = [
    task1,
    task2
]

# ✅ Après
tasks = [
    task1,
    task2,  # Trailing comma
]
```

**Avantages :**
- Diffs Git plus propres
- Facilite l'ajout d'éléments
- Évite les erreurs de syntaxe

### 4. Espaces autour des opérateurs

```python
# ❌ Avant
result=a+b*c

# ✅ Après
result = a + b * c
```

### 5. Imports organisés

Bien que géré par le linter, le formatteur respecte l'organisation :

```python
# ✅ Bon ordre et espacement
import os
import sys

from datetime import datetime

from src.models.task import Task
```

## Exercice pratique

### 1. Créer un fichier mal formaté

Créez `messy_code.py` :

```python
# Formatage inconsistant volontaire
from src.models.task import Task,TaskStatus
from datetime import datetime,timedelta
import os,sys

class   TaskService:
    def __init__(self,manager):
        self.manager=manager
    
    def process(self,task_id,force=False,verbose=True,retry_count=3,timeout=60):
        tasks=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        result={'status':'ok','count':len(tasks)}
        return result
```

### 2. Vérifier les différences

```bash
ruff format --diff messy_code.py
```

Vous verrez tout ce qui va changer.

### 3. Appliquer le formatage

```bash
ruff format messy_code.py
```

### 4. Comparer le résultat

Le fichier devrait maintenant ressembler à :

```python
# Formatage cohérent et propre
import os
import sys
from datetime import datetime, timedelta

from src.models.task import Task, TaskStatus


class TaskService:
    def __init__(self, manager):
        self.manager = manager

    def process(
        self,
        task_id,
        force=False,
        verbose=True,
        retry_count=3,
        timeout=60,
    ):
        tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        result = {"status": "ok", "count": len(tasks)}
        return result
```

### 5. Formater tout le projet

```bash
ruff format src/
```

## 🎯 Workflow recommandé

### En développement

1. **Écrire du code** (sans se soucier du formatage)
2. **Sauvegarder** → Format automatique (si configuré dans VSCode)
3. **Commit** après vérification

### Avant un commit

```bash
# 1. Formater
ruff format src/

# 2. Linter
ruff check src/

# 3. Si tout est bon
git add .
git commit -m "feat: add new feature"
```

## ⚙️ Configuration VSCode

Ajoutez à `.vscode/settings.json` :

```json
{
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.formatOnPaste": true
  }
}
```

**Résultat :**
- ✨ Formatage automatique à chaque sauvegarde
- ✨ Formatage au collage de code
- ✨ Zéro effort mental sur le style

## 🔥 Pre-commit hook (avancé)

Pour formater automatiquement avant chaque commit :

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.15
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
```

Installation :
```bash
pip install pre-commit
pre-commit install
```

À chaque `git commit`, le code sera formaté et linté automatiquement.

## 💡 Pourquoi le formatage automatique ?

### Avantages

1. **Zéro débat d'équipe**
   - Fini les "tabs vs spaces"
   - Fini les "simple vs double quotes"
   - Le formatteur décide, point final

2. **Code reviews plus efficaces**
   - Focus sur la logique, pas le style
   - Diffs Git minimalistes
   - Pas de commentaires "ajoute un espace ici"

3. **Productivité**
   - Pas besoin de réfléchir au formatage
   - Lecture de code plus rapide (style uniforme)
   - Onboarding plus simple

4. **Préparation à la prod**
   - Style cohérent = code plus maintenable
   - Facilite les outils d'analyse statique
   - Standard dans l'industrie

### Inconvénients ?

- Perte de "liberté créative" → mais c'est le but !
- Parfois le résultat n'est pas "optimal" → rare, et peu important

## 📚 Comparaison des formatteurs Python

| Outil | Vitesse | Personnalisation | Adoption |
|-------|---------|------------------|----------|
| **Ruff Format** | 🚀🚀🚀 | Limitée (volontaire) | 📈 Croissante |
| Black | 🚀 | Presque aucune | ⭐⭐⭐ Standard |
| autopep8 | 🐌 | Haute | ⭐⭐ Ancien |
| YAPF | 🐌 | Très haute | ⭐ Niche |

**Notre choix : Ruff Format**
- Compatible Black (pas de migration)
- Ultra-rapide (important sur gros projets)
- Un seul outil pour linting + formatting

## Points de validation

- [ ] Vous avez formaté le code avec `ruff format`
- [ ] Vous comprenez la différence linting/formatting
- [ ] VSCode configuré pour format-on-save (optionnel)
- [ ] Le code suit un style uniforme

## 🎭 Philosophie du formatage

> "Code is read much more often than it is written."
> — Guido van Rossum, créateur de Python

Le formatage automatique n'est pas une contrainte, c'est une libération :
- Plus besoin de réfléchir au style
- Plus d'énergie pour la logique métier
- Équipe alignée par défaut

## 💾 Commit

```bash
git add .
git commit -m "style: apply ruff formatting to all code"
```

## Prochaine étape

→ **Step 06: Workflow Git professionnel**

Vous allez apprendre à travailler avec des branches et des pull requests.

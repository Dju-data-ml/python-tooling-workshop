# Step 04: Linting avec Ruff

## Objectif

Configurer Ruff pour détecter automatiquement les problèmes de code.

## Installation des dépendances

```bash
# Avec UV (recommandé) - installe aussi ruff en dev dependency
uv sync

# Ou méthode classique
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

## Utilisation de Ruff

```bash
# Avec UV
uv run ruff check src/
uv run ruff check --fix src/

# Ou si venv activé
ruff check src/
ruff check --fix src/
```

## Qu'est-ce que le linting ?

Le **linting** est l'analyse statique du code pour détecter :
- 🐛 **Erreurs** : Variables non utilisées, imports manquants
- ⚠️ **Warnings** : Code suspect, mauvaises pratiques
- 📏 **Style** : Non-respect des conventions PEP 8
- 🧹 **Code smell** : Code complexe, redondant

**Différence avec les tests :**
- Tests : Vérifient que le code **fait** ce qu'il doit faire
- Linting : Vérifie que le code est **écrit** correctement

## 🚀 Pourquoi Ruff ?

### Comparaison des outils

| Outil | Vitesse | Fonctionnalités | Popularité |
|-------|---------|-----------------|------------|
| **Ruff** | 🚀🚀🚀 Ultra-rapide (Rust) | Linting + Formatting | ⭐ Montant |
| Flake8 | 🐌 Lent (Python) | Linting uniquement | ⭐⭐⭐ Établi |
| Pylint | 🐌🐌 Très lent | Très complet mais lourd | ⭐⭐ Ancien |
| Black | 🚀 Rapide | Formatting uniquement | ⭐⭐⭐ Standard |

**Notre choix : Ruff**
- ✅ 10-100x plus rapide que les alternatives
- ✅ Remplace Flake8 + isort + plusieurs plugins
- ✅ Compatible avec Black
- ✅ Auto-fix intégré
- ✅ Utilisé par des projets majeurs (FastAPI, Pydantic...)

## 📝 Configuration (pyproject.toml)

### Structure du fichier

```toml
[tool.ruff]
line-length = 100
target-version = "py310"

[tool.ruff.lint]
select = ["E", "F", "I", ...]
ignore = ["E501"]

[tool.ruff.format]
quote-style = "double"
```

### Sections principales

#### 1. Configuration générale

```toml
[tool.ruff]
line-length = 100        # Longueur max des lignes
target-version = "py310"  # Version Python cible
```

**Pourquoi 100 caractères ?**
- Compromis entre lisibilité et productivité
- PEP 8 suggère 79, mais trop strict pour le code moderne
- Black (le formatteur standard) utilise 88
- 100 est un bon équilibre

#### 2. Règles de linting

```toml
[tool.ruff.lint]
select = [
    "E",   # pycodestyle errors
    "F",   # pyflakes
    "I",   # isort
    "N",   # pep8-naming
]
```

**Catégories de règles :**

| Code | Nom | Exemples de détection |
|------|-----|------------------------|
| **E** | pycodestyle errors | Espaces, indentation, lignes vides |
| **W** | pycodestyle warnings | Imports inutiles, trailing whitespace |
| **F** | pyflakes | Variables non utilisées, imports redondants |
| **I** | isort | Ordre des imports |
| **N** | pep8-naming | Noms de variables/fonctions/classes |
| **UP** | pyupgrade | Syntaxe obsolète (ex: `List[str]` → `list[str]`) |
| **B** | flake8-bugbear | Bugs classiques Python |
| **SIM** | flake8-simplify | Code simplifiable |

#### 3. Règles ignorées

```toml
ignore = [
    "E501",  # Line too long (géré par le formatteur)
]
```

Certaines règles sont redondantes avec le formatteur.

#### 4. Exceptions par fichier

```toml
[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401"]  # Autoriser imports non utilisés
```

Les `__init__.py` réexportent souvent des imports.

## 🏗️ Utilisation

### Installation

```bash
pip install ruff
```

### Vérifier le code

```bash
# Linter tout le projet
ruff check .

# Linter un dossier spécifique
ruff check src/

# Linter un fichier
ruff check src/models/task.py
```

### Auto-fix

```bash
# Corriger automatiquement ce qui est possible
ruff check --fix src/

# Voir ce qui serait corrigé sans modifier
ruff check --fix --diff src/
```

### Afficher les règles violées

```bash
# Mode verbeux avec explication
ruff check --output-format=full src/

# Avec liens vers la doc des règles
ruff check --output-format=github src/
```

## 🐛 Exemples de détection

### 1. Variable non utilisée (F841)

```python
# ❌ Avant
def add_task(title, description):
    task_id = generate_id()  # Variable jamais utilisée !
    return create_task(title, description)
```

```bash
$ ruff check
src/services/task_manager.py:5:5: F841 Local variable `task_id` is assigned to but never used
```

**Fix :**
```python
# ✅ Après
def add_task(title, description):
    return create_task(title, description)
```

### 2. Import non utilisé (F401)

```python
# ❌ Avant
from datetime import datetime, timedelta  # timedelta pas utilisé
from typing import List

def get_tasks() -> List:
    ...
```

```bash
$ ruff check --fix src/
- from datetime import datetime, timedelta
+ from datetime import datetime
```

### 3. Ordre des imports (I001)

```python
# Avant
from src.models.task import Task
from datetime import datetime
import os
```

Ruff auto-fixe :
```python
# ✅ Après
import os
from datetime import datetime

from src.models.task import Task
```

**Ordre standard :**
1. Bibliothèque standard (`os`, `sys`...)
2. Bibliothèques tierces (`click`, `rich`...)
3. Imports locaux (`src.models`...)

### 4. Naming conventions (N802, N806)

```python
# ❌ Avant
def AddTask(Title):  # Fonctions en snake_case, pas PascalCase
    TaskID = 1       # Variables en snake_case
    return TaskID

# ✅ Après
def add_task(title):
    task_id = 1
    return task_id
```

### 5. Code simplifiable (SIM)

```python
# ❌ Avant
if status == TaskStatus.TODO:
    return True
else:
    return False

# ✅ Après (SIM103)
return status == TaskStatus.TODO
```

## 🎨 Intégration VSCode

### Installation de l'extension

1. Installer l'extension "Ruff" dans VSCode
2. Ajouter à `.vscode/settings.json` :

```json
{
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll": true,
      "source.organizeImports": true
    }
  },
  "ruff.lint.enable": true
}
```

**Résultat :**
- 🔴 Erreurs soulignées en temps réel
- 💡 Quick fixes disponibles (Ctrl+.)
- ✨ Auto-fix à la sauvegarde

## 🚦 CI/CD (aperçu)

Au Sprint 6, on ajoutera Ruff dans la pipeline GitLab :

```yaml
# .gitlab-ci.yml (aperçu)
lint:
  script:
    - pip install ruff
    - ruff check src/
  allow_failure: false  # Bloque le merge si erreurs
```

## ✅ Exercice pratique

### 1. Installer Ruff

```bash
pip install ruff
```

### 2. Créer un fichier avec des erreurs

Créez `bad_code.py` :

```python
import sys
from datetime import datetime, timedelta
from src.models.task import Task

def AddTask(Title, Description):
    unused_var = "hello"
    TaskID = 1
    if TaskID == 1:
        return True
    else:
        return False
```

### 3. Lancer Ruff

```bash
ruff check bad_code.py
```

Vous devriez voir plusieurs erreurs !

### 4. Auto-fix

```bash
ruff check --fix bad_code.py
```

Comparez le fichier avant/après.

### 5. Vérifier votre vrai code

```bash
ruff check src/
```

Si tout est propre : 🎉 Bravo !

Sinon : corrigez les erreurs (manuellement ou avec `--fix`).

## 🎓 Règles avancées

### Détecter du code bugbear (B)

```python
# ❌ B006: Mutable default argument
def add_tags(task, tags=[]):  # Dangereux !
    tags.append("new")
    return tags

# ✅ Correct
def add_tags(task, tags=None):
    if tags is None:
        tags = []
    tags.append("new")
    return tags
```

### Simplifications (SIM)

```python
# ❌ SIM110: Use all()
found = True
for item in items:
    if not item.valid:
        found = False
        break

# ✅ Plus Pythonic
found = all(item.valid for item in items)
```

## 📚 Ressources

- [Documentation Ruff](https://docs.astral.sh/ruff/)
- [Liste des règles](https://docs.astral.sh/ruff/rules/)
- [Configuration guide](https://docs.astral.sh/ruff/configuration/)

## Points de validation

- [ ] `pyproject.toml` créé avec config Ruff
- [ ] Ruff installé dans le venv
- [ ] `ruff check src/` passe sans erreurs
- [ ] Extension VSCode installée (optionnel)
- [ ] Vous comprenez les principales catégories de règles

## 💡 Astuces

**Ignorer une ligne spécifique :**
```python
import something_weird  # noqa: F401
```

**Ignorer un fichier entier :**
Ajoutez dans `pyproject.toml` :
```toml
extend-exclude = ["old_code.py"]
```

**Voir toutes les règles actives :**
```bash
ruff rule --all
```

## 💾 Commit

```bash
git add pyproject.toml requirements.txt
git commit -m "chore: add ruff linting configuration"
```

## Prochaine étape

→ **Step 05: Formatage automatique**

Vous allez utiliser Ruff comme formatteur pour uniformiser le style du code.

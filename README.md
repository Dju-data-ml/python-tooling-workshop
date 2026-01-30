# Step 02: Environnements virtuels et dépendances

## Objectif

Apprendre à gérer proprement les dépendances Python avec des environnements virtuels.

## Installation des dépendances

### Option 1: Avec UV (recommandé)

[UV](https://docs.astral.sh/uv/) est un gestionnaire de packages Python ultra-rapide.

```bash
# Installer les dépendances (crée automatiquement le venv)
uv sync
```

C'est tout ! UV crée l'environnement virtuel et installe les dépendances en quelques secondes.

### Option 2: Méthode classique (venv + pip)

```bash
# Créer un environnement virtuel
python -m venv .venv

# Activer l'environnement
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Installer les dépendances
pip install -r requirements.txt
```

## Pourquoi un environnement virtuel ?

### Le problème sans venv

Imaginez ce scénario :
```
Projet A nécessite : requests==2.25.0
Projet B nécessite : requests==2.31.0
```

Si vous installez les deux globalement :
- ❌ Conflit de versions
- ❌ Un projet va casser
- ❌ Impossible de reproduire l'environnement

### La solution : venv

Un **environnement virtuel** isole les dépendances de chaque projet :
```
/home/user/
├── projet-a/
│   └── .venv/  → requests 2.25.0
└── projet-b/
    └── .venv/  → requests 2.31.0
```

Pas de conflit
Reproductibilité garantie
Préparation à Docker

## Dépendances du projet

Notre Task Manager utilise deux bibliothèques :

### Rich
- **Rôle :** Affichage stylé dans le terminal
- **Usage :** Tableaux, couleurs, progress bars
- **Pourquoi :** Rendre la CLI professionnelle et agréable

### Click
- **Rôle :** Framework pour créer des CLI
- **Usage :** Parsing des arguments, commandes, options
- **Pourquoi :** Standard de facto pour les CLI Python

## À reproduire

### Avec UV (recommandé)

```bash
# Synchroniser l'environnement
uv sync

# Vérifier l'installation
uv run python -c 'from rich.console import Console; Console().print("[green]OK![/green]")'
```

### Avec venv + pip (méthode classique)

#### 1. Créer un environnement virtuel

```bash
python -m venv .venv
```

**Explication :**
- `python -m venv` : module intégré à Python 3.3+
- `.venv` : nom du dossier (convention, peut être `venv`, `env`, etc.)

#### 2. Activer l'environnement

**Sur Linux/Mac :**
```bash
source .venv/bin/activate
```

**Sur Windows :**
```powershell
.venv\Scripts\activate
```

**Vérification :**
Votre prompt devrait afficher `(.venv)` au début :
```bash
(.venv) user@machine:~/project$
```

#### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

**Ce qui se passe :**
- Pip lit `requirements.txt`
- Télécharge les packages depuis PyPI
- Les installe dans `.venv/lib/python3.x/site-packages/`

#### 4. Vérifier l'installation

```bash
pip list
```

Vous devriez voir :
```
Package    Version
---------- -------
click      8.1.7
rich       13.7.0
...
```

### Tester Rich en Python

```python
python
>>> from rich.console import Console
>>> console = Console()
>>> console.print("[bold green]Success![/bold green]")
```

Vous devriez voir du texte vert et gras !

## Le fichier requirements.txt

### Format

```txt
package==version  # Version exacte (recommandé pour la prod)
package>=version  # Version minimum
package~=version  # Version compatible
```

**Notre choix :** Versions exactes pour la reproductibilité.

### Générer requirements.txt

Si vous avez installé des packages manuellement :
```bash
pip freeze > requirements.txt
```

⚠️ **Attention :** `pip freeze` liste TOUS les packages, y compris les dépendances transitives. Pour un projet propre, listez manuellement uniquement vos dépendances directes.

### requirements-dev.txt (bonus)

On peut séparer les dépendances :

**requirements.txt :** Production uniquement
```txt
rich==13.7.0
click==8.1.7
```

**requirements-dev.txt :** Développement + Production
```txt
-r requirements.txt  # Inclut requirements.txt
pytest==7.4.3
ruff==0.1.9
```

Installation dev :
```bash
pip install -r requirements-dev.txt
```

## Préparation à Docker

Cette approche avec `requirements.txt` est exactement ce qu'on fera dans Docker :

```dockerfile
# Dockerfile (aperçu du Sprint 5)
FROM python:3.11-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ ./src/
```

## Bonnes pratiques

### À faire
- Toujours activer le venv avant de travailler
- Commiter `requirements.txt`
- Mettre `.venv/` dans `.gitignore`
- Documenter les dépendances système si nécessaires

### À éviter
- Commiter le dossier `.venv/` (il est déjà dans `.gitignore`)
- Installer des packages globalement
- Mélanger venv et système
- Oublier d'activer le venv

## Concepts avancés

### UV vs pip/venv

| Aspect | UV | pip + venv |
|--------|----|-----------|
| **Vitesse** | 10-100x plus rapide | Standard |
| **Commandes** | `uv sync` | 3 commandes |
| **Lockfile** | `uv.lock` automatique | Manuel |
| **Reproductibilité** | Garantie | Approximative |

### pyproject.toml

Format moderne pour gérer les dépendances (utilisé par UV) :

```toml
[project]
name = "python-tooling-workshop"
version = "0.1.0"
dependencies = [
    "rich>=13.7.0",
    "click>=8.1.7",
]

[project.optional-dependencies]
dev = [
    "ruff>=0.1.9",
]
```

### Alternatives à venv

- **UV :** Ultra-rapide, moderne, recommandé
- **virtualenv :** Ancêtre de venv, plus de fonctionnalités
- **conda :** Environnements avec packages non-Python (NumPy, ML)
- **poetry :** Gestion moderne de dépendances

## Points de validation

- [ ] Environnement créé (`uv sync` ou `python -m venv`)
- [ ] Dépendances installées (rich et click)
- [ ] Test d'import de Rich fonctionne
- [ ] `.venv/` bien ignoré par Git

## Petit défi

Testez cette commande pour voir la puissance de Rich :

```python
from rich.progress import track
import time

for i in track(range(20), description="Processing..."):
    time.sleep(0.1)
```

Vous devriez voir une progress bar !

## Commit

```bash
git add pyproject.toml uv.lock requirements.txt
git commit -m "feat: add project dependencies (rich, click)"
```

**Note :** On ne commit pas `.venv/` car il est dans `.gitignore`.

## Prochaine étape

→ **Step 03: Implémentation des classes**

Vous allez créer les classes `Task` et `TaskManager` avec de la vraie POO.

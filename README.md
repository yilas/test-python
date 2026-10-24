# Démonstration GitHub Actions

Une pipeline volontairement simple pour illustrer **jobs**, **steps**, exécution **en série** et **en parallèle**.

```text
           Preparation
             /    \
            v      v
      Test Python  Test systeme
            \      /
             v    v
        Livraison fictive
```

Chaque job contient plusieurs steps visibles dans GitHub Actions.

- `preparation` démarre d'abord.
- `python` et `systeme` s'exécutent ensuite en parallèle.
- `livraison` attend la réussite des deux jobs.

## Exécuter le programme

```bash
python main.py
```

## Démonstration

1. Ouvrir une Pull Request : le workflow se lance.
2. Ouvrir l'onglet Actions et développer chaque job pour voir les steps.
3. Observer les deux jobs parallèles et la livraison qui attend leur réussite.
4. Introduire une erreur de syntaxe dans `main.py` : le job Python échoue et la livraison est ignorée.
5. Corriger l'erreur et pousser à nouveau.

Le workflow se déclenche sur les PR, sur les pushs vers `main` et manuellement (depuis la branche par défaut).

Ce projet n'a volontairement ni packaging, ni Ruff, ni pytest, ni vraie publication : l'objectif est uniquement de montrer l'orchestration.

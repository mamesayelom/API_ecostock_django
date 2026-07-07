# Eco-Stock API

## Présentation

Eco-Stock est une API REST développée avec **Django** et **Django REST Framework** permettant de gérer les stocks alimentaires de plusieurs entrepôts.

L'objectif de l'application est de centraliser les surplus alimentaires provenant de commerces locaux afin de les redistribuer avant leur date de péremption.

L'API permet de gérer les entrepôts, les produits, les transferts de produits entre entrepôts et la sécurisation des opérations grâce à une authentification JWT.

---

# Fonctionnalités

## Gestion des entrepôts

* Créer un entrepôt
* Lister tous les entrepôts
* Afficher les détails d'un entrepôt
* Modifier un entrepôt
* Supprimer un entrepôt

Chaque entrepôt possède :

* Nom
* Localisation
* Capacité

---

## Gestion des produits

* Créer un produit
* Lister les produits
* Consulter un produit
* Modifier un produit
* Supprimer un produit

Chaque produit possède :

* Nom
* Quantité
* Date d'expiration
* État (Disponible, Réservé, Périmé)
* Entrepôt

---

## Actions métier

### Déplacement d'un produit

Permet de déplacer un produit d'un entrepôt vers un autre.

**Endpoint**

`POST /api/products/{id}/move/`

Conditions :

* le produit doit exister ;
* le nouvel entrepôt doit exister ;
* un produit périmé ne peut pas être déplacé.

---

### Audit d'un entrepôt

Retourne le nombre total de produits présents dans un entrepôt.

**Endpoint**

`GET /api/warehouses/{id}/audit/`

---

# Authentification

L'API utilise **JWT (JSON Web Token)** avec **Simple JWT**.

Obtenir un token :

`POST /api/token/`

Rafraîchir un token :

`POST /api/token/refresh/`

Les routes de modification sont protégées et nécessitent un token JWT valide.

---

# Technologies utilisées

* Python 3
* Django
* Django REST Framework
* Simple JWT
* SQLite (développement)
* Postman / Insomnia
* Git & GitHub

---

# Installation

## 1. Cloner le projet

```bash
git clone <url-du-repository>
```

## 2. Créer un environnement virtuel

Sous Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Sous Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 4. Appliquer les migrations

```bash
python manage.py migrate
```

---

## 5. Créer un super utilisateur

```bash
python manage.py createsuperuser
```

---

## 6. Lancer le serveur

```bash
python manage.py runserver
```

L'API sera accessible sur :

```
http://127.0.0.1:8000/
```

---

# Endpoints principaux

## Authentification

| Méthode | Endpoint              | Description          |
| ------- | --------------------- | -------------------- |
| POST    | `/api/token/`         | Obtenir un token JWT |
| POST    | `/api/token/refresh/` | Rafraîchir un token  |

---

## Entrepôts

| Méthode | Endpoint                      | Description           |
| ------- | ----------------------------- | --------------------- |
| GET     | `/api/warehouses/`            | Liste des entrepôts   |
| POST    | `/api/warehouses/`            | Créer un entrepôt     |
| GET     | `/api/warehouses/{id}/`       | Détails d'un entrepôt |
| PUT     | `/api/warehouses/{id}/`       | Modifier un entrepôt  |
| DELETE  | `/api/warehouses/{id}/`       | Supprimer un entrepôt |
| GET     | `/api/warehouses/{id}/audit/` | Audit d'un entrepôt   |

---

## Produits

| Méthode | Endpoint                   | Description          |
| ------- | -------------------------- | -------------------- |
| GET     | `/api/products/`           | Liste des produits   |
| POST    | `/api/products/`           | Créer un produit     |
| GET     | `/api/products/{id}/`      | Détails d'un produit |
| PUT     | `/api/products/{id}/`      | Modifier un produit  |
| DELETE  | `/api/products/{id}/`      | Supprimer un produit |
| POST    | `/api/products/{id}/move/` | Déplacer un produit  |

---

# Réponses HTTP

L'API respecte les principaux codes HTTP :

* **200 OK** : opération réussie
* **201 Created** : ressource créée
* **204 No Content** : suppression réussie
* **400 Bad Request** : données invalides
* **401 Unauthorized** : authentification requise
* **404 Not Found** : ressource introuvable

---

# Sécurité

Les opérations sensibles sont protégées grâce à JWT.

Les utilisateurs non authentifiés ne peuvent pas modifier les données de l'application.

---

# Auteur

Développé dans le cadre d'un projet pédagogique avec **Django REST Framework** pour la gestion d'inventaire et des flux logistiques d'Eco-Stock.

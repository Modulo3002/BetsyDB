# Betsy Webshop

Betsy is a fictional web marketplace where users can sell and buy homemade goods. This project showcases database design and querying capabilities using the **Peewee ORM** and **SQLite**. The application demonstrates skills in SQL joins, database modeling, and implementing functionalities such as searching, purchasing, and managing inventory.

---

## Features

### Modeling
- **Users**: Each user has a name, address, and billing information.
- **Products**: Users can list products with details such as name, description, price, quantity, and tags.
- **Tags**: Products are categorized with tags (e.g., "fashion", "home").
- **Transactions**: Tracks purchases made by users, including buyer, product, quantity, and total price.

### Querying
- Search for products by name or description (with fuzzy matching to handle spelling mistakes).
- List all products for a given user.
- List all products under a specific tag.
- Add, update, and remove products from a user's catalog.
- Update stock quantity for products.
- Handle purchases between users.

---

## Setup

### Prerequisites
- Python 3.8 or higher
- SQLite 3.x
- Installed Python packages: `peewee`, `rapidfuzz`

Install dependencies using:
```bash
pip install peewee rapidfuzz

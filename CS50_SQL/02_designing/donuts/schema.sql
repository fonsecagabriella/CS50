-- Donuts table
CREATE TABLE IF NOT EXISTS "donuts" (
    "id" INTEGER,
    "name" VARCHAR(255) NOT NULL DEFAULT 'Delicious Donut',
    "is_gluten_free" BOOLEAN NOT NULL DEFAULT FALSE,
    "is_vegan" BOOLEAN NOT NULL DEFAULT FALSE,
    "price" DECIMAL(5, 2) NOT NULL,
    "is_available" BOOLEAN NOT NULL DEFAULT TRUE,

    PRIMARY KEY ("id")
);

-- Ingredients table
CREATE TABLE IF NOT EXISTS "ingredients" (
    "id" INTEGER,
    "name" VARCHAR(255) NOT NULL,
    "unit" VARCHAR(50) NOT NULL,
    "cost_per_unit" DECIMAL(10, 2) NOT NULL,

    PRIMARY KEY ("id")
);

-- Donut ingredients table
CREATE TABLE IF NOT EXISTS "donut_ingredients" (
    "id" INTEGER,
    "donut_id" INTEGER NOT NULL,
    "ingredient_id" INTEGER NOT NULL,
    "quantity" DECIMAL(10, 2) NOT NULL,

    PRIMARY KEY ("id"),
    FOREIGN KEY ("donut_id") REFERENCES "donuts"("id"),
    FOREIGN KEY ("ingredient_id") REFERENCES "ingredients"("id")
);

-- Customers table
CREATE TABLE IF NOT EXISTS "customers" (
    "id" INTEGER,
    "name" VARCHAR(255) NOT NULL,
    "last_name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) UNIQUE,
    "phone_number" VARCHAR(20) UNIQUE,

    PRIMARY KEY ("id"),
    CONSTRAINT "chk_email" CHECK ("email" IS NULL OR "email" LIKE '%_@__%.__%'),
    CONSTRAINT "chk_phone_or_email" CHECK ("phone_number" IS NOT NULL OR "email" IS NOT NULL)
);

-- Orders table
CREATE TABLE IF NOT EXISTS "orders" (
    "id" INTEGER,
    "customer_id" INTEGER NOT NULL,
    "order_date" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY ("id"),
    FOREIGN KEY ("customer_id") REFERENCES "customers"("id")
);

-- Order items table
CREATE TABLE IF NOT EXISTS "order_items" (
    "id" INTEGER,
    "order_id" INTEGER NOT NULL,
    "donut_id" INTEGER NOT NULL,
    "quantity" INTEGER NOT NULL,

    PRIMARY KEY ("id"),
    FOREIGN KEY ("order_id") REFERENCES "orders"("id"),
    FOREIGN KEY ("donut_id") REFERENCES "donuts"("id")
);
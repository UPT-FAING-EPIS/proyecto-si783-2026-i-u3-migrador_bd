-- SQL Export generado por MigradorBD
-- Fecha: 2026-07-04 11:55:45.238340
-- Motor destino: postgresql

CREATE TABLE IF NOT EXISTS "public"."usuarios" ("id" INTEGER, "nombre" TEXT NOT NULL, "email" TEXT NOT NULL, PRIMARY KEY ("id"));
INSERT INTO "public"."usuarios" ("id", "nombre", "email") VALUES (1, 'Juan Perez', 'juan@ejemplo.com');
INSERT INTO "public"."usuarios" ("id", "nombre", "email") VALUES (2, 'Maria Lopez', 'maria@ejemplo.com');

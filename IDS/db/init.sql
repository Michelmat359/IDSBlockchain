-- Crear el rol Agente
CREATE ROLE agente WITH LOGIN PASSWORD 'agente_password';
GRANT CONNECT ON DATABASE ids TO agente;
GRANT USAGE ON SCHEMA public TO agente;

-- Permisos para el rol Agente
GRANT INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO agente;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT INSERT, UPDATE, DELETE ON TABLES TO agente;

-- Crear el rol Consumidor
CREATE ROLE consumidor WITH LOGIN PASSWORD 'consumidor_password';
GRANT CONNECT ON DATABASE ids TO consumidor;
GRANT USAGE ON SCHEMA public TO consumidor;

-- Permisos para el rol Consumidor
GRANT SELECT ON ALL TABLES IN SCHEMA public TO consumidor;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO consumidor;

# Usar la imagen base de Node.js
FROM node:16

# Configurar el directorio de trabajo
WORKDIR /usr/src/app

# Instalar Ganache CLI globalmente
RUN npm install -g ganache

# Exponer el puerto 8545 por defecto
EXPOSE 8545

# Comando para ejecutar Ganache
CMD ["ganache", "--host", "0.0.0.0"]

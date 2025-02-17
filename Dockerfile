# Dockerfile para construir la documentación con Sphinx
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /docs

# Copia el archivo de requerimientos e instala dependencias
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia todo el contenido de tu documentación
COPY . .

# Comando por defecto: generar la documentación en HTML
CMD ["sphinx-build", "-b", "html", ".", "_build/html"]

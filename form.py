more_html = """<!DOCTYPE html>
<html>
<head>
    <title>Formulario de Contacto</title>
    <link rel="stylesheet" href="contact.css">
</head>
<body>
    <h2>Contáctanos</h2>
    <form id="contact-form" onsubmit="enviar(); return false;">
        <label for="name">Nombre</label>
        <input type="text" id="name" name="name" required placeholder="Nombre"><br>

        <label for="email">Correo</label>
        <input type="text" id="email" name="email" required placeholder="Correo Electronico"><br>

        <label for="msg">Mensaje</label>
        <textarea id="msg" name="msg" required placeholder="Dejanos tu mensaje"></textarea><br>

        <button type="submit" aria-label="Enviar formulario de Contacto">Enviar</button>
    </form>
    <script src="contact.js"></script>
</body>
</html>
"""

contact_css = """body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    color: #333;
}
form {
    width: 50%;
    padding: 50px;
}
input, textarea {
    padding: 10px;
    display: block;
    margin: 10px 0;
    border-radius: 5px;
    border: 1px solid #ccc;
    width: 50%;
}
button {
    background-color: #28a745;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
button:hover {
    background-color: #218838;
}
"""

contact_js = """function enviar() {
    let email = document.getElementById('email').value;
    alert("Gracias por contactarnos " + email);
}
"""

# Guardar nuevos archivos
project_path = "C:/Users/krist/OneDrive/Documentos/GitHub/Programacion-Web"

with open(f"{project_path}/index.html", "w") as f:
    f.write(more_html)

with open(f"{project_path}/contact.css", "w") as f:
    f.write(contact_css)

with open(f"{project_path}/contact.js", "w") as f:
    f.write(contact_js)

# Reempaquetar el proyecto en un nuevo archivo ZIP
extended_zip_path = "/mnt/data/Proyecto_Web_Erroneo_Extendido.zip"
with ZipFile(extended_zip_path, 'w') as zipf:
    for root, _, files in os.walk(project_path):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, arcname=os.path.relpath(file_path, project_path))

extended_zip_path

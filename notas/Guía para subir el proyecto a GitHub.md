Guía práctica para el día a día de este repo (`fraude_clv`): subir actualizaciones (`push`), bajar cambios (`pull`), y clonarlo en otra PC. Ya está creado y en GitHub — esto es solo para seguir usándolo.

## 0. El token (una sola vez por PC)

No hay `gh` CLI ni `credential.helper` configurado en esta máquina, así que GitHub pide un **Personal Access Token (PAT)** en vez de contraseña. Se crea una sola vez por PC/usuario, no por cada push:

1. github.com → foto de perfil → **Settings**.
2. **Developer settings** (al fondo del menú izquierdo).
3. **Personal access tokens** → **Tokens (classic)** → **Generate new token (classic)**.
4. **Note**: algo descriptivo (ej. `push-modelo-fuga`). **Expiration**: 30-90 días. **Scopes**: solo `repo`.
5. **Generate token** → copiar (`ghp_...`). Se muestra **una sola vez** — guardarlo en un gestor de contraseñas.

**Nunca pegarlo en un archivo del proyecto ni en el chat.** Si queda escrito en algún lado, ya está comprometido: revocarlo (Developer settings → Tokens classic → Delete) y generar uno nuevo.

Cuando git lo pida:
- **Username**: tu usuario de GitHub.
- **Password**: el token — no tu contraseña real de GitHub (eso ya no funciona para git desde 2021).

Una vez logueado una vez (o si Windows tiene Git Credential Manager y usa el navegador), no vuelve a pedir nada hasta que el token expire.

---

## 1. Push — subir una actualización

Cada vez que cambias o agregas algo y quieres subirlo a GitHub:

```bash
cd "C:\Users\josearey\Documents\proyecto datascience - modelo de fuga"
git status
```

`git status` te dice qué cambió. Dos casos:

**a) Modificaste un archivo que ya estaba en el repo** (una nota, un notebook):

```bash
git add "notas/nombre del archivo.md"
git commit -m "mensaje corto de qué cambió"
git push
```

**b) Es un archivo nuevo** (no estaba antes en el repo): primero hay que permitirlo en `.gitignore`, si no `git add` no lo encuentra. Abrir `.gitignore` en la raíz del proyecto y agregar una línea, en el bloque que corresponda:

```gitignore
!notas/nombre del archivo nuevo.md
```

o para un notebook nuevo:

```gitignore
!notebooks/nombre_nuevo.ipynb
```

Después, igual que arriba:

```bash
git add .gitignore "notas/nombre del archivo nuevo.md"
git commit -m "mensaje corto"
git push
```

`git add -A` también es seguro de usar en cualquiera de los dos casos: el `.gitignore` ya filtra todo lo que no debe subir (datos, credenciales, `raw/`, etc.), así que agrega todo lo permitido de una y listo.

Si el `push` pide usuario/token, ver la sección 0.

### Ejercicio: subir esta guía

Esta misma nota (`notas/Guía para subir el proyecto a GitHub.md`) ya está permitida en el `.gitignore`. Para subirla:

```bash
cd "C:\Users\josearey\Documents\proyecto datascience - modelo de fuga"
git add "notas/Guía para subir el proyecto a GitHub.md"
git commit -m "Agregar guia de push y pull"
git push
```

---

## 2. Pull — bajar cambios

Cuando el repo remoto tiene algo que tu copia local no tiene (lo subiste desde otra PC, o alguien más con acceso subió algo):

```bash
cd "C:\Users\josearey\Documents\proyecto datascience - modelo de fuga"
git pull
```

Eso es todo en el caso normal. Si tienes cambios locales sin commitear en un archivo que también cambió en el remoto, puede avisar conflicto — ahí conviene primero `git add` + `git commit` tus cambios locales, y recién después `git pull`.

---

## 3. Clonar este proyecto en otra PC

Para tener una copia funcional del repo en una máquina nueva. Importante: el clone solo trae lo que está en GitHub — **no** trae `raw/`, `deploy_totales_*`, `scripts/`, `teoria/` ni nada de eso, porque nunca se subió.

### 3.1 Clonar

```bash
git clone https://github.com/joReAr/fraude_clv.git
cd fraude_clv
```

Esto trae `.gitignore`, `.gitattributes`, `git_clean_notebook.py`, `README.md`, `notebooks/` y `notas/` — lo que esté commiteado en ese momento.

### 3.2 Reconfigurar el filtro de notebooks (obligatorio en cada PC nueva)

Los notebooks de este repo se suben sin outputs gracias a un filtro de git, pero su configuración (`git config filter.stripoutputs.*`) vive en `.git/config` y **no viaja** con el clone — hay que rehacerla en cada máquina:

```bash
git config filter.stripoutputs.clean "\"/ruta/al/python/en/esta/PC/python.exe\" \"$(pwd)/git_clean_notebook.py\""
git config filter.stripoutputs.smudge cat
git config filter.stripoutputs.required false
```

Ajustar la ruta del intérprete de Python a donde esté instalado en esa PC (ver [[entorno-python-anaconda]] — en esta máquina es `%LOCALAPPDATA%\anaconda3\python.exe`). Si se salta este paso, los notebooks se siguen viendo bien, pero cualquier commit nuevo desde esa PC subiría los outputs sin limpiar.

### 3.3 Identidad y credenciales en la PC nueva

```bash
git config user.name "Tu Nombre"
git config user.email "tu-email@ejemplo.com"
```

Para poder hacer `push` desde esa PC, también necesita su propio token (sección 0) — los tokens son por máquina/sesión, no viajan con el repo.

# 🐳 Tuitin - Backend

Este é o back-end do **Tuitin**, um microblog minimalista inspirado no Twitter. A API foi construída com Django e Django REST Framework, permitindo operações de leitura, criação, edição e exclusão de tuits.

> 🔗 API em produção: [https://tuitin-back.onrender.com](https://tuitin-back.onrender.com)

---

## ✨ Funcionalidades

- 📤 **Criação de tuits**
- 📖 **Listagem e detalhes de tuits**
- ✏️ **Edição de tuits**
- ❌ **Exclusão de tuits**
- 🔄 **Seguir/desseguir outros usuários**
- 🖼️ **Alteração de perfil (imagem, capa, nome, etc.)**

---

## 🛠️ Tecnologias Utilizadas

- Python 3.9
- Django 4.2
- Django REST Framework
- PostgreSQL (via Supabase)
- Poetry (gerenciamento de dependências)
- CORS Headers
- Render (deploy)

---

## 🐳 Como rodar localmente
### Importante:
Em `./tuitin/settings.py` você irá se deparar com isso:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
        'OPTIONS': {
            'connect_timeout': 20,
        },
    }
}
```
Se você apenas quer rodar localmente e não quiser configurar as variáveis de ambiente, basta substituir por:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
Assim, você irá rodar um banco de dados `sqlite` local, ideal para teste e prototipagem.

### 1 - Clone o repositório
- `git clone https://github.com/seu-usuario/tuitin-backend.git`
- `cd tuitin-backend`

### 2 - Crie um .env para armazenar as variáveis de ambiente
- `touch .env`
E preencha com:
```
DB_NAME=nome_do_database
DB_USER=nome_de_usuario_do_db
DB_PASSWORD=senha_do_db
DB_HOST=host_do_db
DB_PORT=porta_que_ira_rodar
```

### 3 - Build do container
- `docker build -t tuitin-backend .`

### 4 - Rode o container
- `docker run --env-file .env -p 8000:8000 tuitin-backend`

Se tudo correr normalmente, a API estará rodando em http://localhost:8000

## 📚 API Documentada em `/api/schema/`
Para uma experiência mais agradável, copie e cole o conteudo de `schema.yaml` para a caixa de texto em https://editor.swagger.io/ e visualize todos os endpoints em HTML.

## 🚀 Deploy
O projeto está hospedado na Render. As variáveis de ambiente de produção são configuradas diretamente no painel da Render.

## 🤝 Contribuição
Contribuições são bem-vindas!
Abra uma issue ou envie um pull request com melhorias ou correções.

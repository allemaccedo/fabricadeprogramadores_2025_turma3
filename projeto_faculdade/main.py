from tabelas import SessionLocal, Usuario, Nota

db = SessionLocal()

def criar_novo_usuario_e_nota():
    """Exemplo de como CRIAR dados."""
    novo_usuario = Usuario(
        nome = "Alessandro Macedo",
        email= "macedoalessandro0a16@gmail.com",
        senha_hash= "hash_super_seguro"  
    )

    db.add(novo_usuario)
    db.commit()
    print(f"Usuario '{novo_usuario.nome}' criado com ID: {novo_usuario.id}")

    nova_nota = Nota(
        conteudo="Minha Primeira Nota com SQLAlchemy",
        autor=novo_usuario
    )
    db.add(nova_nota)
    db.commit
    print(f"Nota '{nova_nota.conteudo}' criada para {novo_usuario.nome}")

def ler_dados(nome):
    """Exemplo de como  LER dados."""

    user= db.query(Usuario).filter(Usuario.nome == nome ).filter()

    if user:
        print(f"Encontrei o(a): {user.nome} (Email: {user.email})")
        print("Notas do user:")
        for nota in user.notas:
            print(f"  - conteudo: {nota.conteudo} (ID {nota.id})")

    else:
        print("Usuario(a) nao encontrado.")

def autualizar_nota(id_nota):
    """Exemplo de como ATUALIZAR dados."""
    
    nota_para_editar = db.query(Nota).filter(Nota.id == id_nota).first()

    if nota_para_editar:
        print(f"conteudo original: '{nota_para_editar.conteudo}'")
        nota_para_editar= "Lista de anotações ATUALIZADA!"
        db.commit()
        print(f"conteudo novo: '{nota_para_editar.conteudo}'")
    else:
        print("Nota com ID % não encontrada." % id_nota)

criar_novo_usuario_e_nota()
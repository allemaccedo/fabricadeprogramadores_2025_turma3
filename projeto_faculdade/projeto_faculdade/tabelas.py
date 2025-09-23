import datetime
from sqlalchemy import *
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

DATABASE_URL = "postgresql://postgres:1234@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()

class Usuario (base):
    __tablename__ = "usuarios" 
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column (String(255), unique= True, nullable=False)
    senha_hash = Column (String(255), nullable=False)
    criado_em = Column (DateTime(timezone=True), default=datetime.datetime.now)
    notas = relationship("Nota", back_populates="autor")

class Nota (base):
    __tablename__ = "notas"

    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    conteudo = Column(Text)
    criado_em = Column(DateTime(timezone=True), default=datetime.datetime.now)
    modificado_em = Column(DateTime(timezone=True), default=datetime.datetime.now)

    autor = relationship("Usuario", back_populates="notas")

if __name__ == "__main__":
    base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso (se não existiam).")
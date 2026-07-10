# import psycopg2   # körpü kitabxanamızı çağırırıq
#
# # connect() — Postgres-ə bağlantı yaradır
# # Buradakı 5 məlumat DataGrip-də doldurduğumuz eyni 5 xanadır
# conn = psycopg2.connect(
#     host="localhost",        # database harada yerləşir: öz kompüterimizdə
#     port=5432,               # Postgres-in qapı nömrəsi
#     database="ai_course",    # DataGrip-də yaratdığımız database
#     user="postgres",         # istifadəçi adı
#     password="postgres"   # sizin şifrəniz
# )
#
# print("Postgres-ə uğurla qoşulduq!")
#
# conn.close()   # işimiz bitdi — bağlantını bağlayırıq
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker
# from sqlalchemy import Column, Integer, String, Boolean, DateTime
#
#
# # 1. Engine — bağlantı hovuzunu idarə edir
# # echo=True etsəniz, arxa planda gedən SQL-ləri görəcəksiniz (debug üçün)
# # postgresql://istifadəçi:şifrə@host:port/database_adı
# engine = create_engine("postgresql://postgres:postgres@localhost:5432/ai_course")
#
# # 3. Session fabrikası
# # autocommit=False → dəyişiklikləri özümüz commit etməliyik
# SessionLocal = sessionmaker(bind=engine)
#
# # 4. Baza sinifi — bütün modellərimiz bunu miras alacaq
# Base = declarative_base()
#
# from sqlalchemy import Column, Integer, String, Boolean, DateTime
# from datetime import datetime
#
# class Istifadeci(Base):
#     __tablename__ = "istifadeciler"
#     id = Column(Integer, primary_key=True)
#     ad=Column(String)
#     email=Column(String,unique=True)
#
#     def __repr__(self):
#         return f"<User(id={self.id}, ad='{self.ad}', email='{self.email}')>"
#
#
# # Cədvəli bazada yarat (mövcud deyilsə)
# Base.metadata.create_all(bind=engine)
#
# db=SessionLocal()
#
# istifadeci=db.query(Istifadeci).filter(Istifadeci.id==1).first()
#
# istifadeci.ad="Leyla"
#
# db.commit()
# db.refresh(istifadeci)
# db.delete(istifadeci)
# db.commit()
#
# print(istifadeci)



import psycopg2   # körpü kitabxanamızı çağırırıq

# connect() — Postgres-ə bağlantı yaradır
# Buradakı 5 məlumat DataGrip-də doldurduğumuz eyni 5 xanadır
conn = psycopg2.connect(
    host="localhost",        # database harada yerləşir: öz kompüterimizdə
    port=5432,               # Postgres-in qapı nömrəsi
    database="ai_course",    # DataGrip-də yaratdığımız database
    user="postgres",         # istifadəçi adı
    password="postgres"   # sizin şifrəniz
)

print("Postgres-ə uğurla qoşulduq!")

conn.close()   # işimiz bitdi — bağlantını bağlayırıq

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql://postgres:postgres123@localhost:5432/ai_course")

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

class Kitab(Base):
    __tablename__ = "kitablar"
    id      = Column(Integer, primary_key=True)
    bashliq = Column(String(100))
    muellif = Column(String(50))
    oxunub  = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Kitab '{self.bashliq}'>"

Base.metadata.create_all(bind=engine)


class Kitab(Base):
    __tablename__ = "kitablar"
    id = Column(Integer, primary_key=True)
    ad=Column(String)
    muellif = Column(String)

    db=SessionLocal()

    db.add(Kitab(ad=))
    db.commit()
    db.refresh(Kitab)

axtardigim_kitab=db.query(Kitab).filter(Kitab.ad="").first()

axtrardigim_kitab.ad=""
db.commit()
db.refresh(axtardigim_kitab)

db.delete(axtardigim_kitab)
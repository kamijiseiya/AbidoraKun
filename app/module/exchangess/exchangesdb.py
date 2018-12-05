import os  # パスを操作するモジュール
import sys  # パスを読み込むモジュール

sys.path.append(os.path.abspath(os.path.join('..')))  # 自作モジュールのパス指定
from sqlalchemy import Column, Integer, String

from app.module.exchangess.setting import Base
from app.module.exchangess.setting import ENGINE


class Exchanges(Base):
    """取引所"""
    __tablename__ = 'exchanges'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(200))
    api = Column('api', String(200))
    secret = Column('secret', String(200))


def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main(sys.argv)

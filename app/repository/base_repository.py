from ..extensions import engine, session


class BaseRepository:
      """
      Base Repositry that initiate engine and session from extension

      Attributes:
        engine(object): engine to use in the repository
        session(object): session manager of sqlalchemy
      """
      def __init__(self) -> None:
          self.engine = engine
          self.session = session

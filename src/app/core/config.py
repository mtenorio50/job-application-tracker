from pydantic import BaseSetting


class Settings(BaseSetting):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


class config:
    env_file = ".env"

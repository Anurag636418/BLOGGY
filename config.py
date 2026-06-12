
from pydantic import SecretStr, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):  # BaseSettings from pydantic Settings
    model_config=SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    database_url :str 
    secret_key:SecretStr
    algorithm:str="HS256"
    access_token_expire_minutes:int=30

    s3_bucket_name: str
    s3_region: str = "ap-south-1"
    s3_access_key: SecretStr | None = None
    s3_access_key_id: SecretStr | None = None
    s3_secret_access_key: SecretStr | None = None
    s3_endpoint_url: str | None = None

    @model_validator(mode="after")
    def normalize_s3_access_key_id(self):
        if self.s3_access_key_id is None and self.s3_access_key is not None:
            self.s3_access_key_id = self.s3_access_key
        return self

    max_upload_size_bytes : int=5*1024*1024

    posts_per_page : int =10

    reset_token_expire_minutes:int =60

    mail_server:str ="localhost"
    mail_port :int=587
    mail_username:str=""
    mail_password:SecretStr=SecretStr("")
    mail_from:str="noreply@example.com"
    mail_use_tls:bool=True

    frontend_url:str="https://localhost:8000"

settings=Settings()#loaded from .envfile

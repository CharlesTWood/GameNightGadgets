from dataclasses import dataclass

@dataclass
class Config:    
    SECRET_KEY: str = 'HYUJ78IS9FJBBR0KKOAP9K76GHY'
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///dev.db'
    #URLS
    MINI_SHRINE_URL: str = '/mini_shrines'
    ADVENTURE_KIT_URL: str = '/adventure_kit'
    ADVENTURE_KITS_URL: str = '/adventure_kits'
    ACCOUNT_DETAILS_URL: str = '/account/details'
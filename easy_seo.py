from app import create_app
from config import DevelopmentConfig

app = create_app(DevelopmentConfig)
# print(app.config)



# if __name__ == "__main__":
#     app.run()

from app import routes
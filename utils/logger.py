import logging
import pathlib
from datetime import datetime

logs_dir =pathlib.Path("logs")
logs_dir.mkdir(exist_ok=True)
timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
logging.basicConfig(
    filename=logs_dir/ f"log_{timestamp}.log",
    level=logging.INFO,
    format= "%(asctime)s %(levelname)s %(name)s - %(message)s", # estructura del mensaje (fecha y hora, accion)
    force= True  #cada linea que se genere usara esta configuracion
)

logger = logging.getLogger("talento_tech")
import os 
import sys
import logging

logging_str = '[%(asctime)s: %(levelname)s: %(module)s: %(message)s]'
log_dir = 'logs'
log_filepath = os.path.join(log_dir, 'running_logs.log') #logs/running_logs.log dosya yolu oluşturuldu
os.makedirs(log_dir, exist_ok= True) #logs isimli klasör yaratıldı

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers=[
        logging.FileHandler(log_filepath), #Anlık olarak baktığında logların yazılacağı dosya yolu 
        logging.StreamHandler(sys.stdout) #logların anlık olarak akması için izin veriyoruz 
    ]

)

logger = logging.getLogger('ogrenciTahminlemeLogger') #başka dosyalardan bu loglamayı import etmek için logger ismiyle çağırdık

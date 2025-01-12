from setuptools import find_packages, setup

def get_requirements(file_path:str)->list[str]: #Parametre string tipinde olacaktır ve return tipi liste içinde string tipinde elemanlardan oluşacaktır.
    """
    Bu fonksiyon gereken kütüphaneleri listenin elemanı olarak kayıt eder.
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() #dosya içindeki her satırı sırasıyla okur 
        requirements  = [req.replace('\n','')for req in requirements]
        return requirements
setup(
    name = 'ogrenci_performans_degerlendirme',
    version = '0.0.1',
    author = 'sena',
    author_email = 'senaakhisar1@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('/workspaces/ogrenci_performans_degerlendirme_MLOPs_project/requirements.txt')
)
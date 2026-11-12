# Pet Manager

Aplicacion de escritorio para administrar perros y gatos. La interfaz esta hecha con Tkinter, los reportes con Matplotlib y los datos se guardan en MySQL.

## Ejecutar

Instala las dependencias desde la carpeta del proyecto:

```powershell
python -m pip install -r requirements.txt
```

Inicia la aplicacion:

```powershell
python "Source Packages/View/frmPet.py"
```

La aplicacion espera una base MySQL llamada `administracionmascotasbd` con las tablas `tb_pet`, `tb_dog` y `tb_cat`. Revisa `Source Packages/Model/DbData.py` para configurar la conexion de tu entorno.
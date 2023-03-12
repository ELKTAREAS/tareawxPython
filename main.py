
import wx
import wx.adv
import mysql.connector

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(450, 250))

        panel = wx.Panel(self)

        # Crear los controles del formulario
        self.lbl_nombre = wx.StaticText(panel, label="Nombre:", pos=(20, 20))
        self.txt_nombre = wx.TextCtrl(panel, pos=(150, 20))

        self.lbl_apellido = wx.StaticText(panel, label="Apellido:", pos=(20, 50))
        self.txt_apellido = wx.TextCtrl(panel, pos=(150, 50))

        self.lbl_fecha_nacimiento = wx.StaticText(panel, label="Fecha Nacimiento:", pos=(20, 80))
        # self.txt_fecha_nacimiento = wx.TextCtrl(panel, pos=(150, 80))
        self.txt_fecha_nacimiento = wx.adv.DatePickerCtrl(panel, pos=(150, 80), style=wx.adv.DP_DROPDOWN)

        self.lbl_carrera = wx.StaticText(panel, label="Carrera:", pos=(20, 110))
        carreras = ['Ingeniería en Sistemas', 'Ingeniería en Electrónica', 'Ingeniería Industrial']
        self.combo_carrera = wx.ComboBox(panel, pos=(150, 110), choices=carreras, style=wx.CB_DROPDOWN)

        self.btn_guardar = wx.Button(panel, label="Guardar", pos=(100, 160))
        self.btn_guardar.Bind(wx.EVT_BUTTON, self.guardar_datos)


        # Conectar a la base de datos MySQL
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="estudiantes_db"
        )

    def guardar_datos(self, event):
        # Obtener los datos del formulario
        nombre = self.txt_nombre.GetValue()
        apellido = self.txt_apellido.GetValue()
        fecha_nacimiento = str(self.txt_fecha_nacimiento.GetValue())
        carrera = self.combo_carrera.GetValue()

        # print(fecha_nacimiento)
        # print(type(fecha_nacimiento))

        # Insertar los datos en la base de datos
        cursor = self.db.cursor()
        query = "INSERT INTO estudiantes (nombre, apellido, fecha_nacimiento, carrera) VALUES (%s, %s, %s, %s)"
        values = (nombre, apellido, fecha_nacimiento, carrera)
        cursor.execute(query, values)
        self.db.commit()

        # Limpiar los campos del formulario después de guardar los datos
        self.txt_nombre.SetValue("")
        self.txt_apellido.SetValue("")
        # self.txt_fecha_nacimiento.SetValue("")
        self.combo_carrera.SetValue("")

        wx.MessageBox("Los datos se han guardado correctamente.", "Información", wx.OK | wx.ICON_INFORMATION)

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None, "Formulario de Estudiantes")
    frame.Show(True)
    app.MainLoop()

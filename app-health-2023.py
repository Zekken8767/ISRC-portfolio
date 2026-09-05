import tkinter as tk
from tkinter import ttk
# from ttkbootstrap import Style
import language, model, controller, view

app_root = tk.Tk()
style = ttk.Style() # для ttk
style.theme_use('vista')
# style = Style() # для ttkbootstrap
# app_root = style.master # для ttkbootstrap
#Style().theme_use('superhero')
#Style().theme_use('cosmo')
#Style().theme_use('xpnative')

app_lang = language.Language()
app_model = model.Model(app_root, app_lang)
app_view = view.View(app_root, app_lang)
app_controller = controller.Controller(app_model, app_view)
app_view.set_controller(app_controller)
app_model.set_controller(app_controller)
app_controller.start()

app_root.mainloop()
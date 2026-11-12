import tkinter as tk
import sys
from pathlib import Path
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from Controller.ctlPet import CtlPet
from Classes.clsDog import ClsDog
from Classes.clsCat import ClsCat


class FrmPet(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pet Manager")
        self.geometry("1100x650")
        self.resizable(False, False)

        self.ctl_pet = CtlPet()
        self.init_components()
        self.center_window()
        self.refresh_data()

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def init_components(self):
        # Notebook (Pestañas principales)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # --- Pestaña Pet List ---
        self.frame_pet_list = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_pet_list, text="Pet List")
        
        self.pet_listbox = tk.Listbox(self.frame_pet_list, width=150, height=20)
        self.pet_listbox.pack(padx=10, pady=10, fill="both", expand=True)

        # --- Pestaña Dog Manager ---
        self.frame_dog = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_dog, text="Dog Manager")

        # Campos Dog
        tk.Label(self.frame_dog, text="Code").place(x=20, y=20)
        self.txt_code_dog = tk.Entry(self.frame_dog, width=20)
        self.txt_code_dog.place(x=90, y=20)

        tk.Label(self.frame_dog, text="Name").place(x=350, y=20)
        self.txt_name_dog = tk.Entry(self.frame_dog, width=20)
        self.txt_name_dog.place(x=420, y=20)

        tk.Label(self.frame_dog, text="Born year").place(x=20, y=60)
        self.txt_born_year_dog = tk.Entry(self.frame_dog, width=20)
        self.txt_born_year_dog.place(x=90, y=60)

        tk.Label(self.frame_dog, text="Color").place(x=350, y=60)
        self.txt_color_dog = tk.Entry(self.frame_dog, width=20)
        self.txt_color_dog.place(x=420, y=60)

        tk.Label(self.frame_dog, text="Health Status").place(x=20, y=100)
        self.cb_health_status_dog = ttk.Combobox(self.frame_dog, values=["Sick", "Healthy", "In Surgery"], state="readonly")
        self.cb_health_status_dog.place(x=110, y=100)
        self.cb_health_status_dog.current(0)

        tk.Label(self.frame_dog, text="Breed").place(x=350, y=100)
        self.cb_breed_dog = ttk.Combobox(self.frame_dog, values=["Criollo", "Schnauzer", "German shepherd", "Pincher"], state="readonly")
        self.cb_breed_dog.place(x=420, y=100)
        self.cb_breed_dog.current(0)

        self.cb_pedigree = tk.Checkbutton(self.frame_dog, text="Pedigree")
        self.cb_pedigree.place(x=650, y=100)
        self.pedigree_var = tk.BooleanVar()
        self.cb_pedigree.config(variable=self.pedigree_var)

        tk.Label(self.frame_dog, text="petId").place(x=20, y=145)
        self.txt_pet_id = tk.Entry(self.frame_dog, width=10, state="readonly")
        self.txt_pet_id.place(x=60, y=145)

        tk.Label(self.frame_dog, text="dogId").place(x=180, y=145)
        self.txt_dog_id = tk.Entry(self.frame_dog, width=10, state="readonly")
        self.txt_dog_id.place(x=220, y=145)

        # Botones Dog
        tk.Button(self.frame_dog, text="Save", width=10, command=self.btn_crear_dog_action).place(x=450, y=180)
        tk.Button(self.frame_dog, text="Search", width=10, command=self.btn_buscar_dog_action).place(x=540, y=180)
        tk.Button(self.frame_dog, text="Edit", width=10, command=self.btn_editar_dog_action).place(x=630, y=180)
        tk.Button(self.frame_dog, text="Delete", width=10, command=self.btn_eliminar_dog_action).place(x=720, y=180)

        # Listbox Dog
        self.dog_listbox = tk.Listbox(self.frame_dog, width=150, height=8)
        self.dog_listbox.place(x=20, y=220)

        # --- Pestaña Cat Manager ---
        self.frame_cat = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_cat, text="Cat Manager")

        tk.Label(self.frame_cat, text="Code").place(x=20, y=20)
        self.txt_code_cat = tk.Entry(self.frame_cat, width=20)
        self.txt_code_cat.place(x=90, y=20)

        tk.Label(self.frame_cat, text="Name").place(x=350, y=20)
        self.txt_name_cat = tk.Entry(self.frame_cat, width=20)
        self.txt_name_cat.place(x=420, y=20)

        tk.Label(self.frame_cat, text="Born year").place(x=20, y=60)
        self.txt_born_year_cat = tk.Entry(self.frame_cat, width=20)
        self.txt_born_year_cat.place(x=90, y=60)

        tk.Label(self.frame_cat, text="Color").place(x=350, y=60)
        self.txt_color_cat = tk.Entry(self.frame_cat, width=20)
        self.txt_color_cat.place(x=420, y=60)

        tk.Label(self.frame_cat, text="Health Status").place(x=20, y=100)
        self.cb_health_status_cat = ttk.Combobox(self.frame_cat, values=["Sick", "Healthy", "In Surgery"], state="readonly")
        self.cb_health_status_cat.place(x=110, y=100)
        self.cb_health_status_cat.current(0)

        tk.Label(self.frame_cat, text="Breed").place(x=350, y=100)
        self.cb_breed_cat = ttk.Combobox(self.frame_cat, values=["Birman", "British", "Bombay", "Abyssinian"], state="readonly")
        self.cb_breed_cat.place(x=420, y=100)
        self.cb_breed_cat.current(0)

        tk.Label(self.frame_cat, text="petId2").place(x=20, y=145)
        self.txt_pet_id_2 = tk.Entry(self.frame_cat, width=10, state="readonly")
        self.txt_pet_id_2.place(x=70, y=145)

        tk.Label(self.frame_cat, text="catId").place(x=180, y=145)
        self.txt_cat_id = tk.Entry(self.frame_cat, width=10, state="readonly")
        self.txt_cat_id.place(x=220, y=145)

        # Botones Cat
        tk.Button(self.frame_cat, text="Save", width=10, command=self.btn_crear_cat_action).place(x=450, y=180)
        tk.Button(self.frame_cat, text="Search", width=10, command=self.btn_buscar_cat_action).place(x=540, y=180)
        tk.Button(self.frame_cat, text="Edit", width=10, command=self.btn_editar_cat_action).place(x=630, y=180)
        tk.Button(self.frame_cat, text="Delete", width=10, command=self.btn_eliminar_cat_action).place(x=720, y=180)

        # Listbox Cat
        self.cat_listbox = tk.Listbox(self.frame_cat, width=150, height=8)
        self.cat_listbox.place(x=20, y=220)

        # --- Pestañas de Reportes ---
        self.jp_report_by_health_status = ttk.Frame(self.notebook)
        self.notebook.add(self.jp_report_by_health_status, text="Health Report")

        self.jp_dog_report = ttk.Frame(self.notebook)
        self.notebook.add(self.jp_dog_report, text="Dog Report")

        self.jp_cat_report = ttk.Frame(self.notebook)
        self.notebook.add(self.jp_cat_report, text="Cat Report")

    def fill_dog_jlist(self):
        self.dog_listbox.delete(0, tk.END)
        for dog in self.dog_object_list:
            self.dog_listbox.insert(tk.END, f"Código: {dog.code} | Nombre: {dog.name} | Raza: {dog.breed} | Estado: {dog.health_status}")

    def fill_cat_jlist(self):
        self.cat_listbox.delete(0, tk.END)
        for cat in self.cat_object_list:
            self.cat_listbox.insert(tk.END, f"Código: {cat.code} | Nombre: {cat.name} | Raza: {cat.breed} | Estado: {cat.health_status}")

    def fill_jlist(self):
        self.pet_listbox.delete(0, tk.END)
        for dog in self.dog_object_list:
            self.pet_listbox.insert(tk.END, f"[Perro] Código: {dog.code} | Nombre: {dog.name} | Raza: {dog.breed}")
        for cat in self.cat_object_list:
            self.pet_listbox.insert(tk.END, f"[Gato] Código: {cat.code} | Nombre: {cat.name} | Raza: {cat.breed}")

    def refresh_data(self):
        self.dog_object_list = self.ctl_pet.list_pet("Dog") or []
        self.cat_object_list = self.ctl_pet.list_pet("Cat") or []
        self.fill_dog_jlist()
        self.fill_cat_jlist()
        self.fill_jlist()
        self.refresh_report_by_health_status()
        self.refresh_dog_report()
        self.refresh_cat_report()

    def refresh_report_by_health_status(self):
        report = self.ctl_pet.list_pet_by_health_status()
        labels = [r.health_status for r in report]
        values = [r.amount_of_pets_by_health_status for r in report]

        for widget in self.jp_report_by_health_status.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(6, 4))
        if values:
            ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
        else:
            ax.text(0.5, 0.5, "No data available", ha="center", va="center")
            ax.set_axis_off()
        ax.set_title("Pets Classification By Health Status")

        canvas = FigureCanvasTkAgg(fig, master=self.jp_report_by_health_status)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def refresh_dog_report(self):
        report = self.ctl_pet.list_dog_by_health_status()
        labels = [r.health_status for r in report]
        values = [r.amount_of_pets_by_health_status for r in report]

        for widget in self.jp_dog_report.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(6, 4))
        if values:
            ax.bar(labels, values, color='skyblue')
        else:
            ax.text(0.5, 0.5, "No data available", ha="center", va="center")
            ax.set_axis_off()
        ax.set_title("Dogs Classification By Health Status")
        ax.set_xlabel("Health Status")
        ax.set_ylabel("Amount of Dogs")

        canvas = FigureCanvasTkAgg(fig, master=self.jp_dog_report)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def refresh_cat_report(self):
        report = self.ctl_pet.list_cat_by_health_status()
        labels = [r.health_status for r in report]
        values = [r.amount_of_pets_by_health_status for r in report]

        for widget in self.jp_cat_report.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(6, 4))
        if values:
            ax.barh(labels, values, color='salmon')
        else:
            ax.text(0.5, 0.5, "No data available", ha="center", va="center")
            ax.set_axis_off()
        ax.set_title("Cats Classification By Health Status")
        ax.set_xlabel("Amount of Cats")
        ax.set_ylabel("Health Status")

        canvas = FigureCanvasTkAgg(fig, master=self.jp_cat_report)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Métodos de acción para botones (Dog)
    def btn_crear_dog_action(self):
        try:
            dog = ClsDog(
                dog_id=0,
                breed=self.cb_breed_dog.get(),
                pedigree=self.pedigree_var.get(),
                pet_id=0,
                code=self.txt_code_dog.get(),
                name=self.txt_name_dog.get(),
                born_year=int(self.txt_born_year_dog.get()),
                color=self.txt_color_dog.get(),
                health_status=self.cb_health_status_dog.get()
            )
            if self.ctl_pet.create_pet(dog):
                messagebox.showinfo("Éxito", "Perro guardado correctamente")
                self.refresh_data()
            else:
                messagebox.showerror("Error", "No se pudo guardar el perro")
        except Exception as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def btn_buscar_dog_action(self):
        code = self.txt_code_dog.get()
        dog = self.ctl_pet.search_pet(code, "Dog")
        if dog:
            self.txt_name_dog.delete(0, tk.END)
            self.txt_name_dog.insert(0, dog.name)
            self.txt_born_year_dog.delete(0, tk.END)
            self.txt_born_year_dog.insert(0, str(dog.born_year))
            self.txt_color_dog.delete(0, tk.END)
            self.txt_color_dog.insert(0, dog.color)
            self.cb_health_status_dog.set(dog.health_status)
            self.cb_breed_dog.set(dog.breed)
            self.pedigree_var.set(dog.pedigree)
            self.txt_pet_id.config(state="normal")
            self.txt_pet_id.delete(0, tk.END)
            self.txt_pet_id.insert(0, str(dog.pet_id))
            self.txt_pet_id.config(state="readonly")
            self.txt_dog_id.config(state="normal")
            self.txt_dog_id.delete(0, tk.END)
            self.txt_dog_id.insert(0, str(dog.dog_id))
            self.txt_dog_id.config(state="readonly")
            messagebox.showinfo("Encontrado", "Perro encontrado con éxito")
        else:
            messagebox.showwarning("No encontrado", "No existe un perro con ese código")

    def btn_editar_dog_action(self):
        try:
            dog = ClsDog(
                dog_id=int(self.txt_dog_id.get() or 0),
                breed=self.cb_breed_dog.get(),
                pedigree=self.pedigree_var.get(),
                pet_id=int(self.txt_pet_id.get() or 0),
                code=self.txt_code_dog.get(),
                name=self.txt_name_dog.get(),
                born_year=int(self.txt_born_year_dog.get()),
                color=self.txt_color_dog.get(),
                health_status=self.cb_health_status_dog.get()
            )
            if self.ctl_pet.edit_pet(dog):
                messagebox.showinfo("Éxito", "Perro actualizado correctamente")
                self.refresh_data()
            else:
                messagebox.showerror("Error", "No se pudo actualizar el perro")
        except Exception as e:
            messagebox.showerror("Error", f"Error al editar: {e}")

    def btn_eliminar_dog_action(self):
        try:
            dog = ClsDog(
                dog_id=int(self.txt_dog_id.get() or 0),
                pet_id=int(self.txt_pet_id.get() or 0)
            )
            if self.ctl_pet.delete_pet(dog):
                messagebox.showinfo("Éxito", "Perro eliminado correctamente")
                self.refresh_data()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el perro")
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar: {e}")

    # Métodos de acción para botones (Cat)
    def btn_crear_cat_action(self):
        try:
            cat = ClsCat(
                cat_id=0,
                breed=self.cb_breed_cat.get(),
                pet_id=0,
                code=self.txt_code_cat.get(),
                name=self.txt_name_cat.get(),
                born_year=int(self.txt_born_year_cat.get()),
                color=self.txt_color_cat.get(),
                health_status=self.cb_health_status_cat.get()
            )
            if self.ctl_pet.create_pet(cat):
                messagebox.showinfo("Éxito", "Gato guardado correctamente")
                self.refresh_data()
            else:
                messagebox.showerror("Error", "No se pudo guardar el gato")
        except Exception as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def btn_buscar_cat_action(self):
        code = self.txt_code_cat.get()
        cat = self.ctl_pet.search_pet(code, "Cat")
        if cat:
            self.txt_name_cat.delete(0, tk.END)
            self.txt_name_cat.insert(0, cat.name)
            self.txt_born_year_cat.delete(0, tk.END)
            self.txt_born_year_cat.insert(0, str(cat.born_year))
            self.txt_color_cat.delete(0, tk.END)
            self.txt_color_cat.insert(0, cat.color)
            self.cb_health_status_cat.set(cat.health_status)
            self.cb_breed_cat.set(cat.breed)
            self.txt_pet_id_2.config(state="normal")
            self.txt_pet_id_2.delete(0, tk.END)
            self.txt_pet_id_2.insert(0, str(cat.pet_id))
            self.txt_pet_id_2.config(state="readonly")
            self.txt_cat_id.config(state="normal")
            self.txt_cat_id.delete(0, tk.END)
            self.txt_cat_id.insert(0, str(cat.cat_id))
            self.txt_cat_id.config(state="readonly")
            messagebox.showinfo("Encontrado", "Gato encontrado con éxito")
        else:
            messagebox.showwarning("No encontrado", "No existe un gato con ese código")

    def btn_editar_cat_action(self):
        try:
            cat = ClsCat(
                cat_id=int(self.txt_cat_id.get() or 0),
                breed=self.cb_breed_cat.get(),
                pet_id=int(self.txt_pet_id_2.get() or 0),
                code=self.txt_code_cat.get(),
                name=self.txt_name_cat.get(),
                born_year=int(self.txt_born_year_cat.get()),
                color=self.txt_color_cat.get(),
                health_status=self.cb_health_status_cat.get()
            )
            if self.ctl_pet.edit_pet(cat):
                messagebox.showinfo("Éxito", "Gato actualizado correctamente")
                self.refresh_data()
            else:
                messagebox.showerror("Error", "No se pudo actualizar el gato")
        except Exception as e:
            messagebox.showerror("Error", f"Error al editar: {e}")

    def btn_eliminar_cat_action(self):
        try:
            cat = ClsCat(
                cat_id=int(self.txt_cat_id.get() or 0),
                pet_id=int(self.txt_pet_id_2.get() or 0)
            )
            if self.ctl_pet.delete_pet(cat):
                messagebox.showinfo("Éxito", "Gato eliminado correctamente")
                self.refresh_data()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el gato")
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar: {e}")


if __name__ == "__main__":
    app = FrmPet()
    app.mainloop()
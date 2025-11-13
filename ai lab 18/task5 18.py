import tkinter as tk
from tkinter import ttk, messagebox

# Rule-based crop recommendation function
def recommend_crop(n, p, k, temp, humidity, rainfall, soil_type):
    try:
        n = float(n)
        p = float(p)
        k = float(k)
        temp = float(temp)
        humidity = float(humidity)
        rainfall = float(rainfall)
    except:
        return None  # Invalid input

    if soil_type == "Loamy":
        if 20 <= temp <= 30 and rainfall >= 100:
            return "Rice"
        elif n > 100 and k > 150:
            return "Wheat"
        else:
            return "Maize"
    elif soil_type == "Sandy":
        if temp > 30 and rainfall < 50:
            return "Cotton"
        else:
            return "Maize"
    elif soil_type == "Clayey":
        if humidity > 70 and rainfall > 150:
            return "Rice"
        else:
            return "Barley"
    else:
        return "Maize"

# GUI class
class CropApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crop Recommendation System")
        self.root.geometry("500x600")
        self.root.config(bg="#e6f2ff")

        tk.Label(root, text="Crop Recommendation System", font=("Helvetica", 20, "bold"), bg="#e6f2ff").pack(pady=20)

        self.entries = {}
        for label, key in [("Nitrogen (N):","n"), ("Phosphorus (P):","p"), ("Potassium (K):","k"),
                           ("Temperature (°C):","temp"), ("Humidity (%):","humidity"), ("Rainfall (mm):","rainfall")]:
            tk.Label(root, text=label, font=("Helvetica", 12), bg="#e6f2ff").pack(pady=(10,0))
            entry = tk.Entry(root)
            entry.pack(pady=5)
            self.entries[key] = entry

        tk.Label(root, text="Soil Type:", font=("Helvetica", 12), bg="#e6f2ff").pack(pady=(10,0))
        self.soil_var = tk.StringVar()
        self.soil_combo = ttk.Combobox(root, textvariable=self.soil_var, state="readonly")
        self.soil_combo['values'] = ['Sandy', 'Loamy', 'Clayey']
        self.soil_combo.current(0)
        self.soil_combo.pack(pady=5)

        tk.Button(root, text="Recommend Crop", command=self.predict_crop, bg="#3399ff", fg="white", font=("Helvetica", 12, "bold")).pack(pady=30)
        self.result_label = tk.Label(root, text="", font=("Helvetica", 16), fg="green", bg="#e6f2ff")
        self.result_label.pack(pady=20)

    def predict_crop(self):
        values = {k: e.get() for k, e in self.entries.items()}
        soil = self.soil_var.get()
        crop = recommend_crop(values['n'], values['p'], values['k'], values['temp'], values['humidity'], values['rainfall'], soil)
        if crop:
            self.result_label.config(text=f"Recommended Crop: {crop}")
        else:
            messagebox.showerror("Error", "Please enter valid numeric values for all fields.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CropApp(root)
    root.mainloop()

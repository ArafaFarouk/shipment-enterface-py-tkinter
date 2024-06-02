import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ShippingManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("نظام إدارة الشحنات")

        # إعداد عناصر الواجهة
        self.setup_ui()

    def setup_ui(self):
        # إضافة عناصر الواجهة هنا
        ttk.Label(self.root, text="نظام إدارة الشحنات").grid(column=0, row=0, columnspan=2)

        # إضافة زر لإضافة عميل جديد
        ttk.Button(self.root, text="إضافة عميل", command=self.add_customer).grid(column=0, row=1)
        # إضافة زر لإضافة مندوب جديد
        ttk.Button(self.root, text="إضافة مندوب", command=self.add_courier).grid(column=0, row=2)
        # إضافة زر لإضافة شحنة جديدة
        ttk.Button(self.root, text="إضافة شحنة", command=self.add_shipment).grid(column=0, row=3)
        # إضافة زر لعرض جميع الشحنات
        ttk.Button(self.root, text="عرض الشحنات", command=self.view_shipments).grid(column=0, row=4)

    def add_customer(self):
        # نافذة إدخال عميل جديد
        self.customer_window = tk.Toplevel(self.root)
        self.customer_window.title("إضافة عميل جديد")

        ttk.Label(self.customer_window, text="الاسم:").grid(column=0, row=0)
        self.customer_name = ttk.Entry(self.customer_window)
        self.customer_name.grid(column=1, row=0)

        ttk.Label(self.customer_window, text="البريد الإلكتروني:").grid(column=0, row=1)
        self.customer_email = ttk.Entry(self.customer_window)
        self.customer_email.grid(column=1, row=1)

        ttk.Label(self.customer_window, text="الهاتف:").grid(column=0, row=2)
        self.customer_phone = ttk.Entry(self.customer_window)
        self.customer_phone.grid(column=1, row=2)

        ttk.Button(self.customer_window, text="حفظ", command=self.save_customer).grid(column=0, row=3, columnspan=2)

    def save_customer(self):
        name = self.customer_name.get()
        email = self.customer_email.get()
        phone = self.customer_phone.get()

        conn = sqlite3.connect('إدارة_الشحنات.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO العملاء (الاسم, البريد_الإلكتروني, الهاتف) VALUES (?, ?, ?)", (name, email, phone))
        conn.commit()
        conn.close()

        messagebox.showinfo("نجاح", "تم إضافة العميل بنجاح!")
        self.customer_window.destroy()

    def add_courier(self):
        # نافذة إدخال مندوب جديد
        self.courier_window = tk.Toplevel(self.root)
        self.courier_window.title("إضافة مندوب جديد")

        ttk.Label(self.courier_window, text="الاسم:").grid(column=0, row=0)
        self.courier_name = ttk.Entry(self.courier_window)
        self.courier_name.grid(column=1, row=0)

        ttk.Label(self.courier_window, text="الهاتف:").grid(column=0, row=1)
        self.courier_phone = ttk.Entry(self.courier_window)
        self.courier_phone.grid(column=1, row=1)

        ttk.Button(self.courier_window, text="حفظ", command=self.save_courier).grid(column=0, row=2, columnspan=2)

    def save_courier(self):
        name = self.courier_name.get()
        phone = self.courier_phone.get()

        conn = sqlite3.connect('إدارة_الشحنات.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO المناديب (الاسم, الهاتف) VALUES (?, ?)", (name, phone))
        conn.commit()
        conn.close()

        messagebox.showinfo("نجاح", "تم إضافة المندوب بنجاح!")
        self.courier_window.destroy()

    def add_shipment(self):
        # نافذة إدخال شحنة جديدة
        self.shipment_window = tk.Toplevel(self.root)
        self.shipment_window.title("إضافة شحنة جديدة")

        ttk.Label(self.shipment_window, text="العميل ID:").grid(column=0, row=0)
        self.shipment_customer_id = ttk.Entry(self.shipment_window)
        self.shipment_customer_id.grid(column=1, row=0)

        ttk.Label(self.shipment_window, text="المندوب ID:").grid(column=0, row=1)
        self.shipment_courier_id = ttk.Entry(self.shipment_window)
        self.shipment_courier_id.grid(column=1, row=1)

        ttk.Label(self.shipment_window, text="التكلفة:").grid(column=0, row=2)
        self.shipment_cost = ttk.Entry(self.shipment_window)
        self.shipment_cost.grid(column=1, row=2)

        ttk.Label(self.shipment_window, text="الحالة:").grid(column=0, row=3)
        self.shipment_status = ttk.Entry(self.shipment_window)
        self.shipment_status.grid(column=1, row=3)

        ttk.Button(self.shipment_window, text="حفظ", command=self.save_shipment).grid(column=0, row=4, columnspan=2)

    def save_shipment(self):
        customer_id = self.shipment_customer_id.get()
        courier_id = self.shipment_courier_id.get()
        cost = self.shipment_cost.get()
        status = self.shipment_status.get()

        conn = sqlite3.connect('إدارة_الشحنات.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO الشحنات (العميل_id, المندوب_id, التكلفة, الحالة) VALUES (?, ?, ?, ?)", (customer_id, courier_id, cost, status))
        conn.commit()
        conn.close()

        messagebox.showinfo("نجاح", "تم إضافة الشحنة بنجاح!")
        self.shipment_window.destroy()

    def view_shipments(self):
        # نافذة عرض جميع الشحنات
        self.view_window = tk.Toplevel(self.root)
        self.view_window.title("عرض الشحنات")

        conn = sqlite3.connect('إدارة_الشحنات.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM الشحنات")
        shipments = cursor.fetchall()
        conn.close()

        cols = ('ID', 'العميل ID', 'المندوب ID', 'التكلفة', 'الحالة')
        self.shipments_tree = ttk.Treeview(self.view_window, columns=cols, show='headings')

        for col in cols:
            self.shipments_tree.heading(col, text=col)
            self.shipments_tree.grid(row=0, column=0, columnspan=2)

        for shipment in shipments:
            self.shipments_tree.insert("", "end", values=shipment)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShippingManagementApp(root)
    root.mainloop()

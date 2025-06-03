# 🏥 Odoo Healthcare Modules
![Capture d’écran du 2025-06-03 10-09-40](https://github.com/user-attachments/assets/3a170f15-a41d-4581-b31e-33c8cc335ec9)



---

## 📦 Included Modules

- `hospital`
- `disease_management`
- `patient_portal`
- `nurse`
- `doctor`
- `pharmacy`

---

## 🚀 Installation with Demo Data

Run the following command during the initial setup:

```bash
python odoo-bin -c <odoo.conf> -d <odoodb> -i hospital,disease_management,patient_portal,nurse,doctor,pharmacy,healthcare_bridge
```
 This command installs all the necessary modules and loads demo data automatically.
The system user of your Odoo instance will be assigned to the hospital_admin group.

### Doctor Login
login: doctor1
password: doctor1

### Nurse Login
login: nurse1
password: nurse1

### Patient Login
login: patient1
password: patient1

# To connect with other accounts, navigate to the hospital/demo/ module. You will see the connection information of other users in the demo data.

# CSE_470_Telemedicine_Website
**Telemedicine Website with E-commerce Integration**

**Directory 1: User Management**
1. User Registration and Login
2. User Roles (Patients, Doctors, Admin)
3. Manage User Profiles (specialization, location, availability for doctors; medical history for patients)
4. Doctor Directory (search by specialization, location, availability, and ratings)
5. Patient Directory (search for doctors, manage medical history)

**Directory 2: Appointment Management**
6. Appointment Scheduling
7. Telemedicine Platform (secure CHATTING)
8. Prescription Management (doctors can send electronic prescriptions)
9. Healthcare Reminders (automated reminders for appointments, medication refills)

**Directory 3: E-commerce Integration**
10. Medicine Shop (browse and purchase over-the-counter medicines)
11. Real-time Stock Tracking (avoid out-of-stock orders)
12. Shopping Cart Management
13. Secure Payment Gateway
14. Order Tracking

**Directory 4: Additional Features**
15. Loyalty Program (reward frequent users)
16. Doctor Reviews and Ratings
17. Community Forum (discuss health topics, share experiences)
18. Multilingual Support (Bangla and English)
19. Interactive Symptom Checker (not a substitute for medical diagnosis)
20. HIPAA Compliance (ensure data security and privacy)

Project Structure:
.
├── app.py
├── models
│   ├── __init__.py
│   ├── user.py
│   ├── doctor.py
│   ├── patient.py
│   ├── appointment.py
│   ├── prescription.py
│   ├── product.py
│   └── order.py
├── views
│   ├── __init__.py
│   ├── user.py
│   ├── doctor.py
│   ├── patient.py
│   ├── appointment.py
│   ├── prescription.py
│   ├── product.py
│   └── order.py
└── controllers
    ├── __init__.py
    ├── user.py
    ├── doctor.py
    ├── patient.py
    ├── appointment.py
    ├── prescription.py
    ├── product.py
    └── order.py

 Database Schema:

 ├── User (Parent)
│   ├── id (Primary Key)
│   ├── username
│   ├── password
│   ├── role (Patient, Doctor, Admin)
│   ├── email
│   └── phone
├── Profile (Child of User)
│   ├── id (Primary Key)
│   ├── user_id (Foreign Key referencing User.id)
│   ├── first_name
│   ├── last_name
│   ├── date_of_birth
│   ├── gender
│   └── address
├── Doctor (Child of Profile)
│   ├── id (Primary Key)
│   ├── profile_id (Foreign Key referencing Profile.id)
│   ├── specialization
│   ├── location
│   └── availability
├── Patient (Child of Profile)
│   ├── id (Primary Key)
│   ├── profile_id (Foreign Key referencing Profile.id)
│   └── medical_history
├── Appointment (Child of Doctor and Patient)
│   ├── id (Primary Key)
│   ├── doctor_id (Foreign Key referencing Doctor.id)
│   ├── patient_id (Foreign Key referencing Patient.id)
│   ├── date
│   ├── time
│   └── status
├── Prescription (Child of Appointment)
│   ├── id (Primary Key)
│   ├── appointment_id (Foreign Key referencing Appointment.id)
│   ├── medicine_name
│   ├── dosage
│   └── instructions
├── Product (Parent)
│   ├── id (Primary Key)
│   ├── name
│   ├── description
│   ├── price
│   └── stock
└── Order (Child of User and Product)
    ├── id (Primary Key)
    ├── user_id (Foreign Key referencing User.id)
    ├── product_id (Foreign Key referencing Product.id)
    ├── quantity
    ├── total_price
    └── status

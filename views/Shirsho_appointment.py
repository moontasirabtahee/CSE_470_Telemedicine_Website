from flask import Blueprint, request, jsonify
from controllers.appointment import *

appointment_bp = Blueprint('appointment', __name__)

@appointment_bp.route('/appointments', methods=['POST'])
def create_appointment_route():
    data = request.json
    doctor_id = data.get('doctor_id')
    patient_id = data.get('patient_id')
    date = data.get('date')
    time = data.get('time')
    status = data.get('status')

    appointment = create_appointment(doctor_id, patient_id, date, time, status)
    return jsonify(appointment.serialize()), 201

@appointment_bp.route('/appointments/<int:id>', methods=['GET'])
def get_appointment_route(id):
    appointment = get_appointment(id)
    if appointment:
        return jsonify(appointment.serialize()), 200
    else:
        return jsonify({'message': 'Appointment not found'}), 404

@appointment_bp.route('/appointments/<int:id>', methods=['PUT'])
def update_appointment_route(id):
    data = request.json
    doctor_id = data.get('doctor_id')
    patient_id = data.get('patient_id')
    date = data.get('date')
    time = data.get('time')
    status = data.get('status')

    appointment = update_appointment(id, doctor_id, patient_id, date, time, status)
    return jsonify(appointment.serialize()), 200

@appointment_bp.route('/appointments/<int:id>', methods=['DELETE'])
def delete_appointment_route(id):
    delete_appointment(id)
    return jsonify({'message': 'Appointment deleted successfully'}), 200

@appointment_bp.route('/appointments', methods=['GET'])
def get_all_appointments_route():
    appointments = get_all_appointments()
    return jsonify([appointment.serialize() for appointment in appointments]), 200

# Additional routes for filtering appointments by doctor ID, patient ID, date, etc. can be added similarly

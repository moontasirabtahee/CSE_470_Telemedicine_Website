from flask import Blueprint, request, jsonify
from controllers import patient, appointment

patient_bp = Blueprint('patient', __name__)

@patient_bp.route('/patients/<int:patient_id>/appointments', methods=['POST'])
def book_appointment(patient_id):
    data = request.json
    doctor_id = data.get('doctor_id')
    date = data.get('date')
    time = data.get('time')
    status = 'Booked'
    
    new_appointment = appointment.create_appointment(doctor_id, patient_id, date, time, status)
    return jsonify({'message': 'Appointment booked successfully', 'appointment': new_appointment}), 201

@patient_bp.route('/patients/<int:patient_id>/appointments', methods=['GET'])
def view_appointments(patient_id):
    appointments = appointment.get_appointment_by_patient_id(patient_id)
    return jsonify({'appointments': [apt.__dict__ for apt in appointments]}), 200

@patient_bp.route('/patients/<int:patient_id>/appointments/<int:appointment_id>', methods=['DELETE'])
def cancel_appointment(patient_id, appointment_id):
    appointment.delete_appointment(appointment_id)
    return jsonify({'message': 'Appointment cancelled successfully'}), 200

@patient_bp.route('/patients/<int:patient_id>/prescriptions', methods=['GET'])
def view_prescriptions(patient_id):
    # Implementation for viewing prescriptions goes here
    return jsonify({'message': 'Feature under development'}), 501

@patient_bp.route('/patients/<int:patient_id>/profile', methods=['GET'])
def view_profile(patient_id):
    # Implementation for viewing profile goes here
    return jsonify({'message': 'Feature under development'}), 501

@patient_bp.route('/patients/<int:patient_id>/orders', methods=['POST'])
def order_medicine(patient_id):
    # Implementation for ordering medicine goes here
    return jsonify({'message': 'Feature under development'}), 501

@patient_bp.route('/patients/<int:patient_id>/orders', methods=['GET'])
def view_orders(patient_id):
    # Implementation for viewing orders goes here
    return jsonify({'message': 'Feature under development'}), 501

@patient_bp.route('/patients/<int:patient_id>/orders/<int:order_id>', methods=['DELETE'])
def cancel_order(patient_id, order_id):
    # Implementation for cancelling order goes here
    return jsonify({'message': 'Feature under development'}), 501

@patient_bp.route('/patients/<int:patient_id>/orders/<int:order_id>/status', methods=['GET'])
def view_order_status(patient_id, order_id):
    # Implementation for viewing order status goes here
    return jsonify({'message': 'Feature under development'}), 501

@patient_bp.route('/patients/<int:patient_id>/orders/history', methods=['GET'])
def view_order_history(patient_id):
    # Implementation for viewing order history goes here
    return jsonify({'message': 'Feature under development'}), 501

@patient_bp.route('/patients/<int:patient_id>/medicine', methods=['GET'])
def view_medicine(patient_id):
    # Implementation for viewing available medicine goes here
    return jsonify({'message': 'Feature under development'}), 501

@patient_bp.route('/patients/<int:patient_id>/medicine/<int:medicine_id>', methods=['GET'])
def view_medicine_details(patient_id, medicine_id):
    # Implementation for viewing medicine details goes here
    return jsonify({'message': 'Feature under development'}), 501

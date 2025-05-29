from datetime import date
from odoo.exceptions import ValidationError

def validate_portal_request_data(request_date, doctor_id, symptom_ids):
    if not request_date:
        raise ValidationError("The date of the request is required.")
    if date.fromisoformat(request_date) < date.today():
        raise ValidationError("The request date cannot be earlier than today..")
    if not doctor_id:
        raise ValidationError("Please select a doctor")
    if not symptom_ids:
        raise ValidationError("Please select at least one symptom.")

import qrcode
import base64
from io import BytesIO
from random import randint
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    badge_number = fields.Char(string='Badge Number', copy=False)
    qr_code = fields.Binary(string='QR Code', compute='_compute_qr_code', store=True)
    date_badge_generated = fields.Date(string='Badge Generated On', copy=False)
    badge_expiry_date = fields.Date(string='Badge Expiry Date', copy=False)
    badge_background_color = fields.Char(string='Badge Background Color', default='#FFFFFF')
    
    @api.depends('badge_number', 'name', 'job_title', 'department_id')
    def _compute_qr_code(self):
        """Generate QR code with employee information"""
        for employee in self:
            if employee.badge_number:
                qr_data = f"ID: {employee.badge_number}\nName: {employee.name}\nJob: {employee.job_title or ''}\nDepartment: {employee.department_id.name or ''}"
                
                qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
                qr.add_data(qr_data)
                qr.make(fit=True)
                
                img = qr.make_image()
                buffer = BytesIO()
                img.save(buffer, format="PNG")
                qr_image = base64.b64encode(buffer.getvalue())
                
                employee.qr_code = qr_image
            else:
                employee.qr_code = False
    
    @api.model
    def _generate_badge_number(self):
        """Generate a unique badge number with format EMP-XXXX"""
        while True:
            badge_number = f"EMP-{randint(1000, 9999)}"
            existing = self.search([('badge_number', '=', badge_number)], limit=1)
            if not existing:
                return badge_number
    
    @api.onchange('name')
    def onchange_name(self):
        """Auto-generate badge number for new employees if name is set and badge number is not"""
        if not self.badge_number and self.name:
            self.badge_number = self._generate_badge_number()
    
    def action_generate_badge(self):
        """Action to generate the employee badge"""
        for employee in self:
            if not employee.badge_number:
                employee.badge_number = self._generate_badge_number()
                
            employee.date_badge_generated = fields.Date.today()
            # By default, set expiry date to 1 year from now
            employee.badge_expiry_date = fields.Date.add(fields.Date.today(), years=1)
        
        return self.env.ref('employee_badge.action_report_employee_badge').report_action(self) 
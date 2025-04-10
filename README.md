# Employee Badge Generator

This Odoo module allows you to generate and print ID cards/badges for employees.

## Features

- Extends HR Employee model with badge-related fields
- Automatically generates unique badge numbers
- QR code generation containing employee information
- Configurable badge expiry date
- PDF badge printing functionality

## Installation

1. Copy this module to your Odoo addons directory
2. Update the apps list in your Odoo instance
3. Install the "Employee Badge" module

## Dependencies

This module depends on:
- `hr` (Human Resources)
- Python package: `qrcode` (install with `pip install qrcode`)

## Usage

1. Navigate to Employees > Employees
2. Open an employee record
3. Click on the "Generate Badge" button in the top right
4. The badge will be automatically generated and displayed as a PDF

You can also:
- Generate/print badges in batch by going to Human Resources > Configuration > Employee Badges
- Customize the badge background color in the ID Badge tab of the employee form
- View and update badge information in the ID Badge tab

## Technical Information

The module adds the following fields to the hr.employee model:
- `badge_number`: Unique identifier for the employee badge (auto-generated)
- `qr_code`: QR code containing employee information (auto-generated)
- `date_badge_generated`: Date when the badge was generated
- `badge_expiry_date`: Date when the badge expires (default: 1 year from generation)
- `badge_background_color`: Color picker for badge background 
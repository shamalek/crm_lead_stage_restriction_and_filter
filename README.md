# crm_lead_stage_restriction_and_filter
Developed a custom Odoo CRM module that enforces forward-only stage movement for CRM leads to maintain sales process integrity. Implemented logic using @api.onchange on the stage_id field to prevent users from moving a lead back to an earlier pipeline stage based on sequence comparison.
The solution validates stage transitions in real time and raises user-friendly validation errors when backward movement is attempted, ensuring consistent CRM workflow control without modifying core Odoo code.
<br>
<br>Key Responsibilities:<br>
<ul>

<li>Inherited and extended the crm.lead model safely</li>

<li>Implemented stage sequence validation logic</li>

<li>Prevented backward pipeline transitions using business rules</li>

<li>Integrated custom validation with Odoo CRM views</li>

<li>Maintained upgrade-safe customization</li>
</ul>
<br>
<br>Technologies Used:<br>
Python, Odoo CRM, Odoo ORM, XML Views, PostgreSQL

# crm_lead_stage_restriction_and_filter
Developed a custom Odoo CRM module that enforces forward-only stage movement for CRM leads to maintain sales process integrity. Implemented logic using @api.onchange on the stage_id field to prevent users from moving a lead back to an earlier pipeline stage based on sequence comparison.

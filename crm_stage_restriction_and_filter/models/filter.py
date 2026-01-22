from odoo import models,api
from odoo.exceptions import ValidationError

class inheritCrmFilterClass(models.Model):
    _inherit = 'crm.lead'

    # def write(self, vals):
    #     if 'stage_id' in vals:
    #         new_stage=self.env['crm.stage'].browse(vals['stage_id'])
    #
    #         for lead in self:
    #             if lead.stage_id and new_stage:
    #                 if new_stage.sequence < lead.stage_id.sequence:
    #                     raise ValidationError("You cannot move the lead backwards.")
    #     return super().write(vals)


    @api.onchange('stage_id')
    def onchange_stage_no_backward(self):
        if self._origin:
            old_stage = self._origin.stage_id
            new_stage = self.stage_id
            if old_stage and new_stage:
                if new_stage.sequence < old_stage.sequence:
                    raise ValidationError("No. cannot go backwards")
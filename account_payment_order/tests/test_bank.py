# © 2017 Creu Blanca
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestBank(TransactionCase):

    def test_bank(self):
        bank = self.env['res.bank'].search([], limit=1)
        self.assertTrue(bank)
        with self.assertRaises(ValidationError):
            bank.bic = "TEST"

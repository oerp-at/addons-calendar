# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.tools.sql import column_exists, create_column


def migrate(cr, version):
    """Odoo 20 dropped the timezone of resource.calendar; the booking type keeps
    the one of its availability calendar."""
    if not version or column_exists(cr, "resource_booking_type", "tz"):
        return
    create_column(cr, "resource_booking_type", "tz", "varchar")
    if column_exists(cr, "resource_calendar", "tz"):
        cr.execute(
            """
            UPDATE resource_booking_type rbt
               SET tz = rc.tz
              FROM resource_calendar rc
             WHERE rc.id = rbt.resource_calendar_id
            """
        )
    cr.execute(
        """
        UPDATE resource_booking_type rbt
           SET tz = COALESCE(c.tz, 'UTC')
          FROM res_company c
         WHERE rbt.tz IS NULL AND c.id = rbt.company_id
        """
    )
    cr.execute("UPDATE resource_booking_type SET tz = 'UTC' WHERE tz IS NULL")

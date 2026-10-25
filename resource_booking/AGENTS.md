# resource_booking

## Purpose

Appointments and resource booking on Community: booking types
(`resource.booking.type`) with an availability calendar and a timezone, resource
combinations (`resource.booking.combination`), bookings (`resource.booking`) that
create a `calendar.event`, and a portal page where the customer picks a slot.

## Notes for 20.0

- Migrated from 19.0 in this fork (no upstream migration pull request yet).
- `resource.calendar` has no timezone in 20.0: the booking type carries `tz`
  (migration `20.0.1.0.0` takes it over from the availability calendar); the work
  intervals of a resource are read in `resource.resource.tz`.
- `_work_intervals_batch` / `_leave_intervals_batch` take `resources_per_tz`
  (`{ZoneInfo: resources}`), not `resources` and `tz`.
- Access is in `security/ir.access.csv` (group rows are ORed, rows without group
  are global and ANDed).
- Depends on `web_calendar_slot_duration` (OCA/web), migrated in the
  `oerp-at/addons-web` fork.

## Tests

- `--test-tags /resource_booking`; the portal tours need Chrome. `BaseCommon`
  in 20.0 runs as its test user - give it the groups a test needs.

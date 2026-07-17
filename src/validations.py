from constants import YES, NO, TRACKING_DIGITS, ZIP_DIGITS


yes_or_no = lambda s: s in (YES, NO)
valid_tracking = lambda s: s.strip().isnumeric() and len(s.strip()) == TRACKING_DIGITS
valid_zip = lambda s: s.strip().isnumeric() and len(s.strip()) == ZIP_DIGITS

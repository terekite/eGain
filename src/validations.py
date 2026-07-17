from constants import YES, NO, TRACKING_DIGITS, ZIP_DIGITS


"""
This file contains some examples of how unexpected user inputs are handled.
These validation functions are passed to the Prompt constructor and it calls
them on the user input, then the Prompt object will output an unexpected input
message and essentially restart itself if it doesn't pass the validation.
For more expansive validations, this process could be altered or further designed
to handle other cases.
"""

yes_or_no = lambda s: s in (YES, NO)
valid_tracking = lambda s: s.strip().isnumeric() and len(s.strip()) == TRACKING_DIGITS
valid_zip = lambda s: s.strip().isnumeric() and len(s.strip()) == ZIP_DIGITS
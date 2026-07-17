from constants import MESSAGES, YES, NO
import validations
from prompt import Prompt
from prompt_chain import PromptChain


# Step 1: set up the prompt objects and their validations.
start = Prompt(MESSAGES.START, validations.yes_or_no)
tracking = Prompt(MESSAGES.TRACKING, validations.valid_tracking)
no_tracking = Prompt(MESSAGES.NO_TRACKING, validations.yes_or_no)
zip_code = Prompt(MESSAGES.ZIP_CODE, validations.valid_zip)
closest_office = Prompt(MESSAGES.CLOSEST_OFFICE, validations.yes_or_no)
package_info = Prompt(MESSAGES.PACKAGE_INFO, validations.yes_or_no)
agent = Prompt(MESSAGES.AGENT, validations.yes_or_no)
restart = Prompt(MESSAGES.RESTART, validations.yes_or_no)

# Step 2: connect the prompts together according to the flowchart.
start.set_next({YES: tracking, NO: no_tracking})
tracking.set_next(package_info)
no_tracking.set_next({YES: zip_code, NO: restart})
zip_code.set_next(closest_office)
closest_office.set_next({YES: start, NO: None})
package_info.set_next({YES: agent, NO: restart})
agent.set_next({YES: start, NO: None})
restart.set_next({YES: start, NO: None})

# Step 3: create a chain of prompts, and run the tool.
PromptChain(start).run()
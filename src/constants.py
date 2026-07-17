TRACKING_DIGITS = 10
ZIP_DIGITS = 5
QUIT = "Q"
YES = "Y"
NO = "N"


class MESSAGES:

  
  START = f"""Do you have a tracking number?
    Answer {YES} or {NO}: """

  TRACKING = f"""What is your tracking number?
    Enter a {TRACKING_DIGITS}-digit number: """

  NO_TRACKING = f"""Please go into your nearest post office.
\nWould you like assistance finding your nearest post office?
    Answer {YES} or {NO}: """

  ZIP_CODE = f"""Please enter your zip code.
    Enter a {ZIP_DIGITS}-digit number: """

  CLOSEST_OFFICE = f"""The closest office to you is at 88 Sunny Rd, Sunnyvale, CA 98989.
\nWould you like to track another lost package?
    Answer {YES} or {NO}: """

  PACKAGE_INFO = f"""Here is the updated tracking information:
    Package is currently in transit at a processing facility in Sunnyvale, CA.
    Scheduled delivery is August 1st, 2026.
\nWould you like to speak with an agent?
    Answer {YES} or {NO}: """

  AGENT = f"""Please use your phone to call (888) 888-8888 and speak with an agent.
\nWould you like to track another lost package?
    Answer {YES} or {NO}: """

  RESTART = f"""Thank you for using the tracking service.
\nWould you like to track another lost package?
    Answer {YES} or {NO}: """

  INVALID_INPUT_DEFAULT = "Invalid user input, please try again."

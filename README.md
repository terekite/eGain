# eGain
Package tracking tool

1. Setup/installation instructions
- Make sure python is installed.
- Navigate to the src directory in your terminal.
- Run main.py using python (python main.py or python3 main.py or equivalent).
   
2. Explanation of approach
My approach for implementing this was in 3 steps. Firstly, create Prompt objects for all of the possible prompts that may
come up throughout the tool. A Prompt is an object which contains a message and an input validations, displays/prompts
the user for input, then decides which prompt to go to next. The second step was to wire these prompts together so that
they follow the specifications of the flowchart I made by calling set_next() on the prompt objects. This function can
handle next prompts which rely on user input (such as "Y" for yes or "N" for no), as well as prompts that move directly
to another prompt. The third final step was to start the loop by creating a PromptChain object and calling run() on it,
providing it with a starting prompt. The PromptChain is essentially the chatbot, which loops until the next prompt is null.

3. Screenshots

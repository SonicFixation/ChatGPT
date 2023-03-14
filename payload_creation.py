from config import SCENARIOS

# -- get scenario prompt from config
def get_scenario(input):
    return SCENARIOS.get(input)


# -- start the message history scenario
def create_message_history_list(input):
    scenario = get_scenario(input) or input
    message_history = [{"role": "user", "content": scenario},
                        {"role": "assistant", "content": "OK"}]

    return message_history


# -- functions for creating message history dicts
def user_content(content):
    return {"role": "user", "content": f"{content}"}

def assistant_content(content):
    return {"role": "assistant", "content": f"{content}"}

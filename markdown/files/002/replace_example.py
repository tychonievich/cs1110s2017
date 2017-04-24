import re

text = 'Special Agent Upsorn told Special Agent Stephanie a secret'
# replace the agent's name with 'redacted'

# find a match
# replace that match with '*redacted*'

regex = re.compile(r'Agent [A-Z][a-z]+')
for match_obj in regex.finditer(text):
    print(match_obj.group())

string = regex.sub('*redacted*', text)
print(string)

# agent_name_regex = re.compile(r"Agent (\w)\w*")
# agent_name_regex = re.compile(r"Agent ([A-Z])[a-z]*")
# agent_name_regex = re.compile(r"Agent ([A-Z])([a-z])[a-z]*")

agent_name_regex = re.compile(r"(Agent )([A-Z])([a-z])[a-z]*")    # make regex into 3 group and use group 2 in replacement
string = agent_name_regex.sub(r"\1*redacted*", text)      # replace with the 1st group followed by *redacted*
print("1st group:", string)
string = agent_name_regex.sub(r"####\2*redacted*", text)
print("2nd group:", string)



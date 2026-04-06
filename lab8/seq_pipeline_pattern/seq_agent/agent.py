from google.adk.agents import SequentialAgent

from seq_agent.seq_exe_agent import agent2
from seq_agent.text_to_sql_agent import agent1

# Orchestrate the Pipeline
root_agent = SequentialAgent(
    name="BiqQueryPipeline",
    sub_agents=[agent1, agent2]
)

from google.adk.agents import SequentialAgent
from google.adk.agents.llm_agent import LlmAgent

from agents.delivery_agent import delivery_agent
from agents.order_agent import order_agent
from agents.inventory_agent import inventory_agent

# Orchestrate the Order Approval Workflow
order_creation_workflow_agent = SequentialAgent(
    name="OrderManagementWorkflowAgent",
    sub_agents=[order_agent, inventory_agent]
)

# The Coordinator (Dispatcher)
root_agent = LlmAgent(
    name="CoordinatorAgent",
    # The instructions guide the routing logic
    instruction="Analyze user intent. Route order management requests to OrderManagementWorkflowAgent and order delivery management requests to DeliveryServiceAgent.",
    sub_agents=[order_creation_workflow_agent, delivery_agent]
)

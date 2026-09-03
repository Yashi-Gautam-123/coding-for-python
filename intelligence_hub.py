agent_registry = {
    "Agent_Alpha": {
        "Location": (10, 20),
        "Knowledge": {"grid_map", "comm_protocol", "telemetry_sync"},
    },
    "Agent_Beta":{
        "Location": (15, 5),
        "Knowledge": {"grid_map", "comm_protocol", "power_grid"},
    },
    "Agent_Gamma":{
        "Location": (0,0),
        "Knowledge": {"grid_map","comm_protocol", "power_grid", "telemetry_sync"},
    },
        
}
movement_log = {}

def find_common_intelligence(registry):
    knowledge_sets = [
        agent_data["Knowledge"]
        for agent_data in registry.values()
    ]
    return set.intersection(*knowledge_sets)

def relocate_agent(registry, log, agent_id, new_location):
    current_location = registry[agent_id]["Location"]
    print("Attempting to change the location tuple directly...")
    try:
        current_location[0] = new_location[0]
    except TypeError as error:
        print("TypeError caught!", error)
        print("Tuples are immutable, reassigning a new tuple instead")
        

    registry[agent_id]["Location"] = new_location
    log.setdefault(agent_id, []).append(new_location)

print("---Common Intelligence Across All Agents---")
common_knowledge = find_common_intelligence(agent_registry)
print(common_knowledge)
print()
print("---Reloacting Agent_Alpha----")

relocate_agent(agent_registry, movement_log, "Agent_Alpha", (12,22))
print()
print("Aget Alpha new state:")
print(agent_registry["Agent_Alpha"])

print()
print("Movement Log:", movement_log)


print()
print("----Relocating Agent_Alpha Again---")

agent_registry["Agent_Alpha"]["Locatio"] = (14, 25)
movement_log.setdefault("Agent_Alpha", []).append((14, 25))
print("movement log:", movement_log)
                        

print()
print("---Summary Report---")
summary_report = {
    agent_id: len(data["Knowledge"])
    for agent_id, data in agent_registry.items()
}
print(summary_report)



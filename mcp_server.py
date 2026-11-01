# -*- coding: utf-8 -*-
"""
Personal Agent Hydration Osmolality Electrolyte FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import PersonalAgentHydrationOsmolalityElectrolyte

mcp = FastMCP("genpark-personal-agent-hydration-osmolality-electrolyte-skill")
hydration = PersonalAgentHydrationOsmolalityElectrolyte()

@mcp.tool()
def estimate_hourly_sweat_and_electrolyte_loss(
    ambient_temp_c: float,
    activity_met_level: float = 2.0,
    duration_hours: float = 2.0,
    body_mass_kg: float = 70.0
) -> str:
    """
    Estimates sweat volume and sodium/potassium electrolyte losses based on ambient temperature and MET level.
    """
    res = hydration.estimate_hourly_sweat_and_electrolyte_loss(ambient_temp_c, activity_met_level, duration_hours, body_mass_kg)
    return json.dumps(res, indent=2)

@mcp.tool()
def evaluate_subclinical_dehydration_cognitive_deficit(
    body_mass_kg: float,
    fluid_intake_liters: float,
    fluid_loss_liters: float
) -> str:
    """
    Evaluates subclinical dehydration body mass loss percentage and cognitive performance penalty.
    """
    res = hydration.evaluate_subclinical_dehydration_cognitive_deficit(body_mass_kg, fluid_intake_liters, fluid_loss_liters)
    return json.dumps(res, indent=2)

@mcp.tool()
def generate_personalized_hydration_schedule(
    waking_hours: int = 16,
    body_mass_kg: float = 70.0,
    planned_exercise_hours: float = 1.0,
    exercise_intensity_met: float = 6.0
) -> str:
    """
    Generates personalized hourly fluid and electrolyte replenishment targets.
    """
    res = hydration.generate_personalized_hydration_schedule(waking_hours, body_mass_kg, planned_exercise_hours, exercise_intensity_met)
    return json.dumps(res, indent=2)

def main():
    print("Testing Hydration Osmolality Electrolyte FastMCP Server:")
    print(estimate_hourly_sweat_and_electrolyte_loss(26.0, 3.5, 1.5, 75.0))

if __name__ == "__main__":
    main()

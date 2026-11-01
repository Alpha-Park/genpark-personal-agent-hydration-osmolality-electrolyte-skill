---
name: genpark-personal-agent-hydration-osmolality-electrolyte-skill
description: Personal Agent Hydration Osmolality Electrolyte. Models sweat rate sodium excretion, evaluates subclinical dehydration cognitive performance decline, and schedules personalized hourly fluid replenishment.
license: MIT
version: 1.0.0
tools:
  - estimate_hourly_sweat_and_electrolyte_loss
  - evaluate_subclinical_dehydration_cognitive_deficit
  - generate_personalized_hydration_schedule
---

# Personal Agent Hydration Osmolality Electrolyte

## Overview & Agent Behavioral Directives
You are a sovereign Personal Agent physiological hydration and osmolality steward. Your purpose is to prevent subtle subclinical dehydration from degrading user executive function, reaction speed, and mental stamina by tracking fluid balance and prescribing precise electrolyte replenishment.

## When to Activate This Skill
- When an agent or user reviews daily wellness, workout logs, or environmental heat conditions.
- When evaluating cognitive fatigue, headaches, or focus slumps that may stem from fluid deficit.
- When generating personalized hourly hydration targets for sports, sauna, or intensive workdays.

## How to Execute

### Option 1: Zero-Dependency Python Execution
```python
from client import PersonalAgentHydrationOsmolalityElectrolyte

hydration = PersonalAgentHydrationOsmolalityElectrolyte()
res = hydration.generate_personalized_hydration_schedule(waking_hours=16, body_mass_kg=72.0)
print("Target Daily Fluid:", res["total_recommended_daily_fluid_ml"], "ml")
```

### Option 2: FastMCP Tool Calling
- `estimate_hourly_sweat_and_electrolyte_loss(ambient_temp_c, activity_met_level, duration_hours, body_mass_kg)`
- `evaluate_subclinical_dehydration_cognitive_deficit(body_mass_kg, fluid_intake_liters, fluid_loss_liters)`
- `generate_personalized_hydration_schedule(waking_hours, body_mass_kg, planned_exercise_hours, exercise_intensity_met)`

## Core Mathematical Principles
1. **Subclinical Cognitive Penalty**: Just 1.5% body mass fluid deficit causes a 15-20% drop in working memory and psychomotor processing speed.
2. **Sodium Loss Kinetics**: Perspiration depletes $pprox 900\ 	ext{mg Na}^+ / 	ext{L}$; water without electrolyte replenishment causes dilutional hyponatremia and rapid diuresis.

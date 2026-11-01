# -*- coding: utf-8 -*-
import json
from client import PersonalAgentHydrationOsmolalityElectrolyte

hydration = PersonalAgentHydrationOsmolalityElectrolyte()

print("=" * 64)
print("DEMO: Personal Hydration & Osmolality Electrolyte Optimizer")
print("=" * 64)

# 1. Estimate sweat & electrolyte loss
sweat = hydration.estimate_hourly_sweat_and_electrolyte_loss(ambient_temp_c=28.0, activity_met_level=5.5, duration_hours=1.5, body_mass_kg=75.0)
print(f"\n1. Sweat & Sodium Loss (28°C, 5.5 METs for 1.5 Hours):")
print(f"   Sweat Rate: {sweat['hourly_sweat_rate_liters']} L/h -> Total Loss: {sweat['total_fluid_loss_liters']} Liters")
print(f"   Total Electrolyte Deficit: {sweat['total_sodium_loss_mg']} mg Sodium ({sweat['sweat_intensity_tier']})")

# 2. Evaluate cognitive performance deficit
deficit = hydration.evaluate_subclinical_dehydration_cognitive_deficit(body_mass_kg=75.0, fluid_intake_liters=0.5, fluid_loss_liters=2.2)
print(f"\n2. Subclinical Dehydration Impact:")
print(f"   Body Mass Fluid Loss: {deficit['body_mass_loss_pct']}%")
print(f"   Cognitive Impairment: {deficit['cognitive_impairment_pct']}% ({deficit['hydration_status']})")
print(f"   Immediate Intake Prescribed: {deficit['immediate_intake_recommended_ml']} ml")

# 3. Personalized daily schedule
plan = hydration.generate_personalized_hydration_schedule(waking_hours=16, body_mass_kg=75.0, planned_exercise_hours=1.0, exercise_intensity_met=6.0)
print(f"\n3. Daily Hydration Architecture:")
print(f"   Daily Fluid Target: {plan['total_recommended_daily_fluid_ml']} ml ({plan['total_recommended_sodium_mg']} mg Sodium)")
print(f"   Hourly Intake: ~{plan['target_hourly_intake_ml']} ml/hour")
print(f"   Protocol: {plan['guideline']}")

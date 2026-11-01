# -*- coding: utf-8 -*-
"""
Personal Agent Hydration Osmolality Electrolyte Client
Zero-dependency sweat rate sodium loss estimator, subclinical dehydration cognitive
deficit modeler, and personalized fluid/electrolyte schedule generator.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentHydrationOsmolalityElectrolyte:
    """
    Models human fluid dynamics, sweat sodium excretion, and subclinical dehydration
    cognitive performance penalties to maintain peak executive function.
    """

    def estimate_hourly_sweat_and_electrolyte_loss(
        self,
        ambient_temp_c: float,
        activity_met_level: float = 2.0,
        duration_hours: float = 2.0,
        body_mass_kg: float = 70.0
    ) -> Dict[str, Any]:
        """
        Estimates total fluid and sodium loss based on ambient temperature and MET metabolic intensity.
        Sweat Rate (L/h) = 0.45 + 0.035 * (Temp - 20) + 0.08 * (MET - 1.0)
        """
        temp = max(10.0, min(48.0, float(ambient_temp_c)))
        met = max(1.0, min(16.0, float(activity_met_level)))
        dur = max(0.25, min(12.0, float(duration_hours)))
        mass = max(35.0, min(180.0, float(body_mass_kg)))

        # Base sweat rate in Liters per hour
        base_sweat_rate = 0.45 + 0.035 * max(0.0, temp - 20.0) + 0.08 * (met - 1.0)
        mass_scaling = mass / 70.0
        hourly_sweat_liters = round(max(0.25, base_sweat_rate * mass_scaling), 2)
        total_fluid_loss_liters = round(hourly_sweat_liters * dur, 2)

        # Average sodium sweat concentration: 900 mg / Liter
        hourly_sodium_loss_mg = round(hourly_sweat_liters * 900.0, 1)
        total_sodium_loss_mg = round(hourly_sodium_loss_mg * dur, 1)

        # Potassium sweat loss: approx 200 mg / Liter
        total_potassium_loss_mg = round(total_fluid_loss_liters * 200.0, 1)

        return {
            "ambient_temp_c": temp,
            "met_intensity": met,
            "duration_hours": dur,
            "hourly_sweat_rate_liters": hourly_sweat_liters,
            "total_fluid_loss_liters": total_fluid_loss_liters,
            "total_sodium_loss_mg": total_sodium_loss_mg,
            "total_potassium_loss_mg": total_potassium_loss_mg,
            "sweat_intensity_tier": "HEAVY_PERSPIRATION" if hourly_sweat_liters >= 1.2 else ("MODERATE_PERSPIRATION" if hourly_sweat_liters >= 0.6 else "LIGHT_INSENSIBLE")
        }

    def evaluate_subclinical_dehydration_cognitive_deficit(
        self,
        body_mass_kg: float,
        fluid_intake_liters: float,
        fluid_loss_liters: float
    ) -> Dict[str, Any]:
        """
        Calculates body mass loss % from net fluid deficit and predicts cognitive performance degradation.
        Cognitive Impairment % = min(40.0, 12.0 * (Deficit_pct)^1.25)
        """
        mass = max(35.0, min(180.0, float(body_mass_kg)))
        in_fluid = max(0.0, float(fluid_intake_liters))
        out_fluid = max(0.0, float(fluid_loss_liters))

        net_deficit_liters = max(0.0, out_fluid - in_fluid)
        # 1 Liter water = 1 kg
        body_mass_loss_pct = round((net_deficit_liters / mass) * 100.0, 2)

        # Impairment model
        if body_mass_loss_pct >= 0.75:
            impairment_pct = round(min(45.0, 12.0 * math.pow(body_mass_loss_pct, 1.25)), 1)
        else:
            impairment_pct = 0.0

        if body_mass_loss_pct >= 2.5:
            verdict = "SEVERE_DEHYDRATION_IMPAIRMENT (Pronounced executive dysfunction, headache, fatigue)"
        elif body_mass_loss_pct >= 1.2:
            verdict = "SUBCLINICAL_COGNITIVE_DECLINE (15-20% slower reaction time & working memory loss)"
        elif body_mass_loss_pct >= 0.5:
            verdict = "MILD_FLUID_DEFICIT (Minor attention drift)"
        else:
            verdict = "OPTIMAL_EUHYDRATED_STATE"

        return {
            "net_fluid_deficit_liters": round(net_deficit_liters, 2),
            "body_mass_loss_pct": body_mass_loss_pct,
            "cognitive_impairment_pct": impairment_pct,
            "hydration_status": verdict,
            "immediate_intake_recommended_ml": int(net_deficit_liters * 1000) if net_deficit_liters > 0 else 0
        }

    def generate_personalized_hydration_schedule(
        self,
        waking_hours: int = 16,
        body_mass_kg: float = 70.0,
        planned_exercise_hours: float = 1.0,
        exercise_intensity_met: float = 6.0
    ) -> Dict[str, Any]:
        """
        Generates hourly water and electrolyte intake schedule ensuring euhydration.
        Baseline need: 35 ml / kg / day + Exercise loss.
        """
        mass = max(35.0, min(180.0, float(body_mass_kg)))
        baseline_fluid_ml = mass * 35.0

        # Exercise loss
        ex_hours = max(0.0, min(6.0, float(planned_exercise_hours)))
        ex_loss = self.estimate_hourly_sweat_and_electrolyte_loss(24.0, exercise_intensity_met, ex_hours, mass)
        ex_fluid_ml = ex_loss["total_fluid_loss_liters"] * 1000.0

        total_daily_fluid_ml = round(baseline_fluid_ml + ex_fluid_ml, 0)
        total_sodium_needed_mg = round(ex_loss["total_sodium_loss_mg"] + 1500.0, 0)

        # Distribute over waking hours (e.g. 16 hours)
        hourly_rate_ml = round(total_daily_fluid_ml / max(1, waking_hours), 0)

        return {
            "body_mass_kg": mass,
            "baseline_daily_fluid_need_ml": int(baseline_fluid_ml),
            "exercise_fluid_loss_ml": int(ex_fluid_ml),
            "total_recommended_daily_fluid_ml": int(total_daily_fluid_ml),
            "total_recommended_sodium_mg": int(total_sodium_needed_mg),
            "target_hourly_intake_ml": int(hourly_rate_ml),
            "wake_bolus_recommendation_ml": 500,
            "guideline": f"Drink ~{int(hourly_rate_ml)} ml water per waking hour; front-load 500ml upon waking with a pinch of sea salt."
        }

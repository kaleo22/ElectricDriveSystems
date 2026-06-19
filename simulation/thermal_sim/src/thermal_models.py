from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp


def steady_temperature(
    ambient_temperature_c: float,
    power_loss_w: float,
    thermal_resistance_c_per_w: float,
) -> float:
    return ambient_temperature_c + power_loss_w * thermal_resistance_c_per_w


def thermal_time_constant(
    thermal_resistance_c_per_w: float,
    thermal_capacitance_j_per_c: float,
) -> float:
    return thermal_resistance_c_per_w * thermal_capacitance_j_per_c


def first_order_thermal_response(
    time_s,
    initial_temperature_c: float,
    ambient_temperature_c: float,
    power_loss_w: float,
    thermal_resistance_c_per_w: float,
    thermal_capacitance_j_per_c: float,
):
    time_s = np.asarray(time_s)

    t_steady = steady_temperature(
        ambient_temperature_c,
        power_loss_w,
        thermal_resistance_c_per_w,
    )

    tau = thermal_time_constant(
        thermal_resistance_c_per_w,
        thermal_capacitance_j_per_c,
    )

    return t_steady + (initial_temperature_c - t_steady) * np.exp(-time_s / tau)


def simulate_single_component_ode(
    time_span_s: tuple[float, float],
    initial_temperature_c: float,
    ambient_temperature_c: float,
    power_loss_w: float,
    thermal_resistance_c_per_w: float,
    thermal_capacitance_j_per_c: float,
    number_of_points: int = 1000,
):
    def rhs(t, y):
        temperature_c = y[0]

        dtemperature_dt = (
            power_loss_w
            - (temperature_c - ambient_temperature_c) / thermal_resistance_c_per_w
        ) / thermal_capacitance_j_per_c

        return [dtemperature_dt]

    t_eval = np.linspace(
        time_span_s[0],
        time_span_s[1],
        number_of_points,
    )

    solution = solve_ivp(
        rhs,
        time_span_s,
        [initial_temperature_c],
        t_eval=t_eval,
        method="RK45",
    )

    return solution.t, solution.y[0]


def simulate_pcb_coupled_network(
    time_span_s: tuple[float, float],
    initial_temperatures_c: dict[str, float],
    powers_w: dict[str, float],
    component_to_pcb_resistances_c_per_w: dict[str, float],
    component_capacitances_j_per_c: dict[str, float],
    pcb_ambient_resistance_c_per_w: float,
    pcb_capacitance_j_per_c: float,
    ambient_temperature_c: float,
    number_of_points: int = 1000,
):
    component_names = list(powers_w.keys())

    if "PCB" in component_names:
        raise ValueError("'PCB' is reserved for the board node.")

    y0 = [initial_temperatures_c[name] for name in component_names]
    y0.append(initial_temperatures_c["PCB"])

    def rhs(t, y):
        pcb_temperature = y[-1]
        derivatives = []
        heat_into_pcb_w = 0.0

        for index, name in enumerate(component_names):
            component_temperature = y[index]
            resistance_to_pcb = component_to_pcb_resistances_c_per_w[name]
            capacitance = component_capacitances_j_per_c[name]
            power = powers_w[name]

            heat_to_pcb = (component_temperature - pcb_temperature) / resistance_to_pcb
            heat_into_pcb_w += heat_to_pcb

            dtemperature_dt = (power - heat_to_pcb) / capacitance
            derivatives.append(dtemperature_dt)

        pcb_heat_to_ambient = (
            pcb_temperature - ambient_temperature_c
        ) / pcb_ambient_resistance_c_per_w

        dpcb_dt = (heat_into_pcb_w - pcb_heat_to_ambient) / pcb_capacitance_j_per_c
        derivatives.append(dpcb_dt)

        return derivatives

    t_eval = np.linspace(
        time_span_s[0],
        time_span_s[1],
        number_of_points,
    )

    solution = solve_ivp(
        rhs,
        time_span_s,
        y0,
        t_eval=t_eval,
        method="RK45",
    )

    results = {
        name: solution.y[index]
        for index, name in enumerate(component_names)
    }

    results["PCB"] = solution.y[-1]

    return solution.t, results


def thermal_status(temperature_c: float) -> str:
    if temperature_c < 80.0:
        return "OK"
    if temperature_c < 100.0:
        return "Warm"
    if temperature_c < 125.0:
        return "Check"
    if temperature_c < 150.0:
        return "Critical"

    return "Too hot"
"""
Loss models for a simplified thermal simulation of a PWM-driven DC motor controller.

The equations are intentionally lightweight and transparent.
They are suitable for early design estimation and live demonstrations,
but not a replacement for FEM/CFD or detailed SPICE switching simulations.
"""

from __future__ import annotations


def mosfet_rds_on_temperature(
    rds_on_25: float,
    temperature_c: float,
    alpha: float = 0.005,
) -> float:
    """
    Estimate MOSFET R_DS(on) as a function of junction temperature.

    Parameters
    ----------
    rds_on_25:
        Drain-source on-resistance at 25 °C in ohms.
    temperature_c:
        Junction temperature in °C.
    alpha:
        Linear temperature coefficient in 1/°C.

    Returns
    -------
    float
        Temperature-dependent R_DS(on) in ohms.
    """
    return rds_on_25 * (1.0 + alpha * (temperature_c - 25.0))


def mosfet_conduction_loss(
    current_a: float,
    duty: float,
    rds_on_ohm: float,
) -> float:
    """
    MOSFET conduction loss under PWM operation.

    Approximation:
        P_cond = I^2 * D * R_DS(on)

    Assumes approximately constant motor current during the PWM cycle.
    """
    return current_a**2 * duty * rds_on_ohm


def mosfet_switching_loss(
    voltage_v: float,
    current_a: float,
    rise_time_s: float,
    fall_time_s: float,
    pwm_frequency_hz: float,
) -> float:
    """
    Approximate MOSFET switching loss.

    Approximation:
        P_sw = 0.5 * V_DS * I_D * (t_r + t_f) * f_PWM
    """
    return 0.5 * voltage_v * current_a * (rise_time_s + fall_time_s) * pwm_frequency_hz


def mosfet_gate_drive_loss(
    gate_charge_c: float,
    gate_voltage_v: float,
    pwm_frequency_hz: float,
) -> float:
    """
    Gate drive loss.

    Approximation:
        P_gate = Q_g * V_GS * f_PWM

    This loss is mainly dissipated in the gate driver and gate resistance,
    not necessarily in the MOSFET silicon itself.
    """
    return gate_charge_c * gate_voltage_v * pwm_frequency_hz


def diode_loss(
    forward_voltage_v: float,
    current_a: float,
    duty: float,
) -> float:
    """
    Freewheel diode loss.

    Approximation:
        P_diode = V_F * I * (1 - D)
    """
    return forward_voltage_v * current_a * (1.0 - duty)


def linear_regulator_loss(
    input_voltage_v: float,
    output_voltage_v: float,
    output_current_a: float,
) -> float:
    """
    Linear regulator loss.

    Equation:
        P = (V_in - V_out) * I_out
    """
    return (input_voltage_v - output_voltage_v) * output_current_a


def buck_converter_loss(
    output_voltage_v: float,
    output_current_a: float,
    efficiency: float,
) -> float:
    """
    Buck converter loss from assumed efficiency.

    Equation:
        P_loss = P_out * (1 / eta - 1)
    """
    if not 0.0 < efficiency <= 1.0:
        raise ValueError("Efficiency must be in the range (0, 1].")

    p_out = output_voltage_v * output_current_a
    return p_out * (1.0 / efficiency - 1.0)


def shunt_loss(
    current_a: float,
    resistance_ohm: float,
) -> float:
    """
    Shunt resistor loss.

    Equation:
        P = I^2 * R
    """
    return current_a**2 * resistance_ohm


def trace_loss(
    current_a: float,
    trace_resistance_ohm: float,
) -> float:
    """
    PCB trace loss.

    Equation:
        P = I^2 * R_trace
    """
    return current_a**2 * trace_resistance_ohm


def motor_copper_loss(
    current_a: float,
    winding_resistance_ohm: float,
) -> float:
    """
    Motor winding copper loss.

    Equation:
        P_cu = I^2 * R_winding

    This is useful for estimating motor-side heating,
    but the motor should usually be treated as its own thermal system.
    """
    return current_a**2 * winding_resistance_ohm
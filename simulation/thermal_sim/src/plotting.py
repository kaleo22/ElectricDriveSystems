"""
Plotting helpers for thermal simulation notebooks.
"""

from __future__ import annotations

import matplotlib.pyplot as plt


def plot_temperature_bar(
    dataframe,
    component_column: str = "Component",
    temperature_column: str = "T steady [°C]",
    title: str = "Estimated steady-state component temperatures",
):
    """
    Plot steady-state temperatures as a bar chart.
    """
    plt.figure(figsize=(10, 5))
    plt.bar(dataframe[component_column], dataframe[temperature_column])

    plt.axhline(80, linestyle="--", label="80 °C")
    plt.axhline(100, linestyle="--", label="100 °C")
    plt.axhline(125, linestyle="--", label="125 °C")
    plt.axhline(150, linestyle="--", label="150 °C")

    plt.ylabel("Temperature [°C]")
    plt.xticks(rotation=30, ha="right")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_transient_temperatures(
    time_s,
    temperature_results: dict[str, object],
    title: str = "Transient thermal response",
):
    """
    Plot transient temperature curves.
    """
    plt.figure(figsize=(10, 5))

    for name, temperature_c in temperature_results.items():
        plt.plot(time_s, temperature_c, label=name)

    plt.axhline(80, linestyle="--")
    plt.axhline(100, linestyle="--")
    plt.axhline(125, linestyle="--")
    plt.axhline(150, linestyle="--")

    plt.xlabel("Time [s]")
    plt.ylabel("Temperature [°C]")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_parameter_sweep(
    x_values,
    y_values,
    xlabel: str,
    ylabel: str,
    title: str,
):
    """
    Plot a simple parameter sweep.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, marker="o")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
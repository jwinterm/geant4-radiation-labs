"""Generate annihilation_diagram.png for Lab 4.

A schematic of positron-electron annihilation in PET:
  F-18 nucleus -> emits a positron (e+) -> positron travels a short
  distance in tissue -> annihilates with an electron (e-) -> two 511 keV
  photons fly off back-to-back.

Layout: F-18 sits up and to the left, the positron path arcs down to an
annihilation point in the middle, and the two 511 keV photons fly off
horizontally left and right so they never overlap the positron path.
"""

import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(OUT_DIR, "annihilation_diagram.png")


def main() -> None:
    fig, ax = plt.subplots(figsize=(12, 6.4))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.4)
    ax.set_aspect("equal")
    ax.axis("off")

    # --- F-18 nucleus, upper left ----------------------------------------
    nucleus_xy = (1.7, 5.0)
    ax.add_patch(Circle(nucleus_xy, 0.45, facecolor="#3b6fb6",
                        edgecolor="black", linewidth=1.5, zorder=3))
    ax.text(*nucleus_xy, "F-18", ha="center", va="center",
            color="white", fontsize=12, fontweight="bold", zorder=4)
    ax.text(nucleus_xy[0], nucleus_xy[1] - 0.85,
            r"$\beta^+$ decay", ha="center", va="center", fontsize=10,
            style="italic", color="#222")

    # --- Annihilation point, middle-lower --------------------------------
    annihilation_xy = (6.0, 3.0)

    # --- Wavy positron path from nucleus down to annihilation point ------
    # Build a parametric curve from F-18 to the annihilation point with a
    # small sinusoidal wobble that follows the curve direction.
    t = np.linspace(0.05, 0.97, 240)
    base_x = nucleus_xy[0] + (annihilation_xy[0] - nucleus_xy[0]) * t
    base_y = nucleus_xy[1] + (annihilation_xy[1] - nucleus_xy[1]) * t
    # Tangent direction along the line.
    dx = annihilation_xy[0] - nucleus_xy[0]
    dy = annihilation_xy[1] - nucleus_xy[1]
    seg_len = np.hypot(dx, dy)
    nx, ny = -dy / seg_len, dx / seg_len  # unit normal
    wobble = 0.18 * np.sin(t * 9.0 * np.pi) * (1.0 - 0.4 * t)
    path_x = base_x + wobble * nx
    path_y = base_y + wobble * ny
    ax.plot(path_x, path_y, color="#d04545", linewidth=1.6, alpha=0.9, zorder=2)
    ax.annotate(
        "", xy=annihilation_xy, xytext=(path_x[-3], path_y[-3]),
        arrowprops=dict(arrowstyle="-|>", color="#d04545", lw=1.6),
        zorder=2,
    )

    # Positron label, placed to the side of the path so it doesn't collide
    # with the photon labels (which sit at y ~= 3.5).
    midpoint = (path_x[len(path_x) // 2] + 0.45, path_y[len(path_y) // 2] + 0.25)
    ax.text(*midpoint, r"$e^+$", color="#d04545", fontsize=15,
            fontweight="bold", ha="center")
    ax.text(midpoint[0] + 0.6, midpoint[1] - 0.55,
            "positron range\n(~1 mm in tissue)",
            ha="left", va="center", fontsize=9, color="#444")

    # --- Annihilation event marker + label -------------------------------
    ax.plot(*annihilation_xy, marker="*", markersize=46,
            markerfacecolor="gold", markeredgecolor="black",
            markeredgewidth=1.4, zorder=3)
    ax.text(annihilation_xy[0], annihilation_xy[1] - 0.95,
            "annihilation", ha="center", va="center",
            fontsize=10, fontweight="bold", color="#222")
    ax.text(annihilation_xy[0], annihilation_xy[1] - 1.32,
            r"$e^+ + e^- \to \gamma + \gamma$",
            ha="center", va="center", fontsize=11, color="#222")

    # --- Inbound electron from below the annihilation point --------------
    e_minus_xy = (annihilation_xy[0] + 0.95, annihilation_xy[1] - 0.05)
    ax.text(e_minus_xy[0] + 0.55, e_minus_xy[1] + 0.05,
            r"$e^-$", color="#1f6f3b", fontsize=15,
            fontweight="bold", ha="center", va="center")
    ax.annotate(
        "", xy=(annihilation_xy[0] + 0.32, annihilation_xy[1]),
        xytext=(e_minus_xy[0] + 0.30, e_minus_xy[1]),
        arrowprops=dict(arrowstyle="-|>", color="#1f6f3b", lw=1.6),
    )

    # --- Two 511 keV photons, horizontal, back-to-back -------------------
    photon_y = annihilation_xy[1]
    left_end = (0.6, photon_y)
    right_end = (11.4, photon_y)

    ax.add_patch(FancyArrowPatch(
        (annihilation_xy[0] - 0.35, photon_y), left_end,
        arrowstyle="-|>", mutation_scale=22, color="#b8860b", linewidth=2.2,
    ))
    ax.add_patch(FancyArrowPatch(
        (annihilation_xy[0] + 0.35, photon_y), right_end,
        arrowstyle="-|>", mutation_scale=22, color="#b8860b", linewidth=2.2,
    ))

    # Wavy decoration so the arrows read as electromagnetic waves.
    for x_lo, x_hi in [(0.8, 5.55), (6.45, 11.2)]:
        xs = np.linspace(x_lo, x_hi, 240)
        ys = photon_y + 0.13 * np.sin((xs - x_lo) * 4.5)
        ax.plot(xs, ys, color="#b8860b", linewidth=1.0, alpha=0.7)

    ax.text(2.8, photon_y + 0.55, r"$\gamma$  511 keV", color="#8a6308",
            fontsize=12, fontweight="bold", ha="center")
    ax.text(9.0, photon_y + 0.55, r"$\gamma$  511 keV", color="#8a6308",
            fontsize=12, fontweight="bold", ha="center")

    # --- Footer caption --------------------------------------------------
    ax.text(6.0, 0.55,
            "Two 511 keV photons fly back-to-back (180°) to conserve momentum.\n"
            "A PET ring detects coincident pairs and traces the line connecting "
            "them — the line of response.",
            ha="center", va="center", fontsize=10, color="#333")

    ax.set_title(
        "Positron-Electron Annihilation in PET",
        fontsize=14, fontweight="bold", pad=12,
    )

    plt.tight_layout()
    fig.savefig(OUT_PATH, dpi=200, bbox_inches="tight")
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()

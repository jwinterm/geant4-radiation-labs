"""Generate action_classes.png for Lab 3.

Shows the nested Geant4 user-action hierarchy (Run -> Event -> Step) as
three concentric boxes, each labelled with the corresponding B1 class and
the work that class will do after Lab 3's modifications.

Layout strategy: each layer reserves a "header strip" at its top for its
title and 2-3 body lines, and the next inner box starts BELOW that strip
so nothing overlaps.
"""

import os

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(OUT_DIR, "action_classes.png")

# Figure coordinates (data units = arbitrary).
FIG_W = 11.0
FIG_H = 7.4

# Outer Run box.
RUN_BOX = (0.4, 0.6, 10.2, 6.4)  # x, y, w, h
# Inner Event box. Top is 1.5 units below Run top to leave room for header.
EVENT_BOX = (1.05, 1.0, 8.9, 4.55)
# Innermost Step box. Top is 1.4 units below Event top.
STEP_BOX = (1.7, 1.45, 7.6, 2.7)

LAYERS = [
    {
        "rect": RUN_BOX,
        "color": "#cfe2ff",
        "title": "Run  —  RunAction",
        "lines": [
            "BeginOfRunAction():  open CSV file, define ntuple",
            "EndOfRunAction():     write & close CSV file",
        ],
    },
    {
        "rect": EVENT_BOX,
        "color": "#fff3cd",
        "title": "Event  —  EventAction",
        "lines": [
            "BeginOfEventAction():  reset fEdep = 0",
            "EndOfEventAction():     write fEdep to ntuple",
        ],
    },
    {
        "rect": STEP_BOX,
        "color": "#d4edda",
        "title": "Step  —  SteppingAction",
        "lines": [
            "UserSteppingAction():  add",
            "    aStep->GetTotalEnergyDeposit()",
            "to EventAction's running total",
        ],
    },
]


def main() -> None:
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.set_xlim(0, FIG_W)
    ax.set_ylim(0, FIG_H)
    ax.axis("off")

    # Draw boxes back-to-front so inner boxes paint over parent fills.
    for layer in LAYERS:
        x, y, w, h = layer["rect"]
        patch = FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.05",
            facecolor=layer["color"],
            edgecolor="black",
            linewidth=1.6,
        )
        ax.add_patch(patch)

    # Place title + body in each layer's header strip (above the inner box).
    for layer in LAYERS:
        x, y, w, h = layer["rect"]
        title_y = y + h - 0.45
        ax.text(
            x + 0.3,
            title_y,
            layer["title"],
            ha="left",
            va="center",
            fontsize=12,
            fontweight="bold",
        )
        for i, line in enumerate(layer["lines"]):
            ax.text(
                x + 0.45,
                title_y - 0.4 - i * 0.32,
                line,
                ha="left",
                va="center",
                fontsize=10,
                family="monospace",
            )

    ax.set_title(
        "Geant4 User-Action Hierarchy in Example B1\n"
        "(all classes are in namespace B1)",
        fontsize=13,
        fontweight="bold",
        pad=10,
    )

    ax.text(
        FIG_W / 2,
        0.25,
        "Each Run contains many Events; each Event contains many Steps.",
        ha="center",
        va="center",
        fontsize=10,
        style="italic",
        color="#444",
    )

    plt.tight_layout()
    fig.savefig(OUT_PATH, dpi=200, bbox_inches="tight")
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()

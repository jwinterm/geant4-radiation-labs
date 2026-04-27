"""Generate workflow_diagram.png for Lab 3.

Renders the Simulate -> Save -> Analyze -> Visualize cycle as four labelled
boxes connected by arrows. Re-run this script after editing to regenerate
the PNG.
"""

import os

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(OUT_DIR, "workflow_diagram.png")

BOXES = [
    {
        "title": "Geant4 Simulation",
        "subtitle": "C++ application\n(modified B1)",
        "color": "#cfe2ff",
    },
    {
        "title": "CSV File",
        "subtitle": "B1_output.csv\none row per event",
        "color": "#fff3cd",
    },
    {
        "title": "Python + pandas",
        "subtitle": "Load DataFrame\nfilter & summarize",
        "color": "#d4edda",
    },
    {
        "title": "Plots & Statistics",
        "subtitle": "matplotlib\nhistograms, CDFs",
        "color": "#f8d7da",
    },
]


def main() -> None:
    fig, ax = plt.subplots(figsize=(12, 3.6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 3.5)
    ax.axis("off")

    box_w, box_h = 2.5, 1.7
    gap = 0.4
    total_w = len(BOXES) * box_w + (len(BOXES) - 1) * gap
    x0 = (12 - total_w) / 2
    y0 = 0.85

    centers = []
    for i, b in enumerate(BOXES):
        x = x0 + i * (box_w + gap)
        centers.append((x + box_w / 2, y0 + box_h / 2))
        patch = FancyBboxPatch(
            (x, y0),
            box_w,
            box_h,
            boxstyle="round,pad=0.08",
            facecolor=b["color"],
            edgecolor="black",
            linewidth=1.5,
        )
        ax.add_patch(patch)
        ax.text(
            x + box_w / 2,
            y0 + box_h * 0.68,
            b["title"],
            ha="center",
            va="center",
            fontsize=12,
            fontweight="bold",
        )
        ax.text(
            x + box_w / 2,
            y0 + box_h * 0.28,
            b["subtitle"],
            ha="center",
            va="center",
            fontsize=10,
        )

    # Arrows between consecutive boxes.
    for (cx1, cy), (cx2, _) in zip(centers, centers[1:]):
        arrow = FancyArrowPatch(
            (cx1 + box_w / 2, cy),
            (cx2 - box_w / 2, cy),
            arrowstyle="-|>",
            mutation_scale=20,
            linewidth=1.6,
            color="black",
        )
        ax.add_patch(arrow)

    ax.set_title(
        "Lab 3 Workflow: Simulate → Save → Analyze → Visualize",
        fontsize=13,
        fontweight="bold",
        pad=12,
    )

    plt.tight_layout()
    fig.savefig(OUT_PATH, dpi=200, bbox_inches="tight")
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()

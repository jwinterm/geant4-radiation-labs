"""Generate analysis_manager_flow.png for Lab 3.

Shows how a single event's energy flows from per-step calls in
SteppingAction, through per-event accumulation in EventAction, into
G4AnalysisManager, and finally out to a CSV file. The diagram also
calls out the per-run setup/teardown in RunAction (open/write/close).
"""

import os

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(OUT_DIR, "analysis_manager_flow.png")

# Four boxes in the main left-to-right flow.
MAIN_BOXES = [
    {
        "title": "SteppingAction",
        "scope": "(per step)",
        "code": [
            "edepStep = aStep->",
            "  GetTotalEnergyDeposit();",
            "fEventAction->",
            "  AddEdep(edepStep);",
        ],
        "color": "#cfe2ff",
    },
    {
        "title": "EventAction",
        "scope": "(per event)",
        "code": [
            "fEdep += edepStep;",
            "",
            "// EndOfEventAction:",
            "FillNtupleDColumn(0, fEdep);",
            "AddNtupleRow();",
        ],
        "color": "#fff3cd",
    },
    {
        "title": "G4AnalysisManager",
        "scope": "(buffered)",
        "code": [
            "Buffers each row",
            "until run ends",
        ],
        "color": "#e2d4f0",
    },
    {
        "title": "CSV File",
        "scope": "(on disk)",
        "code": [
            "B1_output_nt_B1.csv",
            "",
            "Edep",
            "0.043",
            "0.512",
            "...",
        ],
        "color": "#d4edda",
    },
]


def main() -> None:
    fig, ax = plt.subplots(figsize=(13, 5.4))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 5.4)
    ax.axis("off")

    box_w, box_h = 2.7, 3.4
    gap = 0.45
    total_w = len(MAIN_BOXES) * box_w + (len(MAIN_BOXES) - 1) * gap
    x0 = (13 - total_w) / 2
    y0 = 1.1

    centers = []
    for i, b in enumerate(MAIN_BOXES):
        x = x0 + i * (box_w + gap)
        centers.append((x + box_w / 2, y0 + box_h / 2, x, x + box_w))
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
            y0 + box_h - 0.45,
            b["title"],
            ha="center",
            va="center",
            fontsize=11.5,
            fontweight="bold",
        )
        ax.text(
            x + box_w / 2,
            y0 + box_h - 0.85,
            b["scope"],
            ha="center",
            va="center",
            fontsize=9,
            style="italic",
            color="#444",
        )
        for j, line in enumerate(b["code"]):
            ax.text(
                x + 0.18,
                y0 + box_h - 1.30 - j * 0.32,
                line,
                ha="left",
                va="center",
                fontsize=9,
                family="monospace",
            )

    # Arrows between consecutive main boxes.
    arrow_y = y0 + box_h / 2
    for (_, _, _, right_a), (_, _, left_b, _) in zip(centers, centers[1:]):
        arrow = FancyArrowPatch(
            (right_a, arrow_y),
            (left_b, arrow_y),
            arrowstyle="-|>",
            mutation_scale=20,
            linewidth=1.6,
            color="black",
        )
        ax.add_patch(arrow)

    # RunAction callout: arrow from below pointing up at the AnalysisManager
    # box, with an explanatory label.
    am_cx = centers[2][0]
    am_left = centers[2][2]
    am_right = centers[2][3]
    callout_y_text = 0.38
    ax.text(
        am_cx,
        callout_y_text,
        "RunAction (per run)",
        ha="center",
        va="center",
        fontsize=10.5,
        fontweight="bold",
    )
    ax.text(
        am_cx,
        callout_y_text - 0.32,
        "BeginOfRunAction: OpenFile + CreateNtuple",
        ha="center",
        va="center",
        fontsize=9,
        family="monospace",
    )
    callout_arrow = FancyArrowPatch(
        (am_left + 0.2, callout_y_text + 0.18),
        (am_left + 0.2, y0 - 0.05),
        arrowstyle="-|>",
        mutation_scale=14,
        linewidth=1.2,
        color="#444",
        linestyle="dashed",
    )
    ax.add_patch(callout_arrow)

    # EndOfRunAction arrow from the AM box across to the CSV box.
    csv_left = centers[3][2]
    end_arrow = FancyArrowPatch(
        (am_right - 0.2, y0 - 0.05),
        (csv_left + 0.2, y0 - 0.05),
        arrowstyle="-|>",
        mutation_scale=14,
        linewidth=1.2,
        color="#444",
        linestyle="dashed",
        connectionstyle="arc3,rad=-0.25",
    )
    ax.add_patch(end_arrow)
    ax.text(
        (am_right + csv_left) / 2,
        y0 - 0.55,
        "EndOfRunAction: Write() + CloseFile()",
        ha="center",
        va="center",
        fontsize=9,
        family="monospace",
        color="#444",
    )

    ax.set_title(
        "Energy Data Flow: Step → Event → AnalysisManager → CSV",
        fontsize=13,
        fontweight="bold",
        pad=10,
    )

    plt.tight_layout()
    fig.savefig(OUT_PATH, dpi=200, bbox_inches="tight")
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()

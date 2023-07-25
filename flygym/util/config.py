import numpy as np
from typing import List


# DoF definitions
all_leg_dofs = [
    f"joint_{side}{pos}{dof}"
    for side in "LR"
    for pos in "FMH"
    for dof in [
        "Coxa",
        "Coxa_roll",
        "Coxa_yaw",
        "Femur",
        "Femur_roll",
        "Tibia",
        "Tarsus1",
    ]
]
leg_dofs_3_per_leg = [
    f"joint_{side}{pos}{dof}"
    for side in "LR"
    for pos in "FMH"
    for dof in ["Coxa" if pos == "F" else "Coxa_roll", "Femur", "Tibia"]
]


# Geometries
all_tarsi_links = [
    f"{side}{pos}Tarsus{i}" for side in "LR" for pos in "FMH" for i in range(1, 6)
]


def get_collision_geoms(config: str = "all") -> List[str]:
    if config == "legs":
        return [
            f"{side}{pos}{dof}_collision"
            for side in "LR"
            for pos in "FMH"
            for dof in [
                "Coxa",
                "Femur",
                "Tibia",
                "Tarsus1",
                "Tarsus2",
                "Tarsus3",
                "Tarsus4",
                "Tarsus5",
            ]
        ]
    elif config == "legs-no-coxa":
        return [
            f"{side}{pos}{dof}_collision"
            for side in "LR"
            for pos in "FMH"
            for dof in [
                "Femur",
                "Tibia",
                "Tarsus1",
                "Tarsus2",
                "Tarsus3",
                "Tarsus4",
                "Tarsus5",
            ]
        ]
    elif config == "tarsi":
        return [
            f"{side}{pos}{dof}_collision"
            for side in "LR"
            for pos in "FMH"
            for dof in ["Tarsus1", "Tarsus2", "Tarsus3", "Tarsus4", "Tarsus5"]
        ]
    elif config == "none":
        return []
    else:
        raise ValueError(f"Unknown collision geometry configuration: {config}")


# Vision
# fovx_per_eye = 146.71
fovy_per_eye = 150  # fovx_per_eye * (2 / np.sqrt(3))
raw_img_height_px = 512
raw_img_width_px = 450
retina_side_len_hex = 16
num_ommatidia_per_eye = 3 * retina_side_len_hex**2 - 3 * retina_side_len_hex + 1
eye_positions = [(0.75, 0.3, 1.32), (0.75, -0.3, 1.32)]  # left, right
eye_orientations = [(1.57, -0.4676, 0), (-1.57, -0.4676, 3.14)]  # L, R as Euler angles


# Leg adhesion
# joint velocities threshold extracted from experiments
adhesion_speed_thresholds = np.array(
    [
        -22.24454997,
        -12.13565398,
        -9.14855537,
        -20.7181815,
        12.49711737,
        10.15158114,
    ]
)

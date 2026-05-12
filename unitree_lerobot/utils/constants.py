import dataclasses


@dataclasses.dataclass(frozen=True)
class RobotConfig:
    motors: list[str]
    cameras: list[str]
    camera_to_image_key: dict[str, str]
    json_state_data_name: list[str]
    json_action_data_name: list[str]
    # FleetGlue addition: optional per-camera image shape (H, W, C). Defaults to (480, 640, 3)
    # for backward compatibility with all existing Unitree configs. Set to (480, 320, 3) for
    # the FleetGlue stereo config where each half-frame is half-width.
    image_shape: tuple = (480, 640, 3)


Z1_CONFIG = RobotConfig(
    motors=[
        "kLeftWaist",
        "kLeftShoulder",
        "kLeftElbow",
        "kLeftForearmRoll",
        "kLeftWristAngle",
        "kLeftWristRotate",
        "kLeftGripper",
        "kRightWaist",
        "kRightShoulder",
        "kRightElbow",
        "kRightForearmRoll",
        "kRightWristAngle",
        "kRightWristRotate",
        "kRightGripper",
    ],
    cameras=[
        "cam_high",
        "cam_left_wrist",
        "cam_right_wrist",
    ],
    camera_to_image_key={"color_0": "cam_high", "color_1": "cam_left_wrist", "color_2": "cam_right_wrist"},
    json_state_data_name=["left_arm.qpos", "right_arm.qpos"],
    json_action_data_name=["left_arm.qpos", "right_arm.qpos"],
)


Z1_SINGLE_CONFIG = RobotConfig(
    motors=[
        "kWaist",
        "kShoulder",
        "kElbow",
        "kForearmRoll",
        "kWristAngle",
        "kWristRotate",
        "kGripper",
    ],
    cameras=[
        "cam_high",
        "cam_wrist",
    ],
    camera_to_image_key={"color_0": "cam_high", "color_1": "cam_wrist"},
    json_state_data_name=["left_arm.qpos", "right_arm.qpos"],
    json_action_data_name=["left_arm.qpos", "right_arm.qpos"],
)


G1_DEX1_CONFIG = RobotConfig(
    motors=[
        "kLeftShoulderPitch",
        "kLeftShoulderRoll",
        "kLeftShoulderYaw",
        "kLeftElbow",
        "kLeftWristRoll",
        "kLeftWristPitch",
        "kLeftWristYaw",
        "kRightShoulderPitch",
        "kRightShoulderRoll",
        "kRightShoulderYaw",
        "kRightElbow",
        "kRightWristRoll",
        "kRightWristPitch",
        "kRightWristYaw",
        "kLeftGripper",
        "kRightGripper",
    ],
    cameras=[
        "cam_left_high",
        "cam_right_high",
        "cam_left_wrist",
        "cam_right_wrist",
    ],
    camera_to_image_key={
        "color_0": "cam_left_high",
        "color_1": "cam_right_high",
        "color_2": "cam_left_wrist",
        "color_3": "cam_right_wrist",
    },
    json_state_data_name=["left_arm.qpos", "right_arm.qpos", "left_ee.qpos", "right_ee.qpos"],
    json_action_data_name=["left_arm.qpos", "right_arm.qpos", "left_ee.qpos", "right_ee.qpos"],
)


G1_DEX1_CONFIG_SIM = RobotConfig(
    motors=[
        "kLeftShoulderPitch",
        "kLeftShoulderRoll",
        "kLeftShoulderYaw",
        "kLeftElbow",
        "kLeftWristRoll",
        "kLeftWristPitch",
        "kLeftWristYaw",
        "kRightShoulderPitch",
        "kRightShoulderRoll",
        "kRightShoulderYaw",
        "kRightElbow",
        "kRightWristRoll",
        "kRightWristPitch",
        "kRightWristYaw",
        "kLeftGripper",
        "kRightGripper",
    ],
    cameras=[
        "cam_left_high",
        "cam_left_wrist",
        "cam_right_wrist",
    ],
    camera_to_image_key={
        "color_0": "cam_left_high",
        "color_1": "cam_left_wrist",
        "color_2": "cam_right_wrist",
    },
    json_state_data_name=["left_arm.qpos", "right_arm.qpos", "left_ee.qpos", "right_ee.qpos"],
    json_action_data_name=["left_arm.qpos", "right_arm.qpos", "left_ee.qpos", "right_ee.qpos"],
)


G1_DEX3_CONFIG = RobotConfig(
    motors=[
        "kLeftShoulderPitch",
        "kLeftShoulderRoll",
        "kLeftShoulderYaw",
        "kLeftElbow",
        "kLeftWristRoll",
        "kLeftWristPitch",
        "kLeftWristYaw",
        "kRightShoulderPitch",
        "kRightShoulderRoll",
        "kRightShoulderYaw",
        "kRightElbow",
        "kRightWristRoll",
        "kRightWristPitch",
        "kRightWristYaw",
        "kLeftHandThumb0",
        "kLeftHandThumb1",
        "kLeftHandThumb2",
        "kLeftHandMiddle0",
        "kLeftHandMiddle1",
        "kLeftHandIndex0",
        "kLeftHandIndex1",
        "kRightHandThumb0",
        "kRightHandThumb1",
        "kRightHandThumb2",
        "kRightHandIndex0",
        "kRightHandIndex1",
        "kRightHandMiddle0",
        "kRightHandMiddle1",
    ],
    cameras=[
        "cam_left_high",
        "cam_right_high",
        "cam_left_wrist",
        "cam_right_wrist",
    ],
    camera_to_image_key={
        "color_0": "cam_left_high",
        "color_1": "cam_right_high",
        "color_2": "cam_left_wrist",
        "color_3": "cam_right_wrist",
    },
    json_state_data_name=["left_arm.qpos", "right_arm.qpos", "left_ee.qpos", "right_ee.qpos"],
    json_action_data_name=["left_arm.qpos", "right_arm.qpos", "left_ee.qpos", "right_ee.qpos"],
)


G1_BRAINCO_CONFIG = RobotConfig(
    motors=[
        "kLeftShoulderPitch",
        "kLeftShoulderRoll",
        "kLeftShoulderYaw",
        "kLeftElbow",
        "kLeftWristRoll",
        "kLeftWristPitch",
        "kLeftWristYaw",
        "kRightShoulderPitch",
        "kRightShoulderRoll",
        "kRightShoulderYaw",
        "kRightElbow",
        "kRightWristRoll",
        "kRightWristPitch",
        "kRightWristYaw",
        "kLeftHandThumb",
        "kLeftHandThumbAux",
        "kLeftHandIndex",
        "kLeftHandMiddle",
        "kLeftHandRing",
        "kLeftHandPinky",
        "kRightHandThumb",
        "kRightHandThumbAux",
        "kRightHandIndex",
        "kRightHandMiddle",
        "kRightHandRing",
        "kRightHandPinky",
    ],
    cameras=[
        "cam_left_high",
        "cam_right_high",
        "cam_left_wrist",
        "cam_right_wrist",
    ],
    camera_to_image_key={
        "color_0": "cam_left_high",
        "color_1": "cam_right_high",
        "color_2": "cam_left_wrist",
        "color_3": "cam_right_wrist",
    },
    json_state_data_name=["left_arm.qpos", "right_arm.qpos", "left_ee.qpos", "right_ee.qpos"],
    json_action_data_name=["left_arm.qpos", "right_arm.qpos", "left_ee.qpos", "right_ee.qpos"],
)


G1_INSPIRE_CONFIG = RobotConfig(
    motors=[
        "kLeftShoulderPitch",
        "kLeftShoulderRoll",
        "kLeftShoulderYaw",
        "kLeftElbow",
        "kLeftWristRoll",
        "kLeftWristPitch",
        "kLeftWristYaw",
        "kRightShoulderPitch",
        "kRightShoulderRoll",
        "kRightShoulderYaw",
        "kRightElbow",
        "kRightWristRoll",
        "kRightWristPitch",
        "kRightWristYaw",
        "kLeftHandPinky",
        "kLeftHandRing",
        "kLeftHandMiddle",
        "kLeftHandIndex",
        "kLeftHandThumbBend",
        "kLeftHandThumbRotation",
        "kRightHandPinky",
        "kRightHandRing",
        "kRightHandMiddle",
        "kRightHandIndex",
        "kRightHandThumbBend",
        "kRightHandThumbRotation",
    ],
    cameras=[
        "cam_left_high",
        "cam_right_high",
        "cam_left_wrist",
        "cam_right_wrist",
    ],
    camera_to_image_key={
        "color_0": "cam_left_high",
        "color_1": "cam_right_high",
        "color_2": "cam_left_wrist",
        "color_3": "cam_right_wrist",
    },
    json_state_data_name=["left_arm.qpos", "right_arm.qpos", "left_ee.qpos", "right_ee.qpos"],
    json_action_data_name=["left_arm.qpos", "right_arm.qpos", "left_ee.qpos", "right_ee.qpos"],
)


MOVEIBLE_LIFT_G1_DEX1_USEWAIST_CONFIG = RobotConfig(
    motors=[
        "kLeftShoulderPitch",
        "kLeftShoulderRoll",
        "kLeftShoulderYaw",
        "kLeftElbow",
        "kLeftWristRoll",
        "kLeftWristPitch",
        "kLeftWristYaw",
        "kRightShoulderPitch",
        "kRightShoulderRoll",
        "kRightShoulderYaw",
        "kRightElbow",
        "kRightWristRoll",
        "kRightWristPitch",
        "kRightWristYaw",
        "kWaistYaw",
        "kWaistPitch",
        "kHighLift",
        "kMoveX",
        "kMoveYaw",
        "kLeftGripper",
        "kRightGripper",
    ],
    cameras=[
        "cam_left_high",
        "cam_right_high",
        "cam_left_wrist",
        "cam_right_wrist",
    ],
    camera_to_image_key={
        "color_0": "cam_left_high",
        "color_1": "cam_right_high",
        "color_2": "cam_left_wrist",
        "color_3": "cam_right_wrist",
    },
    json_state_data_name=[
        "left_arm.qpos",
        "right_arm.qpos",
        "waist.qpos",
        "torso.height",
        "chassis.qvel",
        "left_ee.qpos",
        "right_ee.qpos",
    ],
    json_action_data_name=[
        "left_arm.qpos",
        "right_arm.qpos",
        "waist.qpos",
        "torso.qvel",
        "chassis.qvel",
        "left_ee.qpos",
        "right_ee.qpos",
    ],
)


MOVEIBLE_LIFT_G1_DEX1_NOUSEWAIST_CONFIG = RobotConfig(
    motors=[
        "kLeftShoulderPitch",
        "kLeftShoulderRoll",
        "kLeftShoulderYaw",
        "kLeftElbow",
        "kLeftWristRoll",
        "kLeftWristPitch",
        "kLeftWristYaw",
        "kRightShoulderPitch",
        "kRightShoulderRoll",
        "kRightShoulderYaw",
        "kRightElbow",
        "kRightWristRoll",
        "kRightWristPitch",
        "kRightWristYaw",
        "kHighLift",
        "kMoveX",
        "kMoveYaw",
        "kLeftGripper",
        "kRightGripper",
    ],
    cameras=[
        "cam_left_high",
        "cam_right_high",
        "cam_left_wrist",
        "cam_right_wrist",
    ],
    camera_to_image_key={
        "color_0": "cam_left_high",
        "color_1": "cam_right_high",
        "color_2": "cam_left_wrist",
        "color_3": "cam_right_wrist",
    },
    json_state_data_name=[
        "left_arm.qpos",
        "right_arm.qpos",
        "torso.height",
        "chassis.qvel",
        "left_ee.qpos",
        "right_ee.qpos",
    ],
    json_action_data_name=[
        "left_arm.qpos",
        "right_arm.qpos",
        "torso.qvel",
        "chassis.qvel",
        "left_ee.qpos",
        "right_ee.qpos",
    ],
)


LIFT_G1_DEX1_USEWAIST_CONFIG = RobotConfig(
    motors=[
        "kLeftShoulderPitch",
        "kLeftShoulderRoll",
        "kLeftShoulderYaw",
        "kLeftElbow",
        "kLeftWristRoll",
        "kLeftWristPitch",
        "kLeftWristYaw",
        "kRightShoulderPitch",
        "kRightShoulderRoll",
        "kRightShoulderYaw",
        "kRightElbow",
        "kRightWristRoll",
        "kRightWristPitch",
        "kRightWristYaw",
        "kWaistYaw",
        "kWaistRoll",
        "kHighLift",
        "kLeftGripper",
        "kRightGripper",
    ],
    cameras=[
        "cam_left_high",
        "cam_right_high",
        "cam_left_wrist",
        "cam_right_wrist",
    ],
    camera_to_image_key={
        "color_0": "cam_left_high",
        "color_1": "cam_right_high",
        "color_2": "cam_left_wrist",
        "color_3": "cam_right_wrist",
    },
    json_state_data_name=[
        "left_arm.qpos",
        "right_arm.qpos",
        "waist.qpos",
        "torso.height",
        "left_ee.qpos",
        "right_ee.qpos",
    ],
    json_action_data_name=[
        "left_arm.qpos",
        "right_arm.qpos",
        "waist.qpos",
        "torso.qvel",
        "left_ee.qpos",
        "right_ee.qpos",
    ],
)


LIFT_G1_DEX1_NOUSEWAIST_CONFIG = RobotConfig(
    motors=[
        "kLeftShoulderPitch",
        "kLeftShoulderRoll",
        "kLeftShoulderYaw",
        "kLeftElbow",
        "kLeftWristRoll",
        "kLeftWristPitch",
        "kLeftWristYaw",
        "kRightShoulderPitch",
        "kRightShoulderRoll",
        "kRightShoulderYaw",
        "kRightElbow",
        "kRightWristRoll",
        "kRightWristPitch",
        "kRightWristYaw",
        "kHighLift",
        "kLeftGripper",
        "kRightGripper",
    ],
    cameras=[
        "cam_left_high",
        "cam_right_high",
        "cam_left_wrist",
        "cam_right_wrist",
    ],
    camera_to_image_key={
        "color_0": "cam_left_high",
        "color_1": "cam_right_high",
        "color_2": "cam_left_wrist",
        "color_3": "cam_right_wrist",
    },
    json_state_data_name=["left_arm.qpos", "right_arm.qpos", "torso.height", "left_ee.qpos", "right_ee.qpos"],
    json_action_data_name=["left_arm.qpos", "right_arm.qpos", "torso.qvel", "left_ee.qpos", "right_ee.qpos"],
)

# FleetGlue: G1 EDU+ (U2) with 3-DOF waist, prosthetic grippers (no dex hands), single head camera.
# Matches xr_teleoperate EpisodeWriter output: states/actions use the `body.qpos` field (3 elements
# = waist yaw/roll/pitch) populated only when --head-tracking is on. Mirrors the existing G1 configs
# with two FleetGlue-specific deviations: (1) reads from `body.qpos` (xr_teleoperate's name) rather
# than `waist.qpos` (Unitree LIFT config name); (2) only `cam_head` since this G1 has no wrist cams.
G1_EDU_PLUS_FLEETGLUE_CONFIG = RobotConfig(
    motors=[
        "kLeftShoulderPitch","kLeftShoulderRoll","kLeftShoulderYaw","kLeftElbow",
        "kLeftWristRoll","kLeftWristPitch","kLeftWristYaw",
        "kRightShoulderPitch","kRightShoulderRoll","kRightShoulderYaw","kRightElbow",
        "kRightWristRoll","kRightWristPitch","kRightWristYaw",
        "kWaistYaw","kWaistRoll","kWaistPitch",
    ],
    cameras=["cam_head"],
    camera_to_image_key={"color_0": "cam_head"},
    json_state_data_name=["left_arm.qpos", "right_arm.qpos", "body.qpos"],
    json_action_data_name=["left_arm.qpos", "right_arm.qpos", "body.qpos"],
)

# FleetGlue stereo: same as above but for IR-stereo head camera mode (g1-cam-stereo). In stereo
# mode, xr_teleoperate's recorder splits the 480x640 frame into left half (color_0) + right half
# (color_1), each 480x320. Two cameras, each at the half-shape.
G1_EDU_PLUS_FLEETGLUE_STEREO_CONFIG = RobotConfig(
    motors=[
        "kLeftShoulderPitch","kLeftShoulderRoll","kLeftShoulderYaw","kLeftElbow",
        "kLeftWristRoll","kLeftWristPitch","kLeftWristYaw",
        "kRightShoulderPitch","kRightShoulderRoll","kRightShoulderYaw","kRightElbow",
        "kRightWristRoll","kRightWristPitch","kRightWristYaw",
        "kWaistYaw","kWaistRoll","kWaistPitch",
    ],
    cameras=["cam_head_left", "cam_head_right"],
    camera_to_image_key={"color_0": "cam_head_left", "color_1": "cam_head_right"},
    json_state_data_name=["left_arm.qpos", "right_arm.qpos", "body.qpos"],
    json_action_data_name=["left_arm.qpos", "right_arm.qpos", "body.qpos"],
    image_shape=(480, 320, 3),
)


ROBOT_CONFIGS = {
    "Unitree_Z1_Single": Z1_SINGLE_CONFIG,
    "Unitree_Z1_Dual": Z1_CONFIG,
    "Unitree_G1_Dex1": G1_DEX1_CONFIG,
    "Unitree_G1_Dex1_Sim": G1_DEX1_CONFIG_SIM,
    "Unitree_G1_Dex3": G1_DEX3_CONFIG,
    "Unitree_G1_Brainco": G1_BRAINCO_CONFIG,
    "Unitree_G1_Inspire": G1_INSPIRE_CONFIG,
    "Unitree_G1_MoveibleLift_Dex1_UseWaist": MOVEIBLE_LIFT_G1_DEX1_USEWAIST_CONFIG,
    "Unitree_G1_MoveibleLift_Dex1_NoUseWaist": MOVEIBLE_LIFT_G1_DEX1_NOUSEWAIST_CONFIG,
    "Unitree_G1_Lift_Dex1_UseWaist": LIFT_G1_DEX1_USEWAIST_CONFIG,
    "Unitree_G1_Lift_Dex1_NoUseWaist": LIFT_G1_DEX1_NOUSEWAIST_CONFIG,
    # FleetGlue (2026-05-11): G1 EDU+ with 3-DOF waist, prosthetic grippers, monocular head cam.
    "Unitree_G1_EDU_Plus_FleetGlue": G1_EDU_PLUS_FLEETGLUE_CONFIG,
    # FleetGlue stereo variant — for IR-stereo head cam mode (cam_head_left + cam_head_right, 480x320 each).
    "Unitree_G1_EDU_Plus_FleetGlue_Stereo": G1_EDU_PLUS_FLEETGLUE_STEREO_CONFIG,
}

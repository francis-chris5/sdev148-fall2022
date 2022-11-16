/// @DnDAction : YoYo Games.Common.If_Variable
/// @DnDVersion : 1
/// @DnDHash : 171EA8AE
/// @DnDArgument : "var" "isJumping"
if(isJumping == 0)
{
	/// @DnDAction : YoYo Games.Common.Variable
	/// @DnDVersion : 1
	/// @DnDHash : 22707E89
	/// @DnDParent : 171EA8AE
	/// @DnDArgument : "expr" "1"
	/// @DnDArgument : "var" "isJumping"
	isJumping = 1;

	/// @DnDAction : YoYo Games.Movement.Set_Direction_Fixed
	/// @DnDVersion : 1.1
	/// @DnDHash : 3C2BAD10
	/// @DnDParent : 171EA8AE
	/// @DnDArgument : "direction" "90"
	direction = 90;

	/// @DnDAction : YoYo Games.Movement.Set_Speed
	/// @DnDVersion : 1
	/// @DnDHash : 09F10678
	/// @DnDParent : 171EA8AE
	/// @DnDArgument : "speed" "30"
	speed = 30;

	/// @DnDAction : YoYo Games.Movement.Set_Gravity_Force
	/// @DnDVersion : 1
	/// @DnDHash : 0C768877
	/// @DnDParent : 171EA8AE
	gravity = 1;
}
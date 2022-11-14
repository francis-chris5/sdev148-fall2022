/// @DnDAction : YoYo Games.Common.If_Variable
/// @DnDVersion : 1
/// @DnDHash : 7064C510
/// @DnDArgument : "var" "objSnowman.y"
/// @DnDArgument : "op" "3"
/// @DnDArgument : "value" "-164"
if(objSnowman.y <= -164)
{
	/// @DnDAction : YoYo Games.Movement.Set_Direction_Fixed
	/// @DnDVersion : 1.1
	/// @DnDHash : 7F5F0ECE
	/// @DnDParent : 7064C510
	speed = 0;
	direction = 0;

	/// @DnDAction : YoYo Games.Movement.Set_Speed
	/// @DnDVersion : 1
	/// @DnDHash : 39C1A065
	/// @DnDParent : 7064C510
	speed = 0;

	/// @DnDAction : YoYo Games.Movement.Jump_To_Start
	/// @DnDVersion : 1
	/// @DnDHash : 1A6960F4
	/// @DnDParent : 7064C510
	x = xstart;
	y = ystart;
}
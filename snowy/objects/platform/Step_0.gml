/// @DnDAction : YoYo Games.Common.Variable
/// @DnDVersion : 1
/// @DnDHash : 4CADA155
/// @DnDArgument : "expr" "-1"
/// @DnDArgument : "expr_relative" "1"
/// @DnDArgument : "var" "alarm"
alarm += -1;

/// @DnDAction : YoYo Games.Common.If_Variable
/// @DnDVersion : 1
/// @DnDHash : 46EB5D55
/// @DnDArgument : "var" "alarm"
/// @DnDArgument : "op" "3"
if(alarm <= 0)
{
	/// @DnDAction : YoYo Games.Movement.Jump_To_Start
	/// @DnDVersion : 1
	/// @DnDHash : 710D04D7
	/// @DnDParent : 46EB5D55
	x = xstart;
	y = ystart;
}
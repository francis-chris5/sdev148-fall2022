/// @DnDAction : YoYo Games.Audio.Audo_Set_Master_Volume
/// @DnDVersion : 1
/// @DnDHash : 7E91D8AC
/// @DnDArgument : "volume" "20"
audio_set_master_gain(0, 20);

/// @DnDAction : YoYo Games.Audio.Play_Audio
/// @DnDVersion : 1.1
/// @DnDHash : 5E88D2BC
/// @DnDArgument : "soundid" "Sound1"
/// @DnDSaveInfo : "soundid" "Sound1"
audio_play_sound(Sound1, 0, 0, 1.0, undefined, 1.0);

/// @DnDAction : YoYo Games.Instances.Change_Instance
/// @DnDVersion : 1
/// @DnDHash : 08B5C9ED
/// @DnDArgument : "objind" "objSnowstreams"
/// @DnDSaveInfo : "objind" "objSnowstreams"
instance_change(objSnowstreams, true);
exec(compile((ROOT/'v10/common.py').read_text(),'<common>','exec'))
Y=23.343134;Z=685
c=parts['T01_Knee_motor_rail_shell_PROVISIONAL'].component
holes(c,'x',28.9,14.1,[(Y+s*20,Z+t*33,2.25)for s in [-1,1]for t in [-1,1]],'Restore_motor_bores_through_joined_saddles')
holes(c,'x',37,6,[(Y+s*20,Z+t*33,3.75)for s in [-1,1]for t in [-1,1]],'Motor_M4_socket_head_access')
for sign,label in [(-1,'Lower'),(1,'Upper')]:
 c=parts['T02_Rail_clamp_cap_'+label+'_PROVISIONAL'].component
 holes(c,'x',43.2,11,[(Y+s*20,Z+sign*33,4)for s in [-1,1]],'Motor_screw_tool_access_through_cap')
result={'mount_access_completed':True}

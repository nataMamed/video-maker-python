import subprocess
import os

aerender_file_path = 'C:\Program Files\Adobe\Adobe After Effects 2020\Support Files'
template_file_path = ''.join('C:\ Users\ natam\Documents\ video-maker-python\ templates\ 1\ template.aep'.split())
output_file_path = ''.join('C:\ Users\ natam\Documents\ video-maker-python\content\output.mov'.split())

# subprocess.call([aerender_file_path ,'-comp', 'main'
#   '-project', template_file_path,
#   '-output', output_file_path])
#subprocess.Popen(aerender_file_path,['-project',template_file_path,'-output',output_file_path],)
subprocess.call('C:\Program Files\Adobe\Adobe After Effects 2020\Support Files\aerender.exe')
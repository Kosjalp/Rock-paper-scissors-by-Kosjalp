import os
def playsound(user_os, playsoundfilepath):
  if user_os == "Mac":
    os.system(f"afplay {playsoundfilepath}")
  elif user_os == "Linux":
    os.system(f"aplay {playsoundfilepath}")
  elif user_os == "Windows":
    os.system(f"start {playsoundfilepath}")

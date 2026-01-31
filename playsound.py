import os
def playsound(user_os, playsoundfilepath):
  if user_os == "UNIX":
    os.system(f"afplay {playsoundfilepath}")
  elif user_os == "Windows":
    os.system(f"start {playsoundfilepath}")
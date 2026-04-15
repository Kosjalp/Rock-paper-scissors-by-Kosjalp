import os

def playsound(user_os, playsoundfilepath, async_play=True):
  if user_os == "Mac":
    os.system(f"afplay \"{playsoundfilepath}\"")
  elif user_os == "Linux":
    os.system(f"ffplay -nodisp -autoexit \"{playsoundfilepath}\" >/dev/null 2>&1")
  elif user_os == "Windows":
    #Some artifical intellegence was used in the creation of the following code.
    try:
      import winsound
      flags = winsound.SND_FILENAME | winsound.SND_NODEFAULT
      if async_play:
        flags |= winsound.SND_ASYNC
      else:
        flags |= winsound.SND_SYNC
      winsound.PlaySound(playsoundfilepath, flags)
    except Exception:
      pass
    #End of the artifical intellegence generated code.
